
from .dynamixel_sdk import PortHandler
from .robot_constant import DEVICENAME


def port_init(device_name:str = DEVICENAME, budrate: int = 115200) -> PortHandler:
    portHandler = PortHandler(device_name)
    print('initializing communication')
    port_open = portHandler.openPort()
    if port_open:
        print('port opened, device name: ' + portHandler.getPortName())
        baudrate_avaliable = portHandler.setBaudRate(budrate)
        if baudrate_avaliable != -1:
            print('baudrate setted, value: ' + str(portHandler.getBaudRate()))
    
    portHandler.clearPort()
    return portHandler


def port_close(portHandler: PortHandler):
    print('closing port')
    port_open = portHandler.closePort()
    if not port_open:
        print('port closed')
    return port_open

def port_open(portHandler: PortHandler):
    print('opening port')
    port_open = portHandler.openPort()
    if port_open:
        print('port opened')
    return port_open