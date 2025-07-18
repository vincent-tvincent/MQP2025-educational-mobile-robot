// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from robot_localization:srv/SetPose.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "robot_localization/srv/detail/set_pose__functions.h"
#include "robot_localization/srv/detail/set_pose__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace robot_localization
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _SetPose_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _SetPose_Request_type_support_ids_t;

static const _SetPose_Request_type_support_ids_t _SetPose_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _SetPose_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _SetPose_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _SetPose_Request_type_support_symbol_names_t _SetPose_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_localization, srv, SetPose_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_localization, srv, SetPose_Request)),
  }
};

typedef struct _SetPose_Request_type_support_data_t
{
  void * data[2];
} _SetPose_Request_type_support_data_t;

static _SetPose_Request_type_support_data_t _SetPose_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _SetPose_Request_message_typesupport_map = {
  2,
  "robot_localization",
  &_SetPose_Request_message_typesupport_ids.typesupport_identifier[0],
  &_SetPose_Request_message_typesupport_symbol_names.symbol_name[0],
  &_SetPose_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t SetPose_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_SetPose_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
  &robot_localization__srv__SetPose_Request__get_type_hash,
  &robot_localization__srv__SetPose_Request__get_type_description,
  &robot_localization__srv__SetPose_Request__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace robot_localization

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robot_localization::srv::SetPose_Request>()
{
  return &::robot_localization::srv::rosidl_typesupport_cpp::SetPose_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, robot_localization, srv, SetPose_Request)() {
  return get_message_type_support_handle<robot_localization::srv::SetPose_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "robot_localization/srv/detail/set_pose__functions.h"
// already included above
// #include "robot_localization/srv/detail/set_pose__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace robot_localization
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _SetPose_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _SetPose_Response_type_support_ids_t;

static const _SetPose_Response_type_support_ids_t _SetPose_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _SetPose_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _SetPose_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _SetPose_Response_type_support_symbol_names_t _SetPose_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_localization, srv, SetPose_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_localization, srv, SetPose_Response)),
  }
};

typedef struct _SetPose_Response_type_support_data_t
{
  void * data[2];
} _SetPose_Response_type_support_data_t;

static _SetPose_Response_type_support_data_t _SetPose_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _SetPose_Response_message_typesupport_map = {
  2,
  "robot_localization",
  &_SetPose_Response_message_typesupport_ids.typesupport_identifier[0],
  &_SetPose_Response_message_typesupport_symbol_names.symbol_name[0],
  &_SetPose_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t SetPose_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_SetPose_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
  &robot_localization__srv__SetPose_Response__get_type_hash,
  &robot_localization__srv__SetPose_Response__get_type_description,
  &robot_localization__srv__SetPose_Response__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace robot_localization

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robot_localization::srv::SetPose_Response>()
{
  return &::robot_localization::srv::rosidl_typesupport_cpp::SetPose_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, robot_localization, srv, SetPose_Response)() {
  return get_message_type_support_handle<robot_localization::srv::SetPose_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "robot_localization/srv/detail/set_pose__functions.h"
// already included above
// #include "robot_localization/srv/detail/set_pose__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace robot_localization
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _SetPose_Event_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _SetPose_Event_type_support_ids_t;

static const _SetPose_Event_type_support_ids_t _SetPose_Event_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _SetPose_Event_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _SetPose_Event_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _SetPose_Event_type_support_symbol_names_t _SetPose_Event_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_localization, srv, SetPose_Event)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_localization, srv, SetPose_Event)),
  }
};

typedef struct _SetPose_Event_type_support_data_t
{
  void * data[2];
} _SetPose_Event_type_support_data_t;

static _SetPose_Event_type_support_data_t _SetPose_Event_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _SetPose_Event_message_typesupport_map = {
  2,
  "robot_localization",
  &_SetPose_Event_message_typesupport_ids.typesupport_identifier[0],
  &_SetPose_Event_message_typesupport_symbol_names.symbol_name[0],
  &_SetPose_Event_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t SetPose_Event_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_SetPose_Event_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
  &robot_localization__srv__SetPose_Event__get_type_hash,
  &robot_localization__srv__SetPose_Event__get_type_description,
  &robot_localization__srv__SetPose_Event__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace robot_localization

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robot_localization::srv::SetPose_Event>()
{
  return &::robot_localization::srv::rosidl_typesupport_cpp::SetPose_Event_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, robot_localization, srv, SetPose_Event)() {
  return get_message_type_support_handle<robot_localization::srv::SetPose_Event>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "robot_localization/srv/detail/set_pose__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace robot_localization
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _SetPose_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _SetPose_type_support_ids_t;

static const _SetPose_type_support_ids_t _SetPose_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _SetPose_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _SetPose_type_support_symbol_names_t;
#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _SetPose_type_support_symbol_names_t _SetPose_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_localization, srv, SetPose)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_localization, srv, SetPose)),
  }
};

typedef struct _SetPose_type_support_data_t
{
  void * data[2];
} _SetPose_type_support_data_t;

static _SetPose_type_support_data_t _SetPose_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _SetPose_service_typesupport_map = {
  2,
  "robot_localization",
  &_SetPose_service_typesupport_ids.typesupport_identifier[0],
  &_SetPose_service_typesupport_symbol_names.symbol_name[0],
  &_SetPose_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t SetPose_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_SetPose_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
  ::rosidl_typesupport_cpp::get_message_type_support_handle<robot_localization::srv::SetPose_Request>(),
  ::rosidl_typesupport_cpp::get_message_type_support_handle<robot_localization::srv::SetPose_Response>(),
  ::rosidl_typesupport_cpp::get_message_type_support_handle<robot_localization::srv::SetPose_Event>(),
  &::rosidl_typesupport_cpp::service_create_event_message<robot_localization::srv::SetPose>,
  &::rosidl_typesupport_cpp::service_destroy_event_message<robot_localization::srv::SetPose>,
  &robot_localization__srv__SetPose__get_type_hash,
  &robot_localization__srv__SetPose__get_type_description,
  &robot_localization__srv__SetPose__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace robot_localization

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<robot_localization::srv::SetPose>()
{
  return &::robot_localization::srv::rosidl_typesupport_cpp::SetPose_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_cpp, robot_localization, srv, SetPose)() {
  return ::rosidl_typesupport_cpp::get_service_type_support_handle<robot_localization::srv::SetPose>();
}

#ifdef __cplusplus
}
#endif
