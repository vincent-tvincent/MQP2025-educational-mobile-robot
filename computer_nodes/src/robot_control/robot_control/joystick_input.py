from pydualsense import pydualsense

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

node_name = 'ps5_controller_node'

controller_topic_name = 'robot_controller'

joystick_publish_interval = 1 / 250

queue_size = 200

class ps5_joystick_node(Node):
    def __init__(self):
        super().__init__(node_name)
        self.controller = pydualsense()
        self.controller.init()

        self.joystick_publisher(
            Joy,
            controller_topic_name
        )

        self.timer = self.create_timer(
            joystick_publish_interval,
            self.publish_joystick_input,
            queue_size
        )

    def publish_joystick_input(self):
        pass
def main(args=None):
    rclpy.init(args=args)
    node = ()
    try:  
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("shouting down")
    finally:
        node.destroy_node() 


if __name__ == '__main__':
    main()