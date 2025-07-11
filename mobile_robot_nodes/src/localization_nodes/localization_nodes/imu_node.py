from .localization_package.imu_driver import *
from .localization_package.robot_constant import *
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Imu
from std_msgs.msg import Int32

node_name = 'robot_imu'
imu_feedback_publish_topic_name =  'feedback_imu'
imu_lowpass_samples_topic_name = 'set_lowpass_samples_imu'
imu_publish_interval = 1 / 1000
queue_size = 50

class imu_node(Node):
    def __init__(self):
        super().__init__(node_name)
        self.frame_id = 0
        self.imu = imu_icm20948_qwiic()
        self.imu.caliberation()
        self.imu.set_lowpass_samples(int(1125 * imu_publish_interval))
        self.imu_subscriber = self.create_subscription(
            Int32,
            imu_lowpass_samples_topic_name,
            self.set_lowpass_samples,
            queue_size
        )

        self.imu_publisher = self.create_publisher(
            Imu,
            imu_feedback_publish_topic_name,
            queue_size
        ) 

        self.imu_publish_timer = self.create_timer(
            imu_publish_interval,
            self.send_feedback
        )
        
    def set_lowpass_samples(self, msg: Int32):
        self.imu.set_lowpass_samples(msg.data)

    def send_feedback(self):
        data = self.imu.read_imu()
        message = Imu()
        
        for key in data.keys():
            # x and y swapped for align with the direction of ros2 system 
            if key == IMU_ACCELERATION_NAME:
                message.linear_acceleration.x = data[IMU_ACCELERATION_NAME][1] * imu_acc_unit
                message.linear_acceleration.y = - data[IMU_ACCELERATION_NAME][0] * imu_acc_unit
                message.linear_acceleration.z = - data[IMU_ACCELERATION_NAME][2] * imu_acc_unit
            elif key == IMU_GYROSCOPE_NAME:
                message.angular_velocity.x = data[IMU_GYROSCOPE_NAME][1] * imu_gyro_unit_radian
                message.angular_velocity.y = - data[IMU_GYROSCOPE_NAME][0] * imu_gyro_unit_radian
                message.angular_velocity.z = data[IMU_GYROSCOPE_NAME][2] * imu_gyro_unit_radian 
                
        message.header.frame_id = 'robot'
        message.header.stamp = self.get_clock().now().to_msg()
        self.frame_id += 1
        # self.get_logger().info(f'{message.header.frame_id} , {message.angular_velocity.y}')
        self.imu_publisher.publish(message)


def main(args=None):
    rclpy.init(args=args)
    node = imu_node()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("shouting down")
        print(node.frame_id)
    finally:
        node.destroy_node()
     

if __name__ == '__main__':
    main()