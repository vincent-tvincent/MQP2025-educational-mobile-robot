
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist, TwistStamped, Vector3
from sensor_msgs.msg import Joy
from std_msgs.msg import Int16

import time
import math

node_name = 'chassis_control'
chassis_goal_topic_name = 'goal_chassis'
chassis_commend_topic_name = 'commend_chassis'
chassis_feedback_euler_topic_name = 'feedback_twist_chassis'
odometry_generator_topic_name = 'odom_in_twist'
controller_topic_name = 'robot_controller'
gimbal_manual_controller_topic_name = 'gimbal_manual_controller'


chassis_goal_interval = 1 / 400


chassis_frame_id = 'base_link'

queue_size = 200

robot_linear_speed_limit = 200
robot_angular_speed_limit = math.pi * 2

class chassis_control_node(Node): 
    def __init__(self):
        super().__init__(node_name)

        self.next_goal = [0.0, 0.0]
        
        # init publisher
        self.goal_publisher = self.create_publisher(
            Twist,
            chassis_goal_topic_name,
            queue_size
        )

        self.commend_publisher = self.create_publisher(
            Int16,
            chassis_commend_topic_name,
            queue_size
        )

        self.odom_publisher = self.create_publisher(
            TwistStamped,
            odometry_generator_topic_name,
            queue_size 
        )

        self.gimbal_manual_control_publisher = self.create_publisher(
            Vector3,
            gimbal_manual_controller_topic_name,
            queue_size
        )

        # init subscriber 
        self.feedback_subscriber = self.create_subscription(
            TwistStamped,
            chassis_feedback_euler_topic_name,
            self.handle_feedback,
            queue_size 
        ) 

        self.control_subscriber = self.create_subscription(
            Joy,
            controller_topic_name,
            self.handle_control,
            queue_size
        )
 
        self.goal_timer = self.create_timer(
            chassis_goal_interval,
            self.send_goal
        )

        self.left_direction_joystick = True


    def handle_control(self, msg: Joy):
        ls = msg.buttons[0]
        rs = msg.buttons[1]
        ljb = msg.buttons[2]
        rjb = msg.buttons[3]

        lx = msg.axes[0]
        ly = msg.axes[1]
        lt = msg.axes[2]

        rx = msg.axes[3]
        ry = msg.axes[4]
        rt = msg.axes[5]

        if (self.left_direction_joystick and rjb != 0) or (not self.left_direction_joystick and ljb != 0):  
            self.left_direction_joystick = not self.left_direction_joystick

        velocity_control = 0
        direction_control = 0 
        fine_velocity_contol = 0
        gimbal_yaw_control = 0
        gimbal_pitch_control = 0

        if self.left_direction_joystick:
            direction_control = lx
            fine_velocity_contol = ly
            gimbal_pitch_control = ry
            gimbal_yaw_control = rx
            velocity_control = rt - lt
        else:
            direction_control = rx
            fine_velocity_contol = ry
            gimbal_pitch_control = ly
            gimbal_yaw_control = lx
            velocity_control = lt - rt
        
        # print(ry)
        # print(gimbal_pitch_control)
        gimbal_message = Vector3()
        gimbal_message.y = float(gimbal_pitch_control)
        gimbal_message.z = float(gimbal_yaw_control)
        self.gimbal_manual_control_publisher.publish(gimbal_message)

        if lt == 0 and rt == 0:
            linear_velocity = -1 * float(robot_linear_speed_limit) * 0.2 * fine_velocity_contol
        else:
            linear_velocity = float(robot_linear_speed_limit) * velocity_control

        angular_velocity = -1 * float(robot_angular_speed_limit) * direction_control
        # if linear_velocity != 0:
        #     angular_velocity *= linear_velocity / abs(linear_velocity)
        self.next_goal = [linear_velocity, angular_velocity]


    def send_goal(self):
        # self.next_goal = [0.0,0.1] 
        self.set_goal(self.next_goal)       


    def set_goal(self, goal: list[float]):
        message = Twist()
        message.linear.x = goal[0]
        message.angular.z = goal[1]
        self.goal_publisher.publish(message) 


    def set_commend(self, commend: int):
        message = Int16()
        message.data = commend
        self.commend_publisher.publish(message)


    # def __add_stamp(self, msg: Twist):
    #     out = TwistWithCovarianceStamped()
    #     out.header.stamp = self.get_clock().now().to_msg()
    #     out.header.frame_id = chassis_frame_id
    #     out.twist.twist = msg
    #     out.twist.covariance = [0.1]*36  # set realistic covariance values
    #     return out


    def handle_feedback(self, msg: TwistStamped):
        # print(f"recent feedback{msg.linear.x}, {msg.angular.z}")
        self.odom_publisher.publish(msg) 
         
        
def main(args=None):
    rclpy.init(args=args)
    node = chassis_control_node()
    try:  
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("shouting down")
    finally:
        node.destroy_node()
        rclpy.shutdown() 


if __name__ == '__main__':
    main()