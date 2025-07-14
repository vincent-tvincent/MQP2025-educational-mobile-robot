from collections import deque
import numpy

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Imu
from std_msgs.msg import Int32



node_name = "imu_processing"
imu_feedback_publish_topic_name =  'feedback_imu'
imu_lowpass_samples_topic_name = 'set_lowpass_samples_imu'
imu_test_plot_topic_name = 'test_plot_imu'

odometry_generator_topic_name = 'odom_in_imu'

imu_frame_id = 'imu_link'

queue_size = 200

imu_g = 9806.65 # mm/s^2
data_buffer_size = 50
lpf_alpha = 0.5

class imu_processing_node(Node):
    def __init__(self):
        super().__init__(node_name)

        #prepare for higher order filtering implementation 
        self.imu_data_buffer = deque()
        self.caliberated = False
        self.bias = numpy.zeros(6)

        self.imu_subscriber = self.create_subscription(
            Imu,
            imu_feedback_publish_topic_name,
            self.handle_imu_data,
            queue_size  
        )

        self.lowpass_publisher = self.create_publisher(
            Int32,
            imu_lowpass_samples_topic_name,
            queue_size 
        )

        self.test_publisher = self.create_publisher(
            Imu,
            imu_test_plot_topic_name,
            queue_size 
        )

        self.odom_publisher = self.create_publisher(
            Imu,
            odometry_generator_topic_name,
            queue_size
        )

         


    def __message_to_numpy(self, msg: Imu):
        output = numpy.zeros(6)
        output[0] = msg.linear_acceleration.x
        output[1] = msg.linear_acceleration.y
        output[2] = msg.linear_acceleration.z
        output[3] = msg.angular_velocity.x
        output[4] = msg.angular_velocity.y
        output[5] = msg.angular_velocity.z
        return output

    def __numpy_to_message(self, value: numpy.ndarray):
        message = Imu()
        message.linear_acceleration.x = value[0]
        message.linear_acceleration.y = value[1]
        message.linear_acceleration.z = value[2]
        message.angular_velocity.x = value[3]
        message.angular_velocity.y = value[4]
        message.angular_velocity.z = value[5]
        return message


    def __imu_enqueue(self, msg: Imu):
        if len(self.imu_data_buffer) >= data_buffer_size:
            self.imu_data_buffer.popleft()  
        recent_data =  self.__message_to_numpy(msg)
        if len(self.imu_data_buffer) > 1:  
            previous_data = self.imu_data_buffer[len(self.imu_data_buffer) - 1]  
            recent_data[0:3] = previous_data[0:3] * (1 - lpf_alpha) + recent_data[0:3] * lpf_alpha 
            recent_data[3:6] = numpy.trunc(recent_data[3:6] * 100) / 100
            # print(recent_data[0:3])
        self.imu_data_buffer.append(recent_data)

    def handle_imu_data(self, msg: Imu):
        self.__imu_enqueue(msg) 
        to_localization = self.__numpy_to_message(self.imu_data_buffer[len(self.imu_data_buffer) - 1])
        to_localization.header = msg.header
        to_localization.header.frame_id = imu_frame_id
        
        self.odom_publisher.publish(to_localization)
          

    def set_lowpass_samples(self, samples: int):
        message = Int32()
        message.data = samples
        self.lowpass_publisher.publish(message)


def main(args=None):
    rclpy.init(args=args)
    node = imu_processing_node()
    try:  
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("shouting down")
    finally:
        node.destroy_node() 


if __name__ == '__main__':
    main()