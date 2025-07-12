
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist, TwistStamped, Quaternion, Vector3

from nav_msgs.msg import Odometry

import numpy
from scipy.spatial.transform import Rotation
import math
import tf_transformations

node_name = 'odometry_generator'

frame_id = 'odom'
child_frame_id = 'base_link'

twist_in_topic = 'odom_in_twist'
imu_in_topic = 'odom_in_imu'
odom_out_topic = 'odom_output'
euler_fused_topic = 'fused_euler'

odometry_generating_interval = 1 / 400

acc_angle_trust_x = 0.005
acc_angle_trust_y = 0.005

yaw_gyro_trust = 0.5
yaw_encoder_trust = 1 - yaw_gyro_trust
# yaw_fusion_min_velocity = 5
# yaw_fusion_min_angular_velocity = numpy.pi / 8
queue_size = 200

class odometry_generator(Node):
    def __init__(self):
        super().__init__(node_name)

        self.odom_gyro = numpy.zeros(6) #odom able to culculate from gyro
        self.odom_acc = numpy.zeros(6) #odom able to culuculate from acc
        self.odom_twist = numpy.zeros(6) #odom able to calculate from twist
        self.enable_3d = True 

        # fusing imu 
        self.acc_trust = numpy.array([1, 1, 1, acc_angle_trust_x, acc_angle_trust_y, 0])
        self.gyro_trust = 1 - self.acc_trust

        self.imu_dt: float = 0.0
        self.twist_dt: float = 0.0
        self.first_call_imu_update = True
        self.first_call_twist_update = True
        self.imu_previous_t: float = 0.0
        self.twist_previous_t: float = 0.0

        self.recent_imu  = Imu()
        self.recent_twist = TwistStamped()

        self.imu_subscriber = self.create_subscription(
           Imu,
           imu_in_topic,
           self.update_imu,
           queue_size 
        ) 

        self.chassis_subscriber = self.create_subscription(
           TwistStamped,
           twist_in_topic,
           self.update_twist,
           queue_size 
        )

        self.odom_publisher = self.create_publisher(
           Odometry,
           odom_out_topic,
           queue_size  
        )

        self.fused_euler_publisher = self.create_publisher(
           Vector3,
           euler_fused_topic,
           queue_size  
        )

        self.odom_timer = self.create_timer(
           odometry_generating_interval,
           self.generate_odometry
        ) 

    def __imu_to_numpy(self, msg: Imu):
        output = numpy.zeros(6)
        output[0] = msg.linear_acceleration.x
        output[1] = msg.linear_acceleration.y
        output[2] = msg.linear_acceleration.z
        output[3] = msg.angular_velocity.x
        output[4] = msg.angular_velocity.y
        output[5] = msg.angular_velocity.z
        return output
    
    
    def __twist_to_numpy(self, msg: TwistStamped):
        output = numpy.zeros(6)
        output[0] = msg.twist.linear.x
        output[1] = msg.twist.linear.y
        output[2] = msg.twist.linear.z
        output[3] = msg.twist.angular.x
        output[4] = msg.twist.angular.y
        output[5] = msg.twist.angular.z
        return output
    

    def stamp_to_sec(self, sec: int, nanosec: int) -> float:
        return float(sec) + float(nanosec) / 1e9    

    # generate imu frame transformation 
    def update_imu(self, msg: Imu):
        # print("get imu")
        self.recent_imu = msg
        imu_t = self.stamp_to_sec(msg.header.stamp.sec, msg.header.stamp.nanosec)
        if self.first_call_imu_update:
            self.imu_previous_t = imu_t 
            self.first_call_imu_update = False
        self.imu_dt = imu_t - self.imu_previous_t
        self.imu_previous_t = imu_t

        # print(self.imu_dt)
        
        new_data = self.__imu_to_numpy(msg)
        ax,ay,az = new_data[0],new_data[1],new_data[2]

        
        self.odom_gyro[3:6] += new_data[3:6] * self.imu_dt # around x y z angular
        # print(self.odom_gyro[3:6])
        # print(d[0])
        
        
        self.odom_acc[3] = numpy.arctan2(ay, az) # around x
        self.odom_acc[4] = numpy.arctan2(-ax, numpy.sqrt(ay**2 + az**2))  # around y
        self.odom_acc[3:5] = numpy.trunc(self.odom_acc[3:5] * 1000.0) / 1000.0

        
        # print(self.odom_acc[3:6])
        #now already get position like this:
        # from acc: 
        # _ _ _ roll pitch _
        # from gyro: 
        # _ _ _ roll pitch yaw 

    # generate a twist frame transformation without rotation from base frame
    def update_twist(self, msg: TwistStamped):
        # print("get twist")
        self.recent_twist = msg
        imu_fused = self.__get_imu_fusion()
                        
 
        # print(self.odom_gyro) 
        twist_t = self.stamp_to_sec(msg.header.stamp.sec, msg.header.stamp.nanosec)
        if self.first_call_twist_update:
            self.twist_previous_t = twist_t
            self.first_call_twist_update = False 
        self.twist_dt = twist_t - self.twist_previous_t
        self.twist_previous_t = twist_t 
        new_data = self.__twist_to_numpy(msg) 
        # print(new_data[0:3])
        v = new_data[0]
        omiga = new_data[5]

        self.odom_twist[5] += numpy.trunc(omiga * self.twist_dt * 100.0) / 100.0
        # print(self.odom_twist[5])
        # 
        # vx = numpy.cos(self.odom_twist[5]) * v
        # vy = numpy.sin(self.odom_twist[5]) * v   
        # linear_displacement = numpy.array([vx * self.twist_dt, vy * self.twist_dt, 0, 0, 0, 0])
        
        linear_displacement = numpy.zeros(6)
        if self.enable_3d:
            linear_displacement[0] = v * self.twist_dt
            rx = Rotation.from_euler('x', imu_fused[3])
            ry = Rotation.from_euler('y', imu_fused[4])
            rz = Rotation.from_euler('z', imu_fused[5])
            linear_displacement[0:3] = rx.apply(ry.apply(rz.apply(linear_displacement[0:3])))
        else:
            vx = numpy.cos(self.odom_twist[5]) * v
            vy = numpy.sin(self.odom_twist[5]) * v   
            linear_displacement = numpy.array([vx * self.twist_dt, vy * self.twist_dt, 0, 0, 0, 0])
        self.odom_twist += linear_displacement
        self.odom_twist[5] %= 2 * numpy.pi
        # print(new_data)
        # print(self.odom_twist[0:3])
        # print("===")

    def __get_imu_fusion(self):
        return  numpy.trunc((self.odom_acc * self.acc_trust + self.odom_gyro * self.gyro_trust) * 100.0) / 100.0
    

    def __get_odom_fusion(self, imu_fused): 
        output = numpy.zeros(6)
        twist_frame = self.odom_twist[0:3] 
        output[0:3] = twist_frame
        output[3:6] = imu_fused[3:6] 
        # if self.enable_3d and (self.recent_twist.twist.linear.x > yaw_fusion_min_velocity or self.recent_twist.twist.angular.z > yaw_fusion_min_angular_velocity):
        #     output[5] = output[5] * yaw_gyro_trust + self.odom_twist[5] * yaw_encoder_trust
        return numpy.trunc(output * 1000.0) / 1000.0


    def generate_odometry(self):
        message = Odometry()
        
        imu_fused = self.__get_imu_fusion() 
        # print(self.odom_twist)

        odom_fused = self.__get_odom_fusion(imu_fused) 
        # print(odom_fused)

        message.pose.pose.position.x = odom_fused[0] / 1000.0
        message.pose.pose.position.y = odom_fused[1] / 1000.0
        message.pose.pose.position.z = odom_fused[2] / 1000.0
        # print(odom_fused[0:2])

        q = tf_transformations.quaternion_from_euler(*odom_fused[3:6])
        message.pose.pose.orientation.x = q[0]
        message.pose.pose.orientation.y = q[1]
        message.pose.pose.orientation.z = q[2]
        message.pose.pose.orientation.w = q[3]

        message.twist.twist = self.recent_twist.twist
        message.twist.twist.linear.x /= 1000.0
        message.twist.twist.linear.y /= 1000.0
        message.twist.twist.linear.z /= 1000.0

        time_stamp = self.get_clock().now().to_msg()
        message.header.stamp = time_stamp
        message.header.frame_id = frame_id
        message.child_frame_id = child_frame_id

        self.odom_publisher.publish(message)

        euler_message = Vector3()
        euler_message.x = imu_fused[3]
        euler_message.y = imu_fused[4]
        euler_message.z = imu_fused[5]
        self.fused_euler_publisher.publish(euler_message)

        # self.get_logger().info(f'published odometry: {message}')


def main(args=None):
    rclpy.init(args=args)
    node = odometry_generator()
    try:  
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("shouting down")
    finally:
        node.destroy_node()
        rclpy.shutdown() 

if __name__ == '__main__':
    main()