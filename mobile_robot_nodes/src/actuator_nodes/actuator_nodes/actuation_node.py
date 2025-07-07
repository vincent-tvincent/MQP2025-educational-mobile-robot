from .moving_package.chassis_drive import *
from .moving_package.gimbal_drive import * 
from .moving_package.actuator_package.servo_port_handler import *
from .moving_package.actuator_package.xl330_constant import *

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

from std_msgs.msg import Int16


node_name = 'robot_actuation'
queue_size = 200
chassis_publish_interval = 1 / 500
gimbal_publish_interval = 1 / 500

chassis_goal_topic_name = 'goal_chassis'
gimbal_goal_topic_name = 'goal_gimbal'
chassis_commend_topic_name = 'commend_chassis'
gimbal_commend_topic_name = 'commend_gimbal'

chassis_feedback_twist_topic_name = 'feedback_twist_chassis'
gimbal_feedback_euler_topic_name = 'feedback_euler_gimbal'


class actuation_node(Node):
    def __init__(self):
        super().__init__(node_name) 
        # robot init

        #init port
        self.port_handler = port_init()
        port_open(self.port_handler)
        
        #init servos 
        self.chassis = chassis_4wdiff(self.port_handler) 
        self.gimbal = gimbal_yaw_pitch(self.port_handler)
        feedback = self.chassis.read_feedback_4wdiff()
        self.init_pos = feedback[FEEDBACK_POSITION_NAME]
        self.set_lock = False

        #start up devices  
        self.chassis.enable_torque()        
        self.gimbal.enable_torque()
        
        self.gimbal.gimbal_zeroing()

        # ros2 init
        self.chassis__goal_subscription = self.create_subscription(
            Twist,
            chassis_goal_topic_name,
            self.set_chassis_goal,
            queue_size
        ) 

        self.gimbal_goal_subscription = self.create_subscription(
           Vector3,
            gimbal_goal_topic_name,
            self.set_gimbal_goal,
            queue_size
        )

        self.chassis_commend_subscription = self.create_subscription(
            Int16,
            chassis_commend_topic_name,
            self.set_chassis_commend,
            queue_size
        )

        self.gimbal_commend_subscription = self.create_subscription(
            Int16,
            gimbal_commend_topic_name,
            self.set_gimbal_commend,
            queue_size
        )

        self.chassis_feedback_publishing = self.create_publisher(
            Twist,
            chassis_feedback_twist_topic_name,
            queue_size
        ) 

        self.gimbal_feedback_publishing = self.create_publisher(
            Vector3,
            gimbal_feedback_euler_topic_name,
            queue_size
        )

        #start publisher timer 
        self.chassis_publishing_timer = self.create_timer(
            chassis_publish_interval,
            self.publish_chassis_feedback
        ) 
        
        self.gimbal_publishing_timer = self.create_timer(
            gimbal_publish_interval,
            self.publish_gimbal_feedback
        )


    def set_chassis_goal(self, msg: Twist):
        self.get_logger().info(f"receive goal{msg}")
        self.set_lock = True
        result = COMM_PORT_BUSY
        while result == COMM_PORT_BUSY:
            result = self.chassis.set_speed_4wdiff([msg.linear.x, msg.angular.z])
        self.set_lock = False


    def set_gimbal_goal(self, msg: Vector3):
        self.set_lock = True
        result = COMM_PORT_BUSY
        # print("get gimbal goal")
        while result == COMM_PORT_BUSY:
            result = self.gimbal.set_gimbal_position([msg.z, msg.y])
        # print("gimbal goal setted")
        self.set_lock = False


    def set_chassis_commend(self, msg: Int16):
        if msg == 0:
            self.chassis.disable_torque()
        elif msg == 1:
            self.chassis.enable_torque()


    def set_gimbal_commend(self, msg: Int16):
        self.set_lock = True
        result = COMM_PORT_BUSY
        if msg.data == 0:
            while result == COMM_PORT_BUSY:
                result = self.gimbal.disable_torque()
            time.sleep(0.5)
        elif msg.data == 1:
            while result == COMM_PORT_BUSY:
                result = self.gimbal.enable_torque()
            time.sleep(0.5)
        elif msg.data == 2:
            while result == COMM_PORT_BUSY:
                result = self.gimbal.gimbal_zeroing()
            # print("here")
            time.sleep(0.5)
        self.set_lock = False

    
    def publish_chassis_feedback(self):
        if self.set_lock:
            return 
        feedback = self.chassis.read_feedback_4wdiff()
        message = Twist()
        for key in feedback.keys():
            if key == FEEDBACK_VELOCITY_NAME:
                lf_wheel_velocity = feedback[FEEDBACK_VELOCITY_NAME][0]
                lr_wheel_velocity = feedback[FEEDBACK_VELOCITY_NAME][1]
                rf_wheel_velocity = feedback[FEEDBACK_VELOCITY_NAME][2]
                rr_wheel_velocity = feedback[FEEDBACK_VELOCITY_NAME][3]
                
                l_eq_velocity = (lf_wheel_velocity + lr_wheel_velocity) / 2 * speed_unit
                r_eq_velocity = (rf_wheel_velocity + rr_wheel_velocity) / 2 * speed_unit
                
                diff_eq_velocity = r_eq_velocity - l_eq_velocity
                angular_velocity = diff_eq_velocity / rotation_diameter
                linear_velocity = min(l_eq_velocity, r_eq_velocity)

                message.angular.z = angular_velocity
                message.linear.x = linear_velocity
                # self.get_logger().info(f"publishing chassis velocity: {message.angular.x},{message.angular.y},{message.angular.z},{message.linear.x},{message.linear.y},{message.linear.z}")
                self.chassis_feedback_publishing.publish(message)
                 

    def publish_gimbal_feedback(self):
        if self.set_lock:
            return 
        feedback = self.gimbal.read_feedback_gimbal()
        message = Vector3()
        
        for key in feedback.keys():
            if key == FEEDBACK_POSITION_NAME:
                message.z = (feedback[key][0] - gimbal_quarter) * gimbal_step
                message.y = (feedback[key][1] - gimbal_quarter) * gimbal_step 

        # self.get_logger().info(f"publishing gimbal position: {message.x},{message.y},{message.z}")
        self.gimbal_feedback_publishing.publish(message)    


    def device_shoutdown(self):
        self.set_lock = True
        result = COMM_PORT_BUSY 
        while result == COMM_PORT_BUSY:
            result = self.chassis.set_speed_4wdiff([0,0])

        result = COMM_PORT_BUSY
        while result == COMM_PORT_BUSY:
            result = self.gimbal.gimbal_look_down()
        self.set_lock = False
        time.sleep(0.5)
        self.chassis.disable_torque()
        self.gimbal.disable_torque()
        time.sleep(0.5)
        port_close(self.port_handler)


def main(args=None):
    rclpy.init(args=args)
    node = actuation_node()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("shouting down")
    finally:
        #node.device_shoutdown()
        node.destroy_node()
     


if __name__ == '__main__':
    main() 
        