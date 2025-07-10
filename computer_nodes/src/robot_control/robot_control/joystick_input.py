from pydualsense import pydualsense

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy, Imu

import numpy


node_name = 'ps5_controller_node'

controller_topic_name = 'robot_controller'
controller_imu_topic_name = 'robot_controller_imu'

joystick_publish_interval = 1 / 400
queue_size = 200

enable_imu = False

joystick_deadzone = 10
joystick_max = 120
joystick_range = joystick_max - joystick_deadzone

trigger_deadzone = 0
trigger_max = 255
trigger_range = trigger_max - trigger_deadzone


'''
assignments: 
axes: 
lx ly l_trigger rx ry r_tirgger

buttons:
l1 r1 l_stick r_stick down left up right cross square triangle circle

imu (if switch to enable)
align with ros default directions
ax ay az gx gy gz
'''
class joystick_input(Node):
    def __init__(self):
        super().__init__(node_name)
        self.axes = numpy.zeros(6)
        self.buttons = numpy.zeros(12)
        self.imu = numpy.zeros(6)

        self.controller = pydualsense()
        self.controller.init()

        # linear input 
        self.controller.left_joystick_changed += self.__update_left_joystick        
        self.controller.right_joystick_changed += self.__update_right_joystick
        self.controller.l2_value_changed += self.__update_left_trigger
        self.controller.r2_value_changed += self.__update_right_trigger
        if enable_imu:
            self.controller.gyro_changed += self.__update_gyro
            self.controller.accelerometer_changed += self.__update_acceleration

        # binary input
        self.controller.l1_changed += self.__update_left_shoulder_button
        self.controller.r1_changed += self.__update_right_shoulder_button
        self.controller.l3_changed += self.__update_left_joystick_button
        self.controller.r3_changed += self.__update_right_joystick_button
        self.controller.dpad_down += self.__update_dpad_down
        self.controller.dpad_left += self.__update_dpad_left
        self.controller.dpad_up += self.__update_dpad_up
        self.controller.dpad_right += self.__update_dpad_right
        self.controller.cross_pressed += self.__update_cross
        self.controller.square_pressed += self.__update_square
        self.controller.triangle_pressed += self.__update_triangle
        self.controller.circle_pressed += self.__update_circle

        self.joystick_publisher = self.create_publisher(
            Joy,
            controller_topic_name,
            queue_size
        )


        self.joystick_imu_publisher = self.create_publisher(
            Imu,
            controller_imu_topic_name,
            queue_size
        )


        self.controller_publish_timer = self.create_timer(
            joystick_publish_interval,
            self.publish_joystick_input
        )


    def publish_joystick_input(self):
        message = Joy()
        message.axes = self.axes
        message.buttons = [int(v) for v in self.buttons]
        # print(message)
        self.joystick_publisher.publish(message) 
        if enable_imu:
            imu_message = Imu() 
            imu_message.header.stamp = self.get_clock().now().to_msg()
            imu_message.linear_acceleration.x = self.imu[0]
            imu_message.linear_acceleration.y = self.imu[1]
            imu_message.linear_acceleration.z = self.imu[2]
            imu_message.angular_velocity.x = self.imu[3]
            imu_message.angular_velocity.y = self.imu[4]
            imu_message.angular_velocity.z = self.imu[5]


    def __joysticks_to_percentage(self, raw) -> float:
        if abs(raw) < joystick_deadzone:
            return 0.0
        else:
            output = numpy.trunc((raw - joystick_deadzone * raw / abs(raw)) / joystick_range * 100) / 100
            if abs(output) > 1.0:
                return 1.0 * abs(output) / output
            else:
                return output
            

    def __trigger_to_percentage(self, raw) -> float:
        return (raw - trigger_deadzone) / trigger_range

    def __update_left_joystick(self,x,y):
        self.axes[0] = self.__joysticks_to_percentage(x)
        self.axes[1] = self.__joysticks_to_percentage(y)


    def __update_right_joystick(self,x,y): 
        self.axes[3] = self.__joysticks_to_percentage(x) 
        self.axes[4] = self.__joysticks_to_percentage(y) 


    def __update_gyro(self,y, z, x):
        self.imu[3] = x
        self.imu[4] = y
        self.imu[5] = z


    def __update_acceleration(self,y, z, x):
        self.imu[0] = x
        self.imu[1] = y
        self.imu[2] = z


    def __update_left_trigger(self, v):
        self.axes[2] = self.__trigger_to_percentage(v)


    def __update_right_trigger(self, v):
        self.axes[5] = self.__trigger_to_percentage(v)


    def __update_left_shoulder_button(self, s):
        self.buttons[0] = s 


    def __update_right_shoulder_button(self, s):
        self.buttons[1] = s


    def __update_left_joystick_button(self, s):
        self.buttons[2] = s 


    def __update_right_joystick_button(self, s):
        self.buttons[3] = s


    def __update_dpad_down(self, s):
        self.buttons[4] = s


    def __update_dpad_left(self, s):
        self.buttons[5] = s


    def __update_dpad_up(self, s):
        self.buttons[6] = s


    def __update_dpad_right(self, s):
        self.buttons[7] = s


    def __update_cross(self, s):
        self.buttons[8] = s


    def __update_square(self, s):
        self.buttons[9] = s


    def __update_triangle(self, s):
        self.buttons[10] = s


    def __update_circle(self, s):
        self.buttons[11] = s


    def close_joystick(self):
        self.controller.close()


def main(args=None): 
    rclpy.init(args=args)
    node = joystick_input()
    try:  
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("shouting down")
        node.close_joystick()
    finally:
        node.destroy_node() 


if __name__ == '__main__':
    main()