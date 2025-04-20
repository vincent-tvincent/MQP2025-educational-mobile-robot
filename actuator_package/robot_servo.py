from robot_constant import *
from xl330_constant import *
from dynamixel_sdk import *

DEVICENAME = '/dev/cu.usbserial-FT9BTHA3'
BAUDRATE = 115200

portHandler = PortHandler(DEVICENAME)  
packetHandler = PacketHandler(PROTOCOL_VERSION)
current_mode = {}


def port_init():
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


def set_goal(id:int, value:int):
    addr_goal = ADDR_GOAL_POSITION
    if current_mode[id] == MODE_POSITION:
        addr_goal = ADDR_GOAL_POSITION

    elif current_mode[id] == MODE_VELOCITY:
        addr_goal = ADDR_GOAL_VELOCITY

    elif current_mode[id] == MODE_PWM:
        addr_goal = ADDR_GOAL_PWM
    result,error = packetHandler.write4ByteTxRx(portHandler, id, addr_goal, value)




class servo_group():


    def __init__(self,mode:int, id_list:list[int]):
        self.mode = mode
        self.id_list = id
        
        if mode == MODE_POSITION:
            self.addr_goal = ADDR_GOAL_POSITION
            self.size_goal = SIZE_GOAL_POSITION
        elif mode == MODE_EXTENDED_POSITION:
            self.addr_goal = ADDR_GOAL_POSITION
            self.size_goal = SIZE_GOAL_POSITION
        elif mode == MODE_VELOCITY:
            self.addr_goal = ADDR_GOAL_VELOCITY
            self.size_goal = SIZE_GOAL_VELOCITY
        elif mode == MODE_PWM:
            self.addr_goal = ADDR_GOAL_PWM            
            self.size_goal = SIZE_GOAL_PWM

        self.mode_writer = GroupSyncWrite(portHandler, ADDR_OPERATING_MODE, SIZE_OPERATING_MODE)
        self.torque_writer = GroupSyncWrite(portHandler, ADDR_TORQUE_ENABLE, SIZE_TORQUE_ENABLE)
        self.goal_writer = GroupSyncWrite(portHandler, self.addr_goal,self.size_goal)

        self.mode_reader = GroupSyncRead(portHandler, ADDR_OPERATING_MODE, SIZE_OPERATING_MODE)
        self.torque_reader = GroupSyncRead(portHandler, ADDR_TORQUE_ENABLE, SIZE_TORQUE_ENABLE)

        for id in self.id_list:
            self.mode_writer.addParam(id, mode)  
            self.torque_writer.addParam(id, TORQUE_DISABLE)
            self.goal_writer.addParam(id, 0)

        torque_result, torque_error = self.torque_writer.txPacket()
        if torque_result == COMM_SUCCESS:
            mode_result, mode_error = self.mode_writer.txPacket()  
            for id in self.id_list:
                current_mode[id] = mode


    def set_torque_status(self, status:int):
        for id in self.id_list:
            self.mode_writer.addParam(id, self.mode)  
            self.torque_writer.addParam(id, status)
        torque_result, torque_error = self.torque_writer.txPacket()


    def set_goals(self, values:int):
        for i in range(len(self.id_list)):
            self.goal_writer.changeParam(self.id_list[id], values[i])
        goal_result, goal_error = self.goal_writer.txPacket() 


    def set_mode(self, mode:int):
        self.mode = mode
        if mode == MODE_POSITION:
            self.addr_goal = ADDR_GOAL_POSITION
            self.size_goal = SIZE_GOAL_POSITION
        elif mode == MODE_EXTENDED_POSITION:
            self.addr_goal = ADDR_GOAL_POSITION
            self.size_goal = SIZE_GOAL_POSITION
        elif mode == MODE_VELOCITY:
            self.addr_goal = ADDR_GOAL_VELOCITY
            self.size_goal = SIZE_GOAL_VELOCITY
        elif mode == MODE_PWM:
            self.addr_goal = ADDR_GOAL_PWM            
            self.size_goal = SIZE_GOAL_PWM
        
        for id in self.id_list:
            self.mode_writer.changeParam(id,mode)
        
        self.set_torque_status(TORQUE_DISABLE)
        mode_result, mode_error = self.mode_writer.txPacket()
    
    

        
        
           
port_init()

set_torque_enable(0)
set_torque_enable(1)
set_mode_velocity(0)
set_mode_velocity(1)
set_goal(0, 0)
set_goal(1, 0)