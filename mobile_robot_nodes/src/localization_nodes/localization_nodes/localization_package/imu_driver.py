from .robot_constant import *
from qwiic_icm20948 import *

import time
import sys
import numpy
import math
# def runExample():

# 	print("\nSparkFun 9DoF ICM-20948 Sensor  Example 1\n")
# 	IMU = qwiic_icm20948.QwiicIcm20948()

# 	if IMU.connected == False:
# 		print("The Qwiic ICM20948 device isn't connected to the system. Please check your connection", \
# 			file=sys.stderr)
# 		return

# 	IMU.begin()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
	# while True:
	# 	if IMU.dataReady():
	# 		IMU.getAgmt() # read all axis and temp from sensor, note this also updates all instance variables
	# 		print(\
	# 		 'ax: {: 06d}'.format(IMU.axRaw)\
	# 		, '\t', 'ay: {: 06d}'.format(IMU.ayRaw)\
	# 		, '\t', 'az: {: 06d}'.format(IMU.azRaw)\
	# 		, '\t', 'gx: {: 06d}'.format(IMU.gxRaw)\
	# 		, '\t', 'gy: {: 06d}'.format(IMU.gyRaw)\
	# 		, '\t', 'gz: {: 06d}'.format(IMU.gzRaw)\
	# 		, '\t', 'mx: {: 06d}'.format(IMU.mxRaw)\
	# 		, '\t', 'my: {: 06d}'.format(IMU.myRaw)\
	# 		, '\t', 'mz: {: 06d}'.format(IMU.mzRaw)\
	# 		)
	# 		time.sleep(0.03)
	# 	else:
	# 		print("Waiting for data")
	# 		time.sleep(0.5)
imu_caliberation_samples = 1000
imu_caliberation_repeat_times = 2
imu_gravity = 16384
imu_gyro_one_degree = 131
imu_acc_lsb_max = imu_gravity * 2

imu_g = 9806.65 # mm/s^2
imu_acc_unit = imu_g / imu_gravity

imu_gyro_unit_degree = 1 / imu_gyro_one_degree # degree/s 
imu_gyro_unit_radian = imu_gyro_unit_degree * math.pi / 180

class imu_icm20948_qwiic():
    def __init__(self): 
        self.imu = QwiicIcm20948()
        self.ax_b, self.ay_b, self.az_b, self.gx_b, self.gy_b, self.gz_b, self.mx_b, self.my_b, self.mz_b = 0,0,0,0,0,0,0,0,0
        self.imu_lowpass_samples = 1
        if self.imu.connected:
            self.imu.begin()
            self.imu.enableDlpfAccel(True)
            self.imu.enableDlpfGyro(True)
            self.imu.getAgmt()
        else:
            raise ConnectionError("imu fail to connect")
        self.imu_generator = self.__create_imu_generator()

    def update_imu(self):
        if self.imu.dataReady():
            self.imu.getAgmt() 
        return self.imu.dataReady()


    def read_raw_imu(self) -> dict:
        output = {}
        if IMU_ACCELERATION_ENABLE:
            output[IMU_ACCELERATION_NAME] = numpy.array([self.imu.axRaw - self.ax_b, self.imu.ayRaw - self.ay_b, self.imu.azRaw - self.az_b])
        if IMU_GYROSCOPE_ENABLE:
            output[IMU_GYROSCOPE_NAME] = numpy.array([self.imu.gxRaw - self.gx_b, self.imu.gyRaw - self.gy_b, self.imu.gzRaw - self.gz_b])
        if IMU_MEGNETIC_ENABLE:
            output[IMU_MEGNETIC_NAME] = numpy.array([self.imu.mxRaw - self.mx_b, self.imu.myRaw - self.my_b, self.imu.mzRaw - self.mz_b])
        return output


    def __create_imu_generator(self):
        def imu_generator():
            while True:
                output_a = numpy.zeros(3)
                output_g = numpy.zeros(3)
                output_m = numpy.zeros(3)
                output = {IMU_ACCELERATION_NAME: output_a, IMU_GYROSCOPE_NAME: output_g, IMU_MEGNETIC_NAME: output_m}
                for i in range(self.imu_lowpass_samples):
                    while not self.update_imu():
                        pass        
                    new_read_value = self.read_raw_imu()
                    for key in output.keys():
                        output[key] += new_read_value[key]
                for key in output.keys():
                        output[key] /= self.imu_lowpass_samples
                yield output
        return imu_generator


    def read_imu(self):
        return self.imu_generator().__next__()
                   
        
    def __single_caliberation(self): 
        print("imu caliberating")
        gx, gy, gz, ax, ay, az = 0, 0, 0, 0, 0, 0
        self.imu.getAgmt()
        for i in range(imu_caliberation_samples):
            while not self.update_imu():
                pass
            raw_data = self.read_raw_imu()
            ax += raw_data[IMU_ACCELERATION_NAME][0]
            ay += raw_data[IMU_ACCELERATION_NAME][1]
            az += raw_data[IMU_ACCELERATION_NAME][2] + imu_gravity 

            gx += raw_data[IMU_GYROSCOPE_NAME][0]
            gy += raw_data[IMU_GYROSCOPE_NAME][1]
            gz += raw_data[IMU_GYROSCOPE_NAME][2]


        gx //= imu_caliberation_samples
        gy //= imu_caliberation_samples
        gz //= imu_caliberation_samples

        ax //= imu_caliberation_samples
        ay //= imu_caliberation_samples
        az //= imu_caliberation_samples
 
        self.gx_b += gx
        self.gy_b += gy
        self.gz_b += gz
        self.ax_b += ax
        self.ay_b += ay
        self.az_b += az
        print("imu caliberation complete")
    

    def caliberation(self):
        for i in range(imu_caliberation_repeat_times):
            print("caliberation " + str(i))
            self.__single_caliberation()


    def set_lowpass_samples(self, samples: int):
        self.imu_lowpass_samples = samples 
        
            

        
         
     
        
        
        
         
    
    
# if __name__ == '__main__':
# 	try:
# 		runExample()
# 	except (KeyboardInterrupt, SystemExit) as exErr:
# 		print("\nEnding Example 1")
# 		sys.exit(0)