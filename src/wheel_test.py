# from  actuator_package.servo_group import port_init, port_open, port_close
from chassis_drive import *

chassis = chass_4wdiff()
# chassis.wheel_zeroing()
chassis.enable_torque()
print(chassis.read_feedback_4wdiff())
time.sleep(1)
print(chassis.set_speed_4wdiff([0, 0.25 * math.pi]))  # Set linear speed to 100 mm/s and angular speed to 0 rad/s
print(chassis.read_feedback_4wdiff())

for i in range(20):
    print(chassis.read_feedback_4wdiff())
    time.sleep(0.1)

print(chassis.set_speed_4wdiff([0, 0]))  # Set linear speed to 0 mm/s and angular speed to 1 rad/s
chassis.disable_torque()
port_close()

