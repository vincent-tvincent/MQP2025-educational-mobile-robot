// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from robot_localization:srv/GetState.idl
// generated code does not contain a copyright notice

#include "robot_localization/srv/detail/get_state__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_robot_localization
const rosidl_type_hash_t *
robot_localization__srv__GetState__get_type_hash(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xd8, 0x96, 0xcc, 0x7d, 0xc7, 0x5f, 0x25, 0x5f,
      0x3f, 0x04, 0xdf, 0xc2, 0xfd, 0xeb, 0xe3, 0xae,
      0x87, 0x4a, 0x49, 0xb0, 0x02, 0xd0, 0xbe, 0xcf,
      0x66, 0x29, 0x1b, 0x46, 0x85, 0x54, 0x8b, 0xc7,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_robot_localization
const rosidl_type_hash_t *
robot_localization__srv__GetState_Request__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xdb, 0x2f, 0x94, 0x35, 0xb3, 0xc0, 0x33, 0x38,
      0x84, 0x11, 0x28, 0x98, 0x7f, 0x0b, 0xf0, 0x98,
      0xa6, 0xd7, 0xc7, 0x38, 0x80, 0x16, 0x47, 0xbc,
      0xc4, 0x79, 0x79, 0x59, 0x7d, 0xa5, 0x39, 0x39,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_robot_localization
const rosidl_type_hash_t *
robot_localization__srv__GetState_Response__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xc3, 0x5a, 0x19, 0x39, 0x5f, 0xa7, 0xf0, 0xed,
      0x44, 0x57, 0xfa, 0xfd, 0xa2, 0xdd, 0xf6, 0x61,
      0xe2, 0x61, 0x6c, 0xac, 0xec, 0x4d, 0xd3, 0x0c,
      0x3d, 0x1f, 0xcd, 0xea, 0xb2, 0x1f, 0xd6, 0x0e,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_robot_localization
const rosidl_type_hash_t *
robot_localization__srv__GetState_Event__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x98, 0xa7, 0xfb, 0x53, 0xb7, 0x9d, 0xb5, 0xab,
      0x90, 0xe1, 0x69, 0x99, 0x60, 0x9b, 0xa9, 0xe4,
      0xc1, 0xa0, 0x0c, 0xcc, 0xbc, 0x84, 0x22, 0x19,
      0x42, 0x68, 0x97, 0xfb, 0x62, 0x24, 0xa8, 0xa9,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"
#include "service_msgs/msg/detail/service_event_info__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t service_msgs__msg__ServiceEventInfo__EXPECTED_HASH = {1, {
    0x41, 0xbc, 0xbb, 0xe0, 0x7a, 0x75, 0xc9, 0xb5,
    0x2b, 0xc9, 0x6b, 0xfd, 0x5c, 0x24, 0xd7, 0xf0,
    0xfc, 0x0a, 0x08, 0xc0, 0xcb, 0x79, 0x21, 0xb3,
    0x37, 0x3c, 0x57, 0x32, 0x34, 0x5a, 0x6f, 0x45,
  }};
#endif

static char robot_localization__srv__GetState__TYPE_NAME[] = "robot_localization/srv/GetState";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char robot_localization__srv__GetState_Event__TYPE_NAME[] = "robot_localization/srv/GetState_Event";
static char robot_localization__srv__GetState_Request__TYPE_NAME[] = "robot_localization/srv/GetState_Request";
static char robot_localization__srv__GetState_Response__TYPE_NAME[] = "robot_localization/srv/GetState_Response";
static char service_msgs__msg__ServiceEventInfo__TYPE_NAME[] = "service_msgs/msg/ServiceEventInfo";

// Define type names, field names, and default values
static char robot_localization__srv__GetState__FIELD_NAME__request_message[] = "request_message";
static char robot_localization__srv__GetState__FIELD_NAME__response_message[] = "response_message";
static char robot_localization__srv__GetState__FIELD_NAME__event_message[] = "event_message";

static rosidl_runtime_c__type_description__Field robot_localization__srv__GetState__FIELDS[] = {
  {
    {robot_localization__srv__GetState__FIELD_NAME__request_message, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {robot_localization__srv__GetState_Request__TYPE_NAME, 39, 39},
    },
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__GetState__FIELD_NAME__response_message, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {robot_localization__srv__GetState_Response__TYPE_NAME, 40, 40},
    },
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__GetState__FIELD_NAME__event_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {robot_localization__srv__GetState_Event__TYPE_NAME, 37, 37},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription robot_localization__srv__GetState__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__GetState_Event__TYPE_NAME, 37, 37},
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__GetState_Request__TYPE_NAME, 39, 39},
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__GetState_Response__TYPE_NAME, 40, 40},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
robot_localization__srv__GetState__get_type_description(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {robot_localization__srv__GetState__TYPE_NAME, 31, 31},
      {robot_localization__srv__GetState__FIELDS, 3, 3},
    },
    {robot_localization__srv__GetState__REFERENCED_TYPE_DESCRIPTIONS, 5, 5},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = robot_localization__srv__GetState_Event__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = robot_localization__srv__GetState_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = robot_localization__srv__GetState_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[4].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char robot_localization__srv__GetState_Request__FIELD_NAME__time_stamp[] = "time_stamp";
