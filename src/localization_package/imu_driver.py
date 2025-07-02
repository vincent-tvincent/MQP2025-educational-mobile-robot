from .robot_constant import *
from qwiic_icm20948 import *
import time
import sys


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
imu_caliberation_repeat_times = 5
gravity = 16384
class imu_icm20948_qwiic():
    def __init__(self): 
        self.imu = QwiicIcm20948()
        self.ax_b, self.ay_b, self.az_b, self.gx_b, self.gy_b, self.gz_b, self.mx_b, self.my_b, self.mz_b = 0,0,0,0,0,0,0,0,0
        if self.imu.connected:
            self.imu.begin()
        else:
            raise ConnectionError("imu fail to connect")


    def update_imu(self):
        if self.imu.dataReady():
            self.imu.getAgmt() 
        return self.imu.dataReady()


    def read_imu(self) -> dict:
        output = {}
        if IMU_ACCELERATION_ENABLE:
            output[IMU_ACCELERATION_NAME] = [self.imu.axRaw - self.ax_b, self.imu.ayRaw - self.ay_b, self.imu.azRaw - self.az_b]
        if IMU_GYROSCOPE_ENABLE:
            output[IMU_GYROSCOPE_NAME] = [self.imu.gxRaw - self.gx_b, self.imu.gyRaw - self.gy_b, self.imu.gzRaw - self.gz_b]
        if IMU_MEGNETIC_ENABLE:
            output[IMU_MEGNETIC_NAME] = [self.imu.axRaw - self.mx_b, self.imu.ayRaw - self.my_b, self.imu.azRaw - self.mz_b]
        return output

    def __single_caliberation(self): 
        print("imu caliberating")
        gx, gy, gz, ax, ay, az = 0, 0, 0, 0, 0, 0
        self.update_imu()
        for i in range(imu_caliberation_samples):
            while not self.update_imu():
                pass
            raw_data = self.read_imu()
            ax += raw_data[IMU_ACCELERATION_NAME][0]
            ay += raw_data[IMU_ACCELERATION_NAME][1]
            az += raw_data[IMU_ACCELERATION_NAME][2] + gravity 

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
        print(self.az_b)
        print("imu caliberationg complete")
    
    def caliberation(self):
        for i in range(imu_caliberation_repeat_times):
            print("caliberation " + str(i))
            self.__single_caliberation()

         
        
            

        
         
     
        
        
        
         
    
    
# if __name__ == '__main__':
# 	try:
# 		runExample()
# 	except (KeyboardInterrupt, SystemExit) as exErr:
# 		print("\nEnding Example 1")
# 		sys.exit(0)