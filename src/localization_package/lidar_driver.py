from .robot_constant import *
from pyrplidar import *
class lidar_c1():
    def __init__(self, lidar_port: str = LIDAR_DEVICENAME, baudrate: int = LIDAR_BAUDRATE, time_out: int = 3):
        self.lidar = PyRPlidar()
        connected = self.lidar.connect(port=lidar_port, baudrate=baudrate, timeout=time_out)
        if connected:
            print("connected")
            print(self.lidar.get_info())
        else:
            print("fail")

    