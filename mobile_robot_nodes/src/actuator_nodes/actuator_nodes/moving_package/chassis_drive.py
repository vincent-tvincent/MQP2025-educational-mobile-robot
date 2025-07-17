from .actuator_package.servo_group import *
from .actuator_package.xl330_constant import *
from .actuator_package.robot_constant import *
import math

# ids 
left_front_wheel_id = 4
right_front_wheel_id = 5
left_rear_wheel_id = 2
right_rear_wheel_id = 3

# units: mm
chassis_width = 118.5
wheel_thinkness = 12
wheel_diameter = 56
m288_servo_max_rpm = 123
m288_speed_unit = 0.229  # rpm per unit 
left_direction = 1
right_direction = -1

wheel_radius = wheel_diameter / 2
rotation_diameter = chassis_width - wheel_thinkness  # mm
rotation_radius = rotation_diameter / 2
max_wheel_speed = m288_servo_max_rpm * wheel_radius * 2 * math.pi / 60  # mm/s
speed_unit = m288_speed_unit * wheel_radius * 2 * math.pi / 60  # mm/s per unit

class chassis_4wdiff:
    def __init__(self, portHandler: PortHandler):
        self.wheel_group = servo_group(MODE_VELOCITY, portHandler, [left_front_wheel_id,left_rear_wheel_id, right_front_wheel_id, right_rear_wheel_id])
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

        left_goal = int(left_speed / speed_unit) / wheel_radius
        right_goal = int(right_speed / speed_unit) / wheel_radius
        return self.wheel_group.set_goals([left_goal, left_goal, right_goal, right_goal]) 

    def caliberation():
        pass

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
 

