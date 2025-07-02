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


    def scan_around(self) -> dict:
        scans = {} 
        for i in range(LIDAR_SAMPLE_PER_CIRCLE):
            next_scan = self.lidar_generator().__next__()
            value = {}
            if LIDAR_DISTANCE_ENABLE:
                value[LIDAR_DISTANCE_NAME] = next_scan.distance
            if LIDAR_QUALITY_ENABLE: 
                value[LIDAR_QUALITY_NAME] = next_scan.quality
            if LIDAR_START_FLAG_ENABLE:
                value[LIDAR_START_FLAG_NAME] = next_scan.start_flag
            scans[next_scan.angle] = value
        return scans


                
            
            
        
        
        
        


    
     
    


    