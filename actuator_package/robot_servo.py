from robot_constant import *
from xl330_constant import *
from dynamixel_sdk import *


portHandler = PortHandler(DEVICENAME)  
packetHandler = PacketHandler(PROTOCOL_VERSION)
current_mode = {}
port_open = False


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


def wrap_1_byte(value: int):
        return [value]


def wrap_2_byte(value: int):
    return [DXL_LOBYTE(value), DXL_HIBYTE(value)]


def wrap_4_byte(value: int):
    return [DXL_LOBYTE(DXL_LOWORD(value)), DXL_HIBYTE(DXL_LOWORD(value)), DXL_LOBYTE(DXL_HIWORD(value)), DXL_HIBYTE(DXL_HIWORD(value))]

def wrap_byte(value: int, size: int):
    if size == 1: 
        return wrap_1_byte(value)
    if size == 2:
        return wrap_2_byte(value)
    if size == 4:
        return wrap_4_byte(value)
class servo_group():


    def __init__(self,mode:int, id_list:list[int]):
        self.mode = mode
        self.id_list = id_list
        self.feedback_data = {}
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

        self.mode_writer = GroupSyncWrite(portHandler, packetHandler, ADDR_OPERATING_MODE, SIZE_OPERATING_MODE)
        self.torque_writer = GroupSyncWrite(portHandler, packetHandler, ADDR_TORQUE_ENABLE, SIZE_TORQUE_ENABLE)
        self.goal_writer = GroupSyncWrite(portHandler, packetHandler, self.addr_goal,self.size_goal)

        self.mode_reader = GroupSyncRead(portHandler, packetHandler, ADDR_OPERATING_MODE, SIZE_OPERATING_MODE)
        self.torque_status_reader = GroupSyncRead(portHandler, packetHandler, ADDR_TORQUE_ENABLE, SIZE_TORQUE_ENABLE)
        self.position_reader = GroupSyncRead(portHandler, packetHandler, ADDR_PRESENT_POSITION, SIZE_PRESENT_POSITION)
        self.velocity_reader = GroupSyncRead(portHandler, packetHandler, ADDR_PRESENT_VELOCITY, SIZE_PRESENT_VELOCITY)
        self.pwm_reader = GroupSyncRead(portHandler, packetHandler, ADDR_PRESENT_PWM, SIZE_PRESENT_PWM)
        self.temperature_reader = GroupSyncRead(portHandler, packetHandler, ADDR_PRESENT_TEMPERATURE, SIZE_PRESENT_TEMPERATURE)
        self.current_reader = GroupSyncRead(portHandler,packetHandler, ADDR_PRESENT_CURRENT, SIZE_PRESENT_CURRENT) 
        self.voltage_reader = GroupSyncRead(portHandler, packetHandler, ADDR_PRESENT_INPUT_VOLTAGE, SIZE_PRESENT_INPUT_VOLTAGE)


        for id in self.id_list:
            self.mode_writer.addParam(id, wrap_1_byte(self.mode))  
            self.torque_writer.addParam(id, wrap_1_byte(TORQUE_DISABLE))
            self.goal_writer.addParam(id, wrap_byte(0,self.size_goal))
            
            self.mode_reader.addParam(id)
            self.torque_status_reader.addParam(id)
            self.position_reader.addParam(id)
            self.velocity_reader.addParam(id)
            self.pwm_reader.addParam(id)
            self.temperature_reader.addParam(id)
            self.current_reader.addParam(id)
            self.voltage_reader.addParam(id)
            
        torque_result = self.torque_writer.txPacket()
        if torque_result == COMM_SUCCESS:
            mode_result = self.mode_writer.txPacket()  
            for id in self.id_list:
                current_mode[id] = mode


    def set_torque_status(self, status:int):
        for id in self.id_list:
            self.torque_writer.changeParam(id, wrap_1_byte(status))
        torque_result = self.torque_writer.txPacket()
        time.sleep(0.05)


    def set_goals(self, values:int):
        for i in range(len(self.id_list)):
            self.goal_writer.changeParam(self.id_list[i], wrap_byte(values[i],self.size_goal))
        goal_result = self.goal_writer.txPacket()


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

        self.goal_writer = GroupSyncWrite(portHandler, packetHandler, self.addr_goal,self.size_goal) 

        for id in self.id_list:
            self.mode_writer.changeParam(id,wrap_1_byte(mode))
            self.goal_writer.addParam(id, wrap_byte(0, self.size_goal))
        
        self.set_torque_status(TORQUE_DISABLE)
        mode_result = self.mode_writer.txPacket()
    
    def __update_single_feedback(self, name: str, reader: GroupSyncRead, address: int, size: int):
            read_result = reader.fastSyncRead()
            if read_result == COMM_SUCCESS:
                datas= []
                for id in self.id_list:
                    data = 0
                    if reader.isAvailable(id, address, size):
                        data = reader.getData(id, address, size)
                    datas.append(data)
                self.feedback_data[name] = datas
        
    def get_feedback(self):
        if FEEDBACK_POSITION_ENABLE:
            self.__update_single_feedback(FEEDBACK_POSITION_NAME, self.position_reader, ADDR_PRESENT_POSITION, SIZE_PRESENT_POSITION)
        if FEEDBACK_VELOCITY_ENABLE: 
            self.__update_single_feedback(FEEDBACK_VELOCITY_NAME, self.velocity_reader, ADDR_PRESENT_VELOCITY, SIZE_PRESENT_VELOCITY) 
        return self.feedback_data
    
               
port_init()

# set_torque_enable(0)
# set_torque_enable(1)
# set_mode_velocity(0)
# set_mode_velocity(1)
# set_goal(0, 0)
# set_goal(1, 0)

wheel_group = servo_group(MODE_VELOCITY, [0, 1])
wheel_group.set_torque_status(TORQUE_ENABLE)

wheel_group.set_goals([1000,1000])
time.sleep(1)
result = wheel_group.get_feedback()
print(result)
wheel_group.set_torque_status(TORQUE_DISABLE)
port_close()