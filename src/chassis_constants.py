import math
# ids 
left_front_wheel_id = 4
right_front_wheel_id = 5
left_rear_wheel_id = 2
right_rear_wheel_id = 3

# units: mm
chassis_width = 118.5
wheel_thinkness = 12
wheel_diameter = 56.5
m288_servo_max_rpm = 123
m288_speed_unit = 0.229  # rpm per unit 
left_direction = 1
right_direction = -1

wheel_radius = wheel_diameter / 2
rotation_diameter = chassis_width - wheel_thinkness  # mm
rotation_radius = rotation_diameter / 2
max_wheel_speed = m288_servo_max_rpm * wheel_radius * 2 * math.pi / 60  # mm/s
speed_unit = m288_speed_unit * wheel_radius * 2 * math.pi / 60  # mm/s per unit