static char robot_localization__srv__GetState_Request__FIELD_NAME__frame_id[] = "frame_id";

static rosidl_runtime_c__type_description__Field robot_localization__srv__GetState_Request__FIELDS[] = {
  {
    {robot_localization__srv__GetState_Request__FIELD_NAME__time_stamp, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    },
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__GetState_Request__FIELD_NAME__frame_id, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription robot_localization__srv__GetState_Request__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
robot_localization__srv__GetState_Request__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {robot_localization__srv__GetState_Request__TYPE_NAME, 39, 39},
      {robot_localization__srv__GetState_Request__FIELDS, 2, 2},
    },
    {robot_localization__srv__GetState_Request__REFERENCED_TYPE_DESCRIPTIONS, 1, 1},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char robot_localization__srv__GetState_Response__FIELD_NAME__state[] = "state";
static char robot_localization__srv__GetState_Response__FIELD_NAME__covariance[] = "covariance";

static rosidl_runtime_c__type_description__Field robot_localization__srv__GetState_Response__FIELDS[] = {
  {
    {robot_localization__srv__GetState_Response__FIELD_NAME__state, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE_ARRAY,
      15,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__GetState_Response__FIELD_NAME__covariance, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE_ARRAY,
      225,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
robot_localization__srv__GetState_Response__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {robot_localization__srv__GetState_Response__TYPE_NAME, 40, 40},
      {robot_localization__srv__GetState_Response__FIELDS, 2, 2},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char robot_localization__srv__GetState_Event__FIELD_NAME__info[] = "info";
static char robot_localization__srv__GetState_Event__FIELD_NAME__request[] = "request";
static char robot_localization__srv__GetState_Event__FIELD_NAME__response[] = "response";

static rosidl_runtime_c__type_description__Field robot_localization__srv__GetState_Event__FIELDS[] = {
  {
    {robot_localization__srv__GetState_Event__FIELD_NAME__info, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__GetState_Event__FIELD_NAME__request, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {robot_localization__srv__GetState_Request__TYPE_NAME, 39, 39},
    },
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__GetState_Event__FIELD_NAME__response, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {robot_localization__srv__GetState_Response__TYPE_NAME, 40, 40},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription robot_localization__srv__GetState_Event__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__GetState_Request__TYPE_NAME, 39, 39},
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__GetState_Response__TYPE_NAME, 40, 40},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
robot_localization__srv__GetState_Event__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {robot_localization__srv__GetState_Event__TYPE_NAME, 37, 37},
      {robot_localization__srv__GetState_Event__FIELDS, 3, 3},
    },
    {robot_localization__srv__GetState_Event__REFERENCED_TYPE_DESCRIPTIONS, 4, 4},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = robot_localization__srv__GetState_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = robot_localization__srv__GetState_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[3].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "builtin_interfaces/Time time_stamp\n"
  "string frame_id\n"
  "---\n"
  "# State vector: x, y, z, roll, pitch, yaw, vx, vy, vz, vroll, vpitch, vyaw, ax, ay, az\n"
  "float64[15] state\n"
  "\n"
  "# Covariance matrix in row-major order\n"
  "float64[225] covariance";

static char srv_encoding[] = "srv";
static char implicit_encoding[] = "implicit";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
robot_localization__srv__GetState__get_individual_type_description_source(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {robot_localization__srv__GetState__TYPE_NAME, 31, 31},
    {srv_encoding, 3, 3},
    {toplevel_type_raw_source, 224, 224},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
robot_localization__srv__GetState_Request__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {robot_localization__srv__GetState_Request__TYPE_NAME, 39, 39},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
robot_localization__srv__GetState_Response__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {robot_localization__srv__GetState_Response__TYPE_NAME, 40, 40},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
robot_localization__srv__GetState_Event__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {robot_localization__srv__GetState_Event__TYPE_NAME, 37, 37},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
robot_localization__srv__GetState__get_type_description_sources(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[6];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 6, 6};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *robot_localization__srv__GetState__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *robot_localization__srv__GetState_Event__get_individual_type_description_source(NULL);
    sources[3] = *robot_localization__srv__GetState_Request__get_individual_type_description_source(NULL);
    sources[4] = *robot_localization__srv__GetState_Response__get_individual_type_description_source(NULL);
    sources[5] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
robot_localization__srv__GetState_Request__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[2];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 2, 2};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *robot_localization__srv__GetState_Request__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
robot_localization__srv__GetState_Response__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *robot_localization__srv__GetState_Response__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
robot_localization__srv__GetState_Event__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[5];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 5, 5};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *robot_localization__srv__GetState_Event__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *robot_localization__srv__GetState_Request__get_individual_type_description_source(NULL);
    sources[3] = *robot_localization__srv__GetState_Response__get_individual_type_description_source(NULL);
    sources[4] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
