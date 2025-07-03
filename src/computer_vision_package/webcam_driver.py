from .robot_constant import *
import cv2
import numpy
import time

class webcam_ub0240():
    def __init__(self):
        self.camera = cv2.VideoCapture(CAMERA_DEVICE_INDEX)
        self.camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_FRAME_WIDTH)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_FRAME_HEIGHT)
        self.fov = CAMERA_FOV
        self.image_generator = self.__create_image_generator()
    
    
    def capture_single_image(self) -> tuple[bool, numpy.ndarray]:
        return self.camera.read()

    
    def __create_image_generator(self):
        def image_generator() -> numpy.ndarray:
            while True:
                ok, frame = self.capture_single_image()
                if not ok:
                    continue
                yield frame 
        return image_generator() 


    def capture_mutable_image(self, image_amount: int, interval: int = 0) -> list[numpy.ndarray]:
        output = []
        for i in range(image_amount):
            output.append(self.image_generator.__next__())
            time.sleep(interval)
        return output 

    def close_camera():
        self.camera.release()
    
        