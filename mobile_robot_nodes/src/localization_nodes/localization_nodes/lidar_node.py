from .localization_package.lidar_driver import * 
from .localization_package.robot_constant import * 

import rclpy
from rclpy.node import Node 

from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int16
import numpy

node_name = 'robot_imu'
lidar_publishing_topic_name = 'lidar_scan'
lidar_commend_subscriber_topic_name = 'commend_lidar'

lidar_scan_interval = 1 / 500
queue_size = 50
lidar_buffer_size = 1000


'''
!!!! this one is incomplete and not used !!!!
'''
class lidar_node(Node):
    def __init__(self):
        super().__init__(node_name)
        self.lidar = lidar_c1()
        self.lidar.start_scan()

        self.data_buffer = numpy.array(lidar_buffer_size)
        self.quality_buffer = numpy.array(lidar_buffer_size) 
        self.angle_buffer = numpy.array(lidar_buffer_size)
        self.lidar_index = 0
        self.first_scan = True

        self.lidar_publisher = self.create_publisher(
            LaserScan,
            lidar_publishing_topic_name,
            queue_size
        )

        self.lidar_commend_subscriber = self.create_subscription(
            Int16,
            lidar_commend_subscriber_topic_name,
            self.handle_commend,
            queue_size
        )

        self.scan_timer = self.create_timer(
            lidar_scan_interval,
            self.get_scan             
        )


    def get_scan(self):
        angle, data = self.lidar.get_single_scan() 
        print(angle, data)
        


    def publish_scan(self):
        pass        
    def handle_commend(self, msg):
        pass


def main(args=None):
    rclpy.init(args=args)
    node = lidar_node()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("shouting down")
    finally:
        node.destroy_node()
     

if __name__ == '__main__':
    main()