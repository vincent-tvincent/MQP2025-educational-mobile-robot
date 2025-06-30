from .robot_constant import *
from .xl330_constant import *
from .dynamixel_sdk import *

portHandler = PortHandler(DEVICENAME)  
# packetHandler = PacketHandler(PROTOCOL_VERSION)
minimum_blocked_delay = 0.01  # Minimum delay required for two communications

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


class servo_group():

    def wrap_1_byte(self, value: int) -> list[int]:
        return [value]


    def wrap_2_byte(self, value: int) -> list[int]:
        return [DXL_LOBYTE(value), DXL_HIBYTE(value)]


    def wrap_4_byte(self, value: int) -> list[int]:
        return [DXL_LOBYTE(DXL_LOWORD(value)), DXL_HIBYTE(DXL_LOWORD(value)), DXL_LOBYTE(DXL_HIWORD(value)), DXL_HIBYTE(DXL_HIWORD(value))]

    def wrap_byte(self, value: int, size: int) -> list[int]:
        match size:
            case 1:
                return self.wrap_1_byte(value)
            case 2:
                return self.wrap_2_byte(value)
            case 4:
                return self.wrap_4_byte(value) 


    def __init__(self,mode: int, portHandler: PortHandler, id_list: list[int]):
        self.portHandler = portHandler
        self.packetHandler = PacketHandler(PROTOCOL_VERSION)
        self.__mode = mode
        self.id_list = id_list
        self.__recent_mode = {id: mode for id in id_list}
        self.__feedback_data = {}
        self.enable_blocked_delay = True

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

        self.mode_writer = GroupSyncWrite(self.portHandler, self.packetHandler, ADDR_OPERATING_MODE, SIZE_OPERATING_MODE)
        self.torque_writer = GroupSyncWrite(self.portHandler, self.packetHandler, ADDR_TORQUE_ENABLE, SIZE_TORQUE_ENABLE)
        self.goal_writer = GroupSyncWrite(self.portHandler, self.packetHandler, self.addr_goal,self.size_goal)

        self.mode_reader = GroupSyncRead(self.portHandler, self.packetHandler, ADDR_OPERATING_MODE, SIZE_OPERATING_MODE)
        self.torque_status_reader = GroupSyncRead(self.portHandler, self.packetHandler, ADDR_TORQUE_ENABLE, SIZE_TORQUE_ENABLE)
        self.position_reader = GroupSyncRead(self.portHandler, self.packetHandler, ADDR_PRESENT_POSITION, SIZE_PRESENT_POSITION)
        self.velocity_reader = GroupSyncRead(self.portHandler, self.packetHandler, ADDR_PRESENT_VELOCITY, SIZE_PRESENT_VELOCITY)
        self.pwm_reader = GroupSyncRead(self.portHandler, self.packetHandler, ADDR_PRESENT_PWM, SIZE_PRESENT_PWM)
        self.temperature_reader = GroupSyncRead(self.portHandler, self.packetHandler, ADDR_PRESENT_TEMPERATURE, SIZE_PRESENT_TEMPERATURE)
        self.current_reader = GroupSyncRead(self.portHandler, self.packetHandler, ADDR_PRESENT_CURRENT, SIZE_PRESENT_CURRENT) 
        self.voltage_reader = GroupSyncRead(self.portHandler, self.packetHandler, ADDR_PRESENT_INPUT_VOLTAGE, SIZE_PRESENT_INPUT_VOLTAGE)


        for id in self.id_list:
            self.mode_writer.addParam(id, self.wrap_1_byte(self.__mode))  
            self.torque_writer.addParam(id, self.wrap_1_byte(TORQUE_DISABLE))
            self.goal_writer.addParam(id, self.wrap_byte(0,self.size_goal))
            
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
                self.__recent_mode[id] = mode


    def enable_blocked_delay(self):
        self.enable_blocked_delay = True


    def disable_blocked_delay(self):
        self.enable_blocked_delay = False


    def __apply_blocked_delay(self, second: float):
        if self.enable_blocked_delay:
            time.sleep(second)

    def set_torque_status(self, status:int):
        for id in self.id_list:
            self.torque_writer.changeParam(id, self.wrap_1_byte(status))
        torque_result = self.torque_writer.txPacket()
        self.__apply_blocked_delay(minimum_blocked_delay)
        return torque_result


    def set_goals(self, values:int):
        for i in range(len(self.id_list)):
            self.goal_writer.changeParam(self.id_list[i], self.wrap_byte(values[i],self.size_goal))
        goal_result = self.goal_writer.txPacket()
        self.__apply_blocked_delay(minimum_blocked_delay)
        return goal_result 


    def get_mode(self) -> list[int]:
        read_result = self.mode_reader.fastSyncRead()
        if read_result == COMM_SUCCESS:
            modes = []
            for id in self.id_list:
                mode = 0
                if self.mode_reader.isAvailable(id, ADDR_OPERATING_MODE, SIZE_OPERATING_MODE):
                    mode = self.mode_reader.getData(id, ADDR_OPERATING_MODE, SIZE_OPERATING_MODE)
                modes.append(mode)
            return modes
        else:
            return None
        

    def set_mode(self, mode:int):
        self.__mode = mode

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

        self.goal_writer = GroupSyncWrite(self.portHandler, packetHandler, self.addr_goal,self.size_goal)
        self.__apply_blocked_delay(minimum_blocked_delay) 

        for id in self.id_list:
            self.mode_writer.changeParam(id,self.wrap_1_byte(mode))
            self.goal_writer.addParam(id, self.wrap_byte(0, self.size_goal))
        
        self.set_torque_status(TORQUE_DISABLE)
        mode_result = self.mode_writer.txPacket()
        return mode_result


    def __update_single_feedback(self, name: str, reader: GroupSyncRead, address: int, size: int):
            read_result = reader.fastSyncRead()
            if read_result == COMM_SUCCESS:
                datas= []
                for id in self.id_list:
                    data = 0
                    if reader.isAvailable(id, address, size):
                        data = reader.getData(id, address, size)
                    datas.append(data)
                self.__feedback_data[name] = datas
            return read_result


    def __feedback_data_preprocessing(self, feedback_data: dict) -> dict:
        """
        Preprocess the feedback data to convert it into a more usable format.
        """
        for id, data in feedback_data.items():
            for i in range(len(feedback_data[id])):
                # process unsigned integers to signed integers 
                if feedback_data[id][i] & (1 << 31):
                    feedback_data[id][i] = feedback_data[id][i] - (1 << 32)
        return feedback_data


    def get_feedback(self) -> dict:
        
        if FEEDBACK_POSITION_ENABLE:
            self.__update_single_feedback(FEEDBACK_POSITION_NAME, self.position_reader, ADDR_PRESENT_POSITION, SIZE_PRESENT_POSITION)
        if FEEDBACK_VELOCITY_ENABLE: 
            self.__update_single_feedback(FEEDBACK_VELOCITY_NAME, self.velocity_reader, ADDR_PRESENT_VELOCITY, SIZE_PRESENT_VELOCITY) 
        if FEEDBACK_PWM_ENABLE: 
            self.__update_single_feedback(FEEDBACK_PWM_NAME, self.velocity_reader, ADDR_PRESENT_PWM, SIZE_PRESENT_PWM)
        if FEEDBACK_TEMPERATURE_ENABLE:
            self.__update_single_feedback(FEEDBACK_TEMPERATURE_NAME, self.temperature_reader, ADDR_PRESENT_TEMPERATURE, SIZE_PRESENT_TEMPERATURE)
        if FEEDBACK_CURRENT_ENABLE:
            self.__update_single_feedback(FEEDBACK_CURRENT_NAME, self.current_reader, ADDR_PRESENT_CURRENT, SIZE_PRESENT_CURRENT)
        if FEEDBACK_VOLTAGE_ENABLE:
            self.__update_single_feedback(FEEDBACK_VOLTAGE_NAME, self.current_reader, ADDR_PRESENT_INPUT_VOLTAGE, SIZE_PRESENT_INPUT_VOLTAGE)
        # self.__apply_blocked_delay(minimum_blocked_delay)
        return self.__feedback_data_preprocessing(self.__feedback_data)
    
               
