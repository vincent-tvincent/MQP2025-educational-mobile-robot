// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robot_localization:srv/SetUTMZone.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robot_localization/srv/set_utm_zone.hpp"


#ifndef ROBOT_LOCALIZATION__SRV__DETAIL__SET_UTM_ZONE__TRAITS_HPP_
#define ROBOT_LOCALIZATION__SRV__DETAIL__SET_UTM_ZONE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "robot_localization/srv/detail/set_utm_zone__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace robot_localization
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetUTMZone_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: utm_zone
  {
    out << "utm_zone: ";
    rosidl_generator_traits::value_to_yaml(msg.utm_zone, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetUTMZone_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: utm_zone
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "utm_zone: ";
    rosidl_generator_traits::value_to_yaml(msg.utm_zone, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetUTMZone_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace robot_localization

namespace rosidl_generator_traits
{

[[deprecated("use robot_localization::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_localization::srv::SetUTMZone_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_localization::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_localization::srv::to_yaml() instead")]]
inline std::string to_yaml(const robot_localization::srv::SetUTMZone_Request & msg)
{
  return robot_localization::srv::to_yaml(msg);
}

template<>
inline const char * data_type<robot_localization::srv::SetUTMZone_Request>()
{
  return "robot_localization::srv::SetUTMZone_Request";
}

template<>
inline const char * name<robot_localization::srv::SetUTMZone_Request>()
{
  return "robot_localization/srv/SetUTMZone_Request";
}

template<>
struct has_fixed_size<robot_localization::srv::SetUTMZone_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<robot_localization::srv::SetUTMZone_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<robot_localization::srv::SetUTMZone_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace robot_localization
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetUTMZone_Response & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetUTMZone_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetUTMZone_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace robot_localization

namespace rosidl_generator_traits
{

[[deprecated("use robot_localization::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_localization::srv::SetUTMZone_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_localization::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_localization::srv::to_yaml() instead")]]
inline std::string to_yaml(const robot_localization::srv::SetUTMZone_Response & msg)
{
  return robot_localization::srv::to_yaml(msg);
}

template<>
inline const char * data_type<robot_localization::srv::SetUTMZone_Response>()
{
  return "robot_localization::srv::SetUTMZone_Response";
}

template<>
inline const char * name<robot_localization::srv::SetUTMZone_Response>()
{
  return "robot_localization/srv/SetUTMZone_Response";
}

template<>
struct has_fixed_size<robot_localization::srv::SetUTMZone_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<robot_localization::srv::SetUTMZone_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<robot_localization::srv::SetUTMZone_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace robot_localization
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetUTMZone_Event & msg,
  std::ostream & out)
{
  out << "{";
  // member: info
  {
    out << "info: ";
    to_flow_style_yaml(msg.info, out);
    out << ", ";
  }

  // member: request
  {
    if (msg.request.size() == 0) {
      out << "request: []";
    } else {
      out << "request: [";
      size_t pending_items = msg.request.size();
      for (auto item : msg.request) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: response
  {
    if (msg.response.size() == 0) {
      out << "response: []";
    } else {
      out << "response: [";
      size_t pending_items = msg.response.size();
      for (auto item : msg.response) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetUTMZone_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: info
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "info:\n";
    to_block_style_yaml(msg.info, out, indentation + 2);
  }

  // member: request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.request.size() == 0) {
      out << "request: []\n";
    } else {
      out << "request:\n";
      for (auto item : msg.request) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.response.size() == 0) {
      out << "response: []\n";
    } else {
      out << "response:\n";
      for (auto item : msg.response) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetUTMZone_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace robot_localization

namespace rosidl_generator_traits
{

[[deprecated("use robot_localization::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_localization::srv::SetUTMZone_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_localization::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_localization::srv::to_yaml() instead")]]
inline std::string to_yaml(const robot_localization::srv::SetUTMZone_Event & msg)
{
  return robot_localization::srv::to_yaml(msg);
}

template<>
inline const char * data_type<robot_localization::srv::SetUTMZone_Event>()
{
  return "robot_localization::srv::SetUTMZone_Event";
}

template<>
inline const char * name<robot_localization::srv::SetUTMZone_Event>()
{
  return "robot_localization/srv/SetUTMZone_Event";
}

template<>
struct has_fixed_size<robot_localization::srv::SetUTMZone_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<robot_localization::srv::SetUTMZone_Event>
  : std::integral_constant<bool, has_bounded_size<robot_localization::srv::SetUTMZone_Request>::value && has_bounded_size<robot_localization::srv::SetUTMZone_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<robot_localization::srv::SetUTMZone_Event>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_localization::srv::SetUTMZone>()
{
  return "robot_localization::srv::SetUTMZone";
}

template<>
inline const char * name<robot_localization::srv::SetUTMZone>()
{
  return "robot_localization/srv/SetUTMZone";
}

template<>
struct has_fixed_size<robot_localization::srv::SetUTMZone>
  : std::integral_constant<
    bool,
    has_fixed_size<robot_localization::srv::SetUTMZone_Request>::value &&
    has_fixed_size<robot_localization::srv::SetUTMZone_Response>::value
  >
{
};

template<>
struct has_bounded_size<robot_localization::srv::SetUTMZone>
  : std::integral_constant<
    bool,
    has_bounded_size<robot_localization::srv::SetUTMZone_Request>::value &&
    has_bounded_size<robot_localization::srv::SetUTMZone_Response>::value
  >
{
};

template<>
struct is_service<robot_localization::srv::SetUTMZone>
  : std::true_type
{
};

template<>
struct is_service_request<robot_localization::srv::SetUTMZone_Request>
  : std::true_type
{
};

template<>
struct is_service_response<robot_localization::srv::SetUTMZone_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ROBOT_LOCALIZATION__SRV__DETAIL__SET_UTM_ZONE__TRAITS_HPP_
