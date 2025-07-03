from .robot_constant import *
from .xl330_constant import *
from .dynamixel_sdk import *
portHandler = PortHandler(DEVICENAME)  
packetHandler = PacketHandler(PROTOCOL_VERSION)
recent_mode = {}
def port_init():
    print('initializing communication')
    port_open = portHandler.openPort()
    if port_open:
        print('port opened, device name: ' + portHandler.getPortName())
        baudrate_avaliable = portHandler.setBaudRate(BAUDRATE)
        if baudrate_avaliable != -1:
            print('baudrate setted, value: ' + str(portHandler.getBaudRate()))


def port_close():
    print('closing port')
    port_open = portHandler.closePort()
    if not port_open:
        print('port closed')


def port_open():
    print('opening port')
    port_open = portHandler.openPort()
    if port_open:
        print('port opened')


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
        recent_mode[id] = mode

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


def set_goal(id:int, value:int):
    addr_goal = ADDR_GOAL_POSITION
    if recent_mode[id] == MODE_POSITION:
        addr_goal = ADDR_GOAL_POSITION

    elif recent_mode[id] == MODE_VELOCITY:
        addr_goal = ADDR_GOAL_VELOCITY

    elif recent_mode[id] == MODE_PWM:
        addr_goal = ADDR_GOAL_PWM
    result,error = packetHandler.write4ByteTxRx(portHandler, id, addr_goal, value)

