// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_localization:srv/ToLL.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robot_localization/srv/to_ll.hpp"


#ifndef ROBOT_LOCALIZATION__SRV__DETAIL__TO_LL__STRUCT_HPP_
#define ROBOT_LOCALIZATION__SRV__DETAIL__TO_LL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'map_point'
#include "geometry_msgs/msg/detail/point__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__robot_localization__srv__ToLL_Request __attribute__((deprecated))
#else
# define DEPRECATED__robot_localization__srv__ToLL_Request __declspec(deprecated)
#endif

namespace robot_localization
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ToLL_Request_
{
  using Type = ToLL_Request_<ContainerAllocator>;

  explicit ToLL_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : map_point(_init)
  {
    (void)_init;
  }

  explicit ToLL_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : map_point(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _map_point_type =
    geometry_msgs::msg::Point_<ContainerAllocator>;
  _map_point_type map_point;

  // setters for named parameter idiom
  Type & set__map_point(
    const geometry_msgs::msg::Point_<ContainerAllocator> & _arg)
  {
    this->map_point = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_localization::srv::ToLL_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_localization::srv::ToLL_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_localization::srv::ToLL_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_localization::srv::ToLL_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_localization::srv::ToLL_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_localization::srv::ToLL_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_localization::srv::ToLL_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_localization::srv::ToLL_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_localization::srv::ToLL_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_localization::srv::ToLL_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_localization__srv__ToLL_Request
    std::shared_ptr<robot_localization::srv::ToLL_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_localization__srv__ToLL_Request
    std::shared_ptr<robot_localization::srv::ToLL_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ToLL_Request_ & other) const
  {
    if (this->map_point != other.map_point) {
      return false;
    }
    return true;
  }
  bool operator!=(const ToLL_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ToLL_Request_

// alias to use template instance with default allocator
using ToLL_Request =
  robot_localization::srv::ToLL_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace robot_localization


// Include directives for member types
// Member 'll_point'
#include "geographic_msgs/msg/detail/geo_point__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__robot_localization__srv__ToLL_Response __attribute__((deprecated))
#else
# define DEPRECATED__robot_localization__srv__ToLL_Response __declspec(deprecated)
#endif

namespace robot_localization
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ToLL_Response_
{
  using Type = ToLL_Response_<ContainerAllocator>;

  explicit ToLL_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ll_point(_init)
  {
    (void)_init;
  }

  explicit ToLL_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ll_point(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _ll_point_type =
    geographic_msgs::msg::GeoPoint_<ContainerAllocator>;
  _ll_point_type ll_point;

  // setters for named parameter idiom
  Type & set__ll_point(
    const geographic_msgs::msg::GeoPoint_<ContainerAllocator> & _arg)
  {
    this->ll_point = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_localization::srv::ToLL_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_localization::srv::ToLL_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_localization::srv::ToLL_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_localization::srv::ToLL_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_localization::srv::ToLL_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_localization::srv::ToLL_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_localization::srv::ToLL_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_localization::srv::ToLL_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_localization::srv::ToLL_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_localization::srv::ToLL_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_localization__srv__ToLL_Response
    std::shared_ptr<robot_localization::srv::ToLL_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_localization__srv__ToLL_Response
    std::shared_ptr<robot_localization::srv::ToLL_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ToLL_Response_ & other) const
  {
    if (this->ll_point != other.ll_point) {
      return false;
    }
    return true;
  }
  bool operator!=(const ToLL_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ToLL_Response_

// alias to use template instance with default allocator
using ToLL_Response =
  robot_localization::srv::ToLL_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace robot_localization


// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__robot_localization__srv__ToLL_Event __attribute__((deprecated))
#else
# define DEPRECATED__robot_localization__srv__ToLL_Event __declspec(deprecated)
#endif

namespace robot_localization
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ToLL_Event_
{
  using Type = ToLL_Event_<ContainerAllocator>;

  explicit ToLL_Event_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : info(_init)
  {
    (void)_init;
  }

  explicit ToLL_Event_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : info(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _info_type =
    service_msgs::msg::ServiceEventInfo_<ContainerAllocator>;
  _info_type info;
  using _request_type =
    rosidl_runtime_cpp::BoundedVector<robot_localization::srv::ToLL_Request_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<robot_localization::srv::ToLL_Request_<ContainerAllocator>>>;
  _request_type request;
  using _response_type =
    rosidl_runtime_cpp::BoundedVector<robot_localization::srv::ToLL_Response_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<robot_localization::srv::ToLL_Response_<ContainerAllocator>>>;
  _response_type response;

  // setters for named parameter idiom
  Type & set__info(
    const service_msgs::msg::ServiceEventInfo_<ContainerAllocator> & _arg)
  {
    this->info = _arg;
    return *this;
  }
  Type & set__request(
    const rosidl_runtime_cpp::BoundedVector<robot_localization::srv::ToLL_Request_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<robot_localization::srv::ToLL_Request_<ContainerAllocator>>> & _arg)
  {
    this->request = _arg;
    return *this;
  }
  Type & set__response(
    const rosidl_runtime_cpp::BoundedVector<robot_localization::srv::ToLL_Response_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<robot_localization::srv::ToLL_Response_<ContainerAllocator>>> & _arg)
  {
    this->response = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_localization::srv::ToLL_Event_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_localization::srv::ToLL_Event_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_localization::srv::ToLL_Event_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_localization::srv::ToLL_Event_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_localization::srv::ToLL_Event_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_localization::srv::ToLL_Event_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_localization::srv::ToLL_Event_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_localization::srv::ToLL_Event_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_localization::srv::ToLL_Event_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_localization::srv::ToLL_Event_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_localization__srv__ToLL_Event
    std::shared_ptr<robot_localization::srv::ToLL_Event_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_localization__srv__ToLL_Event
    std::shared_ptr<robot_localization::srv::ToLL_Event_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ToLL_Event_ & other) const
  {
    if (this->info != other.info) {
      return false;
    }
    if (this->request != other.request) {
      return false;
    }
    if (this->response != other.response) {
      return false;
    }
    return true;
  }
  bool operator!=(const ToLL_Event_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ToLL_Event_

// alias to use template instance with default allocator
using ToLL_Event =
  robot_localization::srv::ToLL_Event_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace robot_localization

namespace robot_localization
{

namespace srv
{

struct ToLL
{
  using Request = robot_localization::srv::ToLL_Request;
  using Response = robot_localization::srv::ToLL_Response;
  using Event = robot_localization::srv::ToLL_Event;
};

}  // namespace srv

}  // namespace robot_localization

#endif  // ROBOT_LOCALIZATION__SRV__DETAIL__TO_LL__STRUCT_HPP_
