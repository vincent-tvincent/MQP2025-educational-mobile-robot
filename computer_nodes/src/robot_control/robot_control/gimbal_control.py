

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Vector3
from std_msgs.msg import Int16

import time
import math

node_name = 'gimbal_control'
chassis_goal_topic_name = 'goal_chassis'
gimbal_goal_topic_name = 'goal_gimbal'
chassis_commend_topic_name = 'commend_chassis'
gimbal_commend_topic_name = 'commend_gimbal'
manual_controller_topic = 'gimbal_manual_controller'

gimbal_feedback_euler_topic_name = 'feedback_euler_gimbal'

queue_size = 200
actuation_queue_size = 50

goal_publish_interval = 1 / 400

gimbal_zero = math.pi / 2
gimbal_start = 0
gimbal_end = math.pi

gimbal_range = gimbal_end - gimbal_start
class gimbal_control_node(Node): 
    def __init__(self):
        super().__init__(node_name)
        self.next_goal = [gimbal_zero, gimbal_zero] 
        # init publisher
        self.goal_publisher = self.create_publisher(
            Vector3,
            gimbal_goal_topic_name,
            queue_size
        )

        self.commend_publisher = self.create_publisher(
            Int16,
            gimbal_commend_topic_name,
            queue_size
        )

        # init subscriber 
        self.feedback_subscriber = self.create_subscription(
            Vector3,
            gimbal_feedback_euler_topic_name,
            self.handle_feedback,
            queue_size 
        )

        self.controller_subscriber = self.create_subscription(
            Vector3,
            manual_controller_topic,
            self.handle_control,
            actuation_queue_size
        )

        self.goal_timer = self.create_timer(
            goal_publish_interval,
            self.send_goal
        )

        # self.test_timer = self.create_timer(
        #     0.25,
        #     self.test
        # )
        # self.t = 0.0

    # def test(self):
    #     self.set_goal([self.t, self.t]) 
    #     # self.set_commend(0)

    #     self.t += 0.1
                         
    def handle_control(self, msg: Vector3):
        
        y_value = float(1.0 - msg.y) / 2.0
        z_value = float(1.0 - msg.z) / 2.0
    
        pitch = y_value * (gimbal_range - gimbal_start)
        yaw = z_value * (gimbal_range - gimbal_start) 
        self.next_goal = [yaw, pitch]


    def send_goal(self):
        self.set_goal(self.next_goal)


    def set_goal(self, goal: list[float]):
        message = Vector3()
        message.z = goal[0]
        message.y = goal[1]
        self.goal_publisher.publish(message) 


    def set_commend(self, commend: int):
        message = Int16()
        message.data = commend
        self.commend_publisher.publish(message)


    def handle_feedback(self, msg: Vector3):
        pass
        # print(f"recent feedback{msg.x}, {msg.y}, {msg.z}")
        

def main(args=None):
    rclpy.init(args=args)
    node = gimbal_control_node()
    try:  
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("shouting down")
    finally:
        node.destroy_node() 
        rclpy.shutdown()

if __name__ == '__main__':
    main()
