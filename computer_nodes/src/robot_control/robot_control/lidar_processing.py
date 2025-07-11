import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math

node_name = 'lidar_processing'
lidar_input_topic_name = 'scan'
lidar_output_topic_name = 'processed_scan'
lidar_frame_id = 'robot_lidar'

queue_size = 200
angle_offset = 0

class lidar_processing(Node):
    def __init__(self):
        super().__init__(node_name) 
        
        self.lider_raw_subscription = self.create_subscription(
            LaserScan,
            lidar_input_topic_name, 
            self.handle_scan,
            queue_size)

        self.lidar_processed_publisher = self.create_publisher(
            LaserScan,
            lidar_output_topic_name,
            queue_size)


    def handle_scan(self, msg: LaserScan):
        msg.header.frame_id = lidar_frame_id
        msg.header.stamp = self.get_clock().now().to_msg()  
        msg.angle_min += angle_offset
        msg.angle_max += angle_offset
        self.lidar_processed_publisher.publish(msg) 


def main(args=None):
    rclpy.init(args=args)
    node = lidar_processing()
    try:  
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("shouting down")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
