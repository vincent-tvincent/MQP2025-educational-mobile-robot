from robot_constant import *
from xl330_constant import *
from dynamixel_sdk import *

portHandler = PortHandler(DEVICENAME)  
packetHandler = PacketHandler(PROTOCOL_VERSION)
current_mode = {}


def servo_init():
    portHandler.openPort()
    portHandler.setBaudRate(BAUDRATE)


def set_torque_enable(id:int):
    packetHandler.write1ByteTxRx(portHandler, id, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)


def set_torque_disable(id:int):
    packetHandler.write1ByteTxRx(portHandler, id, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)


def set_torque_status(id:int, status:int):
    packetHandler.write1ByteTxRx(portHandler, id, ADDR_TORQUE_ENABLE, status)


def set_mode(id:int, mode:int):
    original_torque_status,read_result,read_error=packetHandler.read1ByteTxRx(portHandler, id, ADDR_TORQUE_ENABLE)

    if original_torque_status == TORQUE_ENABLE:
        set_torque_disable(id)

    write_result,write_error = packetHandler.write1ByteTxRx(portHandler, id, ADDR_OPERATING_MODE, mode)  
    if write_result == COMM_SUCCESS:
        current_mode[id] = mode

    if original_torque_status == TORQUE_ENABLE:
        set_torque_enable(id)
        

def set_mode_position(id:int):
    set_mode(id, MODE_POSITION)


def set_mode_extended_position(id:int):
    set_mode(id, MODE_EXTENDED_POSITION)


def set_mode_velocity(id:int):
    set_mode(id, MODE_VELOCITY)


def set_mode_pwm(id:int):
    set_mode(id, MODE_PWM)


def set_value(id:int, value:int):
    addr_goal = ADDR_GOAL_POSITION
    if current_mode[id] == MODE_POSITION:
        addr_goal = ADDR_GOAL_POSITION

    elif current_mode[id] == MODE_VELOCITY:
        addr_goal = ADDR_GOAL_VELOCITY

    elif current_mode[id] == MODE_PWM:
        addr_goal = ADDR_GOAL_PWM
    result,error = packetHandler.write4ByteTxRx(portHandler, id, addr_goal, value)


servo_init()

set_torque_enable(0)
set_torque_enable(1)
set_mode_velocity(0)
set_mode_velocity(1)
set_value(0, 0)
set_value(1, 0)