
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from std_msgs.msg import Int16

import time

node_name = 'chassis_control'
chassis_goal_topic_name = 'goal_chassis'
chassis_commend_topic_name = 'commend_chassis'


chassis_feedback_euler_topic_name = 'feedback_twist_chassis'
 
queue_size = 200


class chassis_control_node(Node): 
    def __init__(self):
        super().__init__(node_name)
        
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

        # init subscriber 
        self.feedback_subscriber = self.create_subscription(
            Twist,
            chassis_feedback_euler_topic_name,
            self.handle_feedback,
            queue_size 
        )

        self.goal_timer = self.create_timer(
            chassis_goal_interval,
            self.send_goal
        )
        self.t = 0.0

    def send_goal(self):
        self.set_goal([0.0, 0.0]) 
        # self.set_commend(0)
        self.t += 0.5    
        # while True:
            # pass       


    def set_goal(self, goal: list[float]):
        message = Twist()
        message.linear.x = goal[0]
        message.angular.z = goal[1]
        self.goal_publisher.publish(message) 


    def set_commend(self, commend: int):
        message = Int16()
        message.data = commend
        self.commend_publisher.publish(message)
    
    def handle_feedback(self, msg: Twist):
        print(f"recent feedback{msg.linear.x}, {msg.angular.z}")
        

def main(args=None):
    rclpy.init(args=args)
    node = chassis_control_node()
    try:  
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("shouting down")
    finally:
        node.destroy_node() 


if __name__ == '__main__':
    main()