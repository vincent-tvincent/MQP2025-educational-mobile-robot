from .robot_constant import *
from pyrplidar import PyRPlidar
from pyrplidar_protocol import PyRPlidarMeasurement
import time
class lidar_c1():
    def __init__(self, lidar_port: str = LIDAR_DEVICENAME, baudrate: int = LIDAR_BAUDRATE, time_out: int = 10): 
        self.lidar = PyRPlidar()
        self.lidar.connect(port=lidar_port, baudrate=baudrate, timeout=time_out) 


    def start_scan(self):
        self.lidar_generator = self.lidar.start_scan()


    def stop_scan(self):
        self.lidar.stop()


    def get_single_scan(self) -> tuple[float, dict]:
        next_scan = self.lidar_generator().__next__()
        return self.__process_single_scan(next_scan)

    
    def __process_single_scan(self, raw: PyRPlidarMeasurement) -> tuple[float, dict]:
        value = {}
        if LIDAR_DISTANCE_ENABLE:
            value[LIDAR_DISTANCE_NAME] = raw.distance
        if LIDAR_QUALITY_ENABLE: 
            value[LIDAR_QUALITY_NAME] = raw.quality
        if LIDAR_START_FLAG_ENABLE:
            value[LIDAR_START_FLAG_NAME] = raw.start_flag
        return raw.angle, value

        
    def scan_around(self) -> dict:
        scans = {} 
        for i in range(LIDAR_SAMPLE_PER_CIRCLE):
            angle, value = self.get_single_scan()
            scans[angle] = value
        return scans


                
            
            
        
        
        
        


    
     
    


    