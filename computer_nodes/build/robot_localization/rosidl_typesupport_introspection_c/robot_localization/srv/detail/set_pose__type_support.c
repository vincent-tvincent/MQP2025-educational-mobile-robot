// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from robot_localization:srv/SetPose.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "robot_localization/srv/detail/set_pose__rosidl_typesupport_introspection_c.h"
#include "robot_localization/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "robot_localization/srv/detail/set_pose__functions.h"
#include "robot_localization/srv/detail/set_pose__struct.h"


// Include directives for member types
// Member `pose`
#include "geometry_msgs/msg/pose_with_covariance_stamped.h"
// Member `pose`
#include "geometry_msgs/msg/detail/pose_with_covariance_stamped__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void robot_localization__srv__SetPose_Request__rosidl_typesupport_introspection_c__SetPose_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_localization__srv__SetPose_Request__init(message_memory);
}

void robot_localization__srv__SetPose_Request__rosidl_typesupport_introspection_c__SetPose_Request_fini_function(void * message_memory)
{
  robot_localization__srv__SetPose_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember robot_localization__srv__SetPose_Request__rosidl_typesupport_introspection_c__SetPose_Request_message_member_array[1] = {
  {
    "pose",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_localization__srv__SetPose_Request, pose),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers robot_localization__srv__SetPose_Request__rosidl_typesupport_introspection_c__SetPose_Request_message_members = {
  "robot_localization__srv",  // message namespace
  "SetPose_Request",  // message name
  1,  // number of fields
  sizeof(robot_localization__srv__SetPose_Request),
  false,  // has_any_key_member_
  robot_localization__srv__SetPose_Request__rosidl_typesupport_introspection_c__SetPose_Request_message_member_array,  // message members
  robot_localization__srv__SetPose_Request__rosidl_typesupport_introspection_c__SetPose_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  robot_localization__srv__SetPose_Request__rosidl_typesupport_introspection_c__SetPose_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t robot_localization__srv__SetPose_Request__rosidl_typesupport_introspection_c__SetPose_Request_message_type_support_handle = {
  0,
  &robot_localization__srv__SetPose_Request__rosidl_typesupport_introspection_c__SetPose_Request_message_members,
  get_message_typesupport_handle_function,
  &robot_localization__srv__SetPose_Request__get_type_hash,
  &robot_localization__srv__SetPose_Request__get_type_description,
  &robot_localization__srv__SetPose_Request__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_localization
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_localization, srv, SetPose_Request)() {
  robot_localization__srv__SetPose_Request__rosidl_typesupport_introspection_c__SetPose_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, PoseWithCovarianceStamped)();
  if (!robot_localization__srv__SetPose_Request__rosidl_typesupport_introspection_c__SetPose_Request_message_type_support_handle.typesupport_identifier) {
    robot_localization__srv__SetPose_Request__rosidl_typesupport_introspection_c__SetPose_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &robot_localization__srv__SetPose_Request__rosidl_typesupport_introspection_c__SetPose_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "robot_localization/srv/detail/set_pose__rosidl_typesupport_introspection_c.h"
// already included above
// #include "robot_localization/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "robot_localization/srv/detail/set_pose__functions.h"
// already included above
// #include "robot_localization/srv/detail/set_pose__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void robot_localization__srv__SetPose_Response__rosidl_typesupport_introspection_c__SetPose_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_localization__srv__SetPose_Response__init(message_memory);
}

void robot_localization__srv__SetPose_Response__rosidl_typesupport_introspection_c__SetPose_Response_fini_function(void * message_memory)
{
  robot_localization__srv__SetPose_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember robot_localization__srv__SetPose_Response__rosidl_typesupport_introspection_c__SetPose_Response_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_localization__srv__SetPose_Response, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers robot_localization__srv__SetPose_Response__rosidl_typesupport_introspection_c__SetPose_Response_message_members = {
  "robot_localization__srv",  // message namespace
  "SetPose_Response",  // message name
  1,  // number of fields
  sizeof(robot_localization__srv__SetPose_Response),
  false,  // has_any_key_member_
  robot_localization__srv__SetPose_Response__rosidl_typesupport_introspection_c__SetPose_Response_message_member_array,  // message members
  robot_localization__srv__SetPose_Response__rosidl_typesupport_introspection_c__SetPose_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  robot_localization__srv__SetPose_Response__rosidl_typesupport_introspection_c__SetPose_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t robot_localization__srv__SetPose_Response__rosidl_typesupport_introspection_c__SetPose_Response_message_type_support_handle = {
  0,
  &robot_localization__srv__SetPose_Response__rosidl_typesupport_introspection_c__SetPose_Response_message_members,
  get_message_typesupport_handle_function,
  &robot_localization__srv__SetPose_Response__get_type_hash,
  &robot_localization__srv__SetPose_Response__get_type_description,
  &robot_localization__srv__SetPose_Response__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_localization
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_localization, srv, SetPose_Response)() {
  if (!robot_localization__srv__SetPose_Response__rosidl_typesupport_introspection_c__SetPose_Response_message_type_support_handle.typesupport_identifier) {
    robot_localization__srv__SetPose_Response__rosidl_typesupport_introspection_c__SetPose_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &robot_localization__srv__SetPose_Response__rosidl_typesupport_introspection_c__SetPose_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "robot_localization/srv/detail/set_pose__rosidl_typesupport_introspection_c.h"
// already included above
// #include "robot_localization/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "robot_localization/srv/detail/set_pose__functions.h"
// already included above
// #include "robot_localization/srv/detail/set_pose__struct.h"


// Include directives for member types
// Member `info`
#include "service_msgs/msg/service_event_info.h"
// Member `info`
#include "service_msgs/msg/detail/service_event_info__rosidl_typesupport_introspection_c.h"
// Member `request`
// Member `response`
#include "robot_localization/srv/set_pose.h"
// Member `request`
// Member `response`
// already included above
// #include "robot_localization/srv/detail/set_pose__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_localization__srv__SetPose_Event__init(message_memory);
}

void robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_fini_function(void * message_memory)
{
  robot_localization__srv__SetPose_Event__fini(message_memory);
}

size_t robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__size_function__SetPose_Event__request(
  const void * untyped_member)
{
  const robot_localization__srv__SetPose_Request__Sequence * member =
    (const robot_localization__srv__SetPose_Request__Sequence *)(untyped_member);
  return member->size;
}

const void * robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__get_const_function__SetPose_Event__request(
  const void * untyped_member, size_t index)
{
  const robot_localization__srv__SetPose_Request__Sequence * member =
    (const robot_localization__srv__SetPose_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void * robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__get_function__SetPose_Event__request(
  void * untyped_member, size_t index)
{
  robot_localization__srv__SetPose_Request__Sequence * member =
    (robot_localization__srv__SetPose_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__fetch_function__SetPose_Event__request(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const robot_localization__srv__SetPose_Request * item =
    ((const robot_localization__srv__SetPose_Request *)
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__get_const_function__SetPose_Event__request(untyped_member, index));
  robot_localization__srv__SetPose_Request * value =
    (robot_localization__srv__SetPose_Request *)(untyped_value);
  *value = *item;
}

void robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__assign_function__SetPose_Event__request(
  void * untyped_member, size_t index, const void * untyped_value)
{
  robot_localization__srv__SetPose_Request * item =
    ((robot_localization__srv__SetPose_Request *)
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__get_function__SetPose_Event__request(untyped_member, index));
  const robot_localization__srv__SetPose_Request * value =
    (const robot_localization__srv__SetPose_Request *)(untyped_value);
  *item = *value;
}

bool robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__resize_function__SetPose_Event__request(
  void * untyped_member, size_t size)
{
  robot_localization__srv__SetPose_Request__Sequence * member =
    (robot_localization__srv__SetPose_Request__Sequence *)(untyped_member);
  robot_localization__srv__SetPose_Request__Sequence__fini(member);
  return robot_localization__srv__SetPose_Request__Sequence__init(member, size);
}

size_t robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__size_function__SetPose_Event__response(
  const void * untyped_member)
{
  const robot_localization__srv__SetPose_Response__Sequence * member =
    (const robot_localization__srv__SetPose_Response__Sequence *)(untyped_member);
  return member->size;
}

const void * robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__get_const_function__SetPose_Event__response(
  const void * untyped_member, size_t index)
{
  const robot_localization__srv__SetPose_Response__Sequence * member =
    (const robot_localization__srv__SetPose_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void * robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__get_function__SetPose_Event__response(
  void * untyped_member, size_t index)
{
  robot_localization__srv__SetPose_Response__Sequence * member =
    (robot_localization__srv__SetPose_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__fetch_function__SetPose_Event__response(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const robot_localization__srv__SetPose_Response * item =
    ((const robot_localization__srv__SetPose_Response *)
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__get_const_function__SetPose_Event__response(untyped_member, index));
  robot_localization__srv__SetPose_Response * value =
    (robot_localization__srv__SetPose_Response *)(untyped_value);
  *value = *item;
}

void robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__assign_function__SetPose_Event__response(
  void * untyped_member, size_t index, const void * untyped_value)
{
  robot_localization__srv__SetPose_Response * item =
    ((robot_localization__srv__SetPose_Response *)
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__get_function__SetPose_Event__response(untyped_member, index));
  const robot_localization__srv__SetPose_Response * value =
    (const robot_localization__srv__SetPose_Response *)(untyped_value);
  *item = *value;
}

bool robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__resize_function__SetPose_Event__response(
  void * untyped_member, size_t size)
{
  robot_localization__srv__SetPose_Response__Sequence * member =
    (robot_localization__srv__SetPose_Response__Sequence *)(untyped_member);
  robot_localization__srv__SetPose_Response__Sequence__fini(member);
  return robot_localization__srv__SetPose_Response__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_message_member_array[3] = {
  {
    "info",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_localization__srv__SetPose_Event, info),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "request",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(robot_localization__srv__SetPose_Event, request),  // bytes offset in struct
    NULL,  // default value
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__size_function__SetPose_Event__request,  // size() function pointer
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__get_const_function__SetPose_Event__request,  // get_const(index) function pointer
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__get_function__SetPose_Event__request,  // get(index) function pointer
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__fetch_function__SetPose_Event__request,  // fetch(index, &value) function pointer
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__assign_function__SetPose_Event__request,  // assign(index, value) function pointer
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__resize_function__SetPose_Event__request  // resize(index) function pointer
  },
  {
    "response",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(robot_localization__srv__SetPose_Event, response),  // bytes offset in struct
    NULL,  // default value
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__size_function__SetPose_Event__response,  // size() function pointer
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__get_const_function__SetPose_Event__response,  // get_const(index) function pointer
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__get_function__SetPose_Event__response,  // get(index) function pointer
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__fetch_function__SetPose_Event__response,  // fetch(index, &value) function pointer
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__assign_function__SetPose_Event__response,  // assign(index, value) function pointer
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__resize_function__SetPose_Event__response  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_message_members = {
  "robot_localization__srv",  // message namespace
  "SetPose_Event",  // message name
  3,  // number of fields
  sizeof(robot_localization__srv__SetPose_Event),
  false,  // has_any_key_member_
  robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_message_member_array,  // message members
  robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_init_function,  // function to initialize message memory (memory has to be allocated)
  robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_message_type_support_handle = {
  0,
  &robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_message_members,
  get_message_typesupport_handle_function,
  &robot_localization__srv__SetPose_Event__get_type_hash,
  &robot_localization__srv__SetPose_Event__get_type_description,
  &robot_localization__srv__SetPose_Event__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_localization
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_localization, srv, SetPose_Event)() {
  robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_msgs, msg, ServiceEventInfo)();
  robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_localization, srv, SetPose_Request)();
  robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_localization, srv, SetPose_Response)();
  if (!robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_message_type_support_handle.typesupport_identifier) {
    robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "robot_localization/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "robot_localization/srv/detail/set_pose__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers robot_localization__srv__detail__set_pose__rosidl_typesupport_introspection_c__SetPose_service_members = {
  "robot_localization__srv",  // service namespace
  "SetPose",  // service name
  // the following fields are initialized below on first access
  NULL,  // request message
  // robot_localization__srv__detail__set_pose__rosidl_typesupport_introspection_c__SetPose_Request_message_type_support_handle,
  NULL,  // response message
  // robot_localization__srv__detail__set_pose__rosidl_typesupport_introspection_c__SetPose_Response_message_type_support_handle
  NULL  // event_message
  // robot_localization__srv__detail__set_pose__rosidl_typesupport_introspection_c__SetPose_Response_message_type_support_handle
};


static rosidl_service_type_support_t robot_localization__srv__detail__set_pose__rosidl_typesupport_introspection_c__SetPose_service_type_support_handle = {
  0,
  &robot_localization__srv__detail__set_pose__rosidl_typesupport_introspection_c__SetPose_service_members,
  get_service_typesupport_handle_function,
  &robot_localization__srv__SetPose_Request__rosidl_typesupport_introspection_c__SetPose_Request_message_type_support_handle,
  &robot_localization__srv__SetPose_Response__rosidl_typesupport_introspection_c__SetPose_Response_message_type_support_handle,
  &robot_localization__srv__SetPose_Event__rosidl_typesupport_introspection_c__SetPose_Event_message_type_support_handle,
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_CREATE_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    robot_localization,
    srv,
    SetPose
  ),
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_DESTROY_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    robot_localization,
    srv,
    SetPose
  ),
  &robot_localization__srv__SetPose__get_type_hash,
  &robot_localization__srv__SetPose__get_type_description,
  &robot_localization__srv__SetPose__get_type_description_sources,
};

// Forward declaration of message type support functions for service members
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_localization, srv, SetPose_Request)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_localization, srv, SetPose_Response)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_localization, srv, SetPose_Event)(void);

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_localization
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_localization, srv, SetPose)(void) {
  if (!robot_localization__srv__detail__set_pose__rosidl_typesupport_introspection_c__SetPose_service_type_support_handle.typesupport_identifier) {
    robot_localization__srv__detail__set_pose__rosidl_typesupport_introspection_c__SetPose_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)robot_localization__srv__detail__set_pose__rosidl_typesupport_introspection_c__SetPose_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_localization, srv, SetPose_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_localization, srv, SetPose_Response)()->data;
  }
  if (!service_members->event_members_) {
    service_members->event_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_localization, srv, SetPose_Event)()->data;
  }

  return &robot_localization__srv__detail__set_pose__rosidl_typesupport_introspection_c__SetPose_service_type_support_handle;
}
