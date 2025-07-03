# ========== Communication Setup ==========
PROTOCOL_VERSION = 2.0 

# ========== Operating Modes ==========
ADDR_OPERATING_MODE = 11             # 1 byte
SIZE_OPERATING_MODE = 1

MODE_VELOCITY = 1
MODE_POSITION = 3
MODE_EXTENDED_POSITION = 4
MODE_PWM = 16

# ========== Torque Control ==========
ADDR_TORQUE_ENABLE = 64              # 1 byte
SIZE_TORQUE_ENABLE = 1

TORQUE_DISABLE = 0
TORQUE_ENABLE = 1

# ========== Position Control ==========
ADDR_GOAL_POSITION = 116             # 4 bytes
SIZE_GOAL_POSITION = 4

ADDR_PRESENT_POSITION = 132          # 4 bytes
SIZE_PRESENT_POSITION = 4

ADDR_PROFILE_VELOCITY = 112          # 4 bytes
SIZE_PROFILE_VELOCITY = 4

ADDR_PROFILE_ACCELERATION = 108      # 4 bytes
SIZE_PROFILE_ACCELERATION = 4

ADDR_POSITION_P_GAIN = 84            # 2 bytes
SIZE_POSITION_P_GAIN = 2

ADDR_POSITION_I_GAIN = 82            # 2 bytes
SIZE_POSITION_I_GAIN = 2

ADDR_POSITION_D_GAIN = 80            # 2 bytes
SIZE_POSITION_D_GAIN = 2

DEFAULT_P_GAIN = 800
DEFAULT_I_GAIN = 0
DEFAULT_D_GAIN = 0

POSITION_MIN = 0
POSITION_MAX = 4095                  # For 12-bit resolution

# ========== Velocity Control ==========
ADDR_GOAL_VELOCITY = 104             # 4 bytes
SIZE_GOAL_VELOCITY = 4

ADDR_PRESENT_VELOCITY = 128          # 4 bytes
SIZE_PRESENT_VELOCITY = 4

ADDR_VELOCITY_LIMIT = 44             # 4 bytes
SIZE_VELOCITY_LIMIT = 4

VELOCITY_MIN = -1023
VELOCITY_MAX = 1023

# ========== PWM Control ==========
ADDR_GOAL_PWM = 100                  # 2 bytes
SIZE_GOAL_PWM = 2

ADDR_PRESENT_PWM = 124               # 2 bytes
SIZE_PRESENT_PWM = 2

ADDR_PWM_LIMIT = 36                  # 2 bytes
SIZE_PWM_LIMIT = 2

# ========== Feedback ==========
ADDR_PRESENT_CURRENT = 126           # 2 bytes
SIZE_PRESENT_CURRENT = 2

ADDR_PRESENT_INPUT_VOLTAGE = 144     # 2 bytes
SIZE_PRESENT_INPUT_VOLTAGE = 2

ADDR_PRESENT_TEMPERATURE = 146       # 1 byte
SIZE_PRESENT_TEMPERATURE = 1

# ========== Status Return ==========
ADDR_STATUS_RETURN_LEVEL = 68        # 1 byte
SIZE_STATUS_RETURN_LEVEL = 1

STATUS_RETURN_ALL = 2
STATUS_RETURN_READ = 1
STATUS_RETURN_NONE = 0

# ========== Hardware Info ==========
ADDR_MODEL_NUMBER = 0                # 2 bytes
SIZE_MODEL_NUMBER = 2

ADDR_FIRMWARE_VERSION = 6            # 1 byte
SIZE_FIRMWARE_VERSION = 1

# ========== EEPROM Lock ==========
ADDR_LOCK = 120                      # 1 byte
SIZE_LOCK = 1

LOCK_OFF = 0
LOCK_ON = 1