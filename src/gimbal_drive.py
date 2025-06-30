from actuator_package.servo_group import *
from actuator_package.xl330_constant import *
from actuator_package.robot_constant import *
import math

#ids 
gimbal_yaw_id = 1
gimbal_pitch_id = 0 

gimbal_zero = POSITION_MAX / 2
gimbal_step = math.pi / POSITION_MAX # 1 step = 360 / 4096 degrees


class gimbal_yaw_pitch:

    def __init__(self, portHandler: PortHandler):
        port_init()
        port_open()
        self.gimbal_group = servo_group(MODE_POSITION, portHandler,[gimbal_yaw_id, gimbal_pitch_id])
        

    def gimbal_zeroing(self):
        self.gimbal_group.set_torque_status(TORQUE_ENABLE)
        self.gimbal_group.set_goals([int(gimbal_zero), int(gimbal_zero)])  # Set initial position to zero

    def set_gimbal_position(self, position_matrix: list[float]) -> int:
        if len(position_matrix) != 2:
            raise ValueError("position_matrix must be a list of two elements: [yaw_position, pitch_position]")
        yaw_position = int(gimbal_zero + position_matrix[0] / gimbal_step) 
        pitch_position = int(gimbal_zero + position_matrix[1] / gimbal_step)
        return self.gimbal_group.set_goals(yaw_positon, pitch_position)

    def read_feedback_gimbal(self) -> dict:
        return self.gimbal_group.get_feedback()

    def gimbal_port_close(self):
        port_close()

    def enable_torque(self):
        return self.gimbal_group.set_torque_status(TORQUE_ENABLE)

    def disable_torque(self):
        return self.gimbal_group.set_torque_status(TORQUE_DISABLE)