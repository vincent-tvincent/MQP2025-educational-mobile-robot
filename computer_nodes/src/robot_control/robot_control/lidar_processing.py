import rclpy
from rclpy.node import Node
import tf2_ros
import tf2_geometry_msgs
import tf_transformations

from sensor_msgs.msg import LaserScan, PointCloud2, PointField
from sensor_msgs_py import point_cloud2
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Vector3
from scipy.spatial.transform import Rotation
import math
import numpy
node_name = 'lidar_processing'
lidar_input_topic_name = 'scan'
odom_topic_name = 'odom_output'
euler_topic_name = 'fused_euler'

lidar_frame_id = 'robot_lidar'
lidar_pointcloud_topic_name = 'processed_pointcloud'

queue_size = 200
point_cloud_queue_size = 200
angle_offset = 0
enable_3d = False

class lidar_processing(Node):
    def __init__(self):
        super().__init__(node_name) 
        self.recent_odom = Odometry()
        self.recent_euler = Vector3() 

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

        self.euler_subscribtion = self.create_subscription(
            Vector3,
            euler_topic_name,
            self.handle_euler,
            queue_size
        )
        
        self.point_cloud_publisher = self.create_publisher(
            PointCloud2,
            lidar_pointcloud_topic_name,
            point_cloud_queue_size
            ) 

    def handle_odom(self, msg: Odometry):
        self.recent_odom = msg

    def handle_euler(self, msg: Vector3):
        self.recent_euler = msg

    def handle_scan(self, msg: LaserScan):
        msg.header.frame_id = lidar_frame_id
        # msg.header.stamp = self.get_clock().now().to_msg()  

        # self.lidar_processed_publisher.publish(msg)
        q = self.recent_odom.pose.pose.orientation
        x = self.recent_odom.pose.pose.position.x
        y = self.recent_odom.pose.pose.position.y
        z = self.recent_odom.pose.pose.position.z

        roll, pitch, yaw = tf_transformations.euler_from_quaternion([q.x, q.y, q.z, q.w])


        # include remapping on coordinartes thus you may see x yz "mismatch"
        ry = Rotation.from_euler('x', roll)
        rx = Rotation.from_euler('y', pitch)
        fields = [
            PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
            PointField(name='intensity', offset=12, datatype=PointField.FLOAT32, count=1),
            ] 
    
        points =numpy.array([numpy.array([
                    -v * numpy.cos((i * msg.angle_increment + msg.angle_min + yaw)) + x, 
                    -v * numpy.sin((i * msg.angle_increment + msg.angle_min)+ yaw) + y, 
                    z,
                    msg.intensities[i] / 255                    
                ]) 
                for i, v in enumerate(msg.ranges) 
                ])

        if enable_3d:
            for i in range(len(points)):
                points[i][0:3] = rx.apply(ry.apply(points[i][0:3]))        

        pointcloud_header = msg.header
        pointcloud = point_cloud2.create_cloud(pointcloud_header, fields, points)
        if abs(roll) < 0.5 and abs(pitch) < 0.5 and not enable_3d:
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
