import rclpy
from rclpy.node import Node
import tf2_ros
import tf2_geometry_msgs
import tf_transformations

from sensor_msgs.msg import LaserScan, PointCloud2
from sensor_msgs_py import point_cloud2
from nav_msgs.msg import Odometry
import math
import numpy
node_name = 'lidar_processing'
lidar_input_topic_name = 'scan'
lidar_output_topic_name = 'processed_scan'
odom_topic_name = 'odom_output'

chassis_frame_id = 'base_link'
lidar_frame_id = 'robot_lidar'
lidar_pointcloud_topic_name = 'processed_pointcloud'
pointcloud_frame_id = 'robot_lidar_pointcloud'

queue_size = 200
angle_offset = 0

class lidar_processing(Node):
    def __init__(self):
        super().__init__(node_name) 
        self.recent_odom = Odometry()
        self.transform_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.transform_buffer, self)

        self.lider_raw_subscription = self.create_subscription(
            LaserScan,
            lidar_input_topic_name, 
            self.handle_scan,
            queue_size
            )  

        self.odom_subscribtion = self.create_subscription(
            Odometry,
            odom_topic_name,
            self.handle_odom,
            queue_size
        )

        self.lidar_processed_publisher = self.create_publisher(
            LaserScan,
            lidar_output_topic_name,
            queue_size
            )
        
        self.point_cloud_publisher = self.create_publisher(
            PointCloud2,
            lidar_pointcloud_topic_name,
            queue_size
            ) 

    def handle_odom(self, msg: Odometry):
        self.recent_odom = msg

    def handle_scan(self, msg: LaserScan):
        msg.header.frame_id = lidar_frame_id
        # msg.header.stamp = self.get_clock().now().to_msg()  

        self.lidar_processed_publisher.publish(msg)
        q = self.recent_odom.pose.pose.orientation
        x = self.recent_odom.pose.pose.position.x
        y = self.recent_odom.pose.pose.position.y
        z = self.recent_odom.pose.pose.position.z
        roll, pitch, yaw = tf_transformations.euler_from_quaternion([q.x, q.y, q.z, q.w])

         
        points =numpy.array([[
                    -v * numpy.cos((i * msg.angle_increment + msg.angle_min + yaw)) + x, 
                    -v * numpy.sin((i * msg.angle_increment + msg.angle_min + yaw)) + y, 
                    0
                ] 
                for i, v in enumerate(msg.ranges) 
                ])
        

        
        pointcloud_header = msg.header
        pointcloud = point_cloud2.create_cloud_xyz32(pointcloud_header, points)
        self.point_cloud_publisher.publish(pointcloud)


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
