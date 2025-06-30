from chassis_constants import *
from actuator_package.servo_group import *
from actuator_package.xl330_constant import *
from actuator_package.robot_constant import *

class chass_4wdiff:
    def __init__(self):
        port_init()
        port_open()
        self.wheel_group = servo_group(MODE_VELOCITY, [left_front_wheel_id,left_rear_wheel_id, right_front_wheel_id, right_rear_wheel_id])
        self.direction = [left_direction, left_direction, right_direction, right_direction]  # Direction for each wheel

    def wheel_zeroing(self):
        """
        Set all wheels to zero position
        """
        self.wheel_group.set_torque_status(TORQUE_DISABLE)
        self.wheel_group.set_mode(MODE_POSITION)
        self.wheel_group.set_torque_status(TORQUE_ENABLE)
        self.wheel_group.set_goals([0, 0, 0, 0])  # Set all wheels to zero position 
        time.sleep(1)
        self.wheel_group.set_torque_status(TORQUE_DISABLE)
        self.wheel_group.set_mode(MODE_VELOCITY)
        self.wheel_group.set_torque_status(TORQUE_ENABLE)
      # Allow time for the wheels to stop    

    def set_speed_4wdiff(self, speed_matrix: list[float]) -> int:
        if len(speed_matrix) != 2:
            raise ValueError("speed_matrix must be a list of two elements: [linear_speed, angular_speed]")
        angular_to_linear_velocity = speed_matrix[1] * rotation_radius
        left_speed = (speed_matrix[0] - angular_to_linear_velocity) * left_direction
        right_speed = (speed_matrix[0] + angular_to_linear_velocity) * right_direction 

        left_goal = int(left_speed / speed_unit)
        right_goal = int(right_speed / speed_unit)
        
        return self.wheel_group.set_goals([left_goal, left_goal, right_goal, right_goal]) 


    def read_feedback_4wdiff(self) -> dict:
        servo_data = self.wheel_group.get_feedback()
        for i in range(len(servo_data[FEEDBACK_VELOCITY_NAME])):
            servo_data[FEEDBACK_VELOCITY_NAME][i] = servo_data[FEEDBACK_VELOCITY_NAME][i] * self.direction[i]
            servo_data[FEEDBACK_POSITION_NAME][i] = servo_data[FEEDBACK_POSITION_NAME][i] * self.direction[i]
        return servo_data

    def enable_torque(self):
        return self.wheel_group.set_torque_status(TORQUE_ENABLE)

    def disable_torque(self):
        return self.wheel_group.set_torque_status(TORQUE_DISABLE)

    def chassis_port_close(self):
        port_close()

    def chassis_port_open(self):
        port_open()

