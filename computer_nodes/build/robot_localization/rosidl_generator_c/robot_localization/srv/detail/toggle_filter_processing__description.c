// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from robot_localization:srv/ToggleFilterProcessing.idl
// generated code does not contain a copyright notice

#include "robot_localization/srv/detail/toggle_filter_processing__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_robot_localization
const rosidl_type_hash_t *
robot_localization__srv__ToggleFilterProcessing__get_type_hash(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xa3, 0x94, 0xa6, 0xdb, 0x1a, 0x24, 0x13, 0xcb,
      0x92, 0xe9, 0x31, 0xeb, 0xe5, 0x9d, 0xa8, 0x53,
      0x98, 0x90, 0x9e, 0x7f, 0x8a, 0x31, 0x7e, 0x7c,
      0xd4, 0xc8, 0xaa, 0xa3, 0xd7, 0x36, 0x51, 0x7e,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_robot_localization
const rosidl_type_hash_t *
robot_localization__srv__ToggleFilterProcessing_Request__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xdf, 0x1a, 0xac, 0xf0, 0x9e, 0x10, 0x01, 0xc2,
      0x98, 0x14, 0x5b, 0x29, 0x31, 0x58, 0x6c, 0x0e,
      0xad, 0x38, 0x39, 0xf3, 0xce, 0x98, 0x6d, 0x48,
      0x63, 0x01, 0xcc, 0x98, 0x74, 0xe9, 0x85, 0x38,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_robot_localization
const rosidl_type_hash_t *
robot_localization__srv__ToggleFilterProcessing_Response__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x0a, 0x60, 0xa1, 0x65, 0x6f, 0x11, 0x4f, 0xfa,
      0xf5, 0xe7, 0xa1, 0x7b, 0x2d, 0x43, 0x38, 0x47,
      0x42, 0xb0, 0x02, 0x64, 0x75, 0xa5, 0xb0, 0x07,
      0xfe, 0x4e, 0x33, 0x38, 0x77, 0xb2, 0xed, 0xcb,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_robot_localization
const rosidl_type_hash_t *
robot_localization__srv__ToggleFilterProcessing_Event__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x4d, 0x8f, 0x53, 0xcd, 0x5b, 0xd7, 0xd4, 0x7e,
      0x0b, 0xa5, 0xdb, 0xba, 0x7c, 0x21, 0xba, 0x55,
      0x50, 0x1d, 0x5a, 0x01, 0xef, 0x18, 0x16, 0x92,
      0xd2, 0xe6, 0xb7, 0xc0, 0x45, 0xe0, 0x40, 0xdf,
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

static char robot_localization__srv__ToggleFilterProcessing__TYPE_NAME[] = "robot_localization/srv/ToggleFilterProcessing";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char robot_localization__srv__ToggleFilterProcessing_Event__TYPE_NAME[] = "robot_localization/srv/ToggleFilterProcessing_Event";
static char robot_localization__srv__ToggleFilterProcessing_Request__TYPE_NAME[] = "robot_localization/srv/ToggleFilterProcessing_Request";
static char robot_localization__srv__ToggleFilterProcessing_Response__TYPE_NAME[] = "robot_localization/srv/ToggleFilterProcessing_Response";
static char service_msgs__msg__ServiceEventInfo__TYPE_NAME[] = "service_msgs/msg/ServiceEventInfo";

// Define type names, field names, and default values
static char robot_localization__srv__ToggleFilterProcessing__FIELD_NAME__request_message[] = "request_message";
static char robot_localization__srv__ToggleFilterProcessing__FIELD_NAME__response_message[] = "response_message";
static char robot_localization__srv__ToggleFilterProcessing__FIELD_NAME__event_message[] = "event_message";

static rosidl_runtime_c__type_description__Field robot_localization__srv__ToggleFilterProcessing__FIELDS[] = {
  {
    {robot_localization__srv__ToggleFilterProcessing__FIELD_NAME__request_message, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {robot_localization__srv__ToggleFilterProcessing_Request__TYPE_NAME, 53, 53},
    },
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__ToggleFilterProcessing__FIELD_NAME__response_message, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {robot_localization__srv__ToggleFilterProcessing_Response__TYPE_NAME, 54, 54},
    },
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__ToggleFilterProcessing__FIELD_NAME__event_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {robot_localization__srv__ToggleFilterProcessing_Event__TYPE_NAME, 51, 51},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription robot_localization__srv__ToggleFilterProcessing__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__ToggleFilterProcessing_Event__TYPE_NAME, 51, 51},
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__ToggleFilterProcessing_Request__TYPE_NAME, 53, 53},
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__ToggleFilterProcessing_Response__TYPE_NAME, 54, 54},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
robot_localization__srv__ToggleFilterProcessing__get_type_description(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {robot_localization__srv__ToggleFilterProcessing__TYPE_NAME, 45, 45},
      {robot_localization__srv__ToggleFilterProcessing__FIELDS, 3, 3},
    },
    {robot_localization__srv__ToggleFilterProcessing__REFERENCED_TYPE_DESCRIPTIONS, 5, 5},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = robot_localization__srv__ToggleFilterProcessing_Event__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = robot_localization__srv__ToggleFilterProcessing_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = robot_localization__srv__ToggleFilterProcessing_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[4].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char robot_localization__srv__ToggleFilterProcessing_Request__FIELD_NAME__on[] = "on";

static rosidl_runtime_c__type_description__Field robot_localization__srv__ToggleFilterProcessing_Request__FIELDS[] = {
  {
    {robot_localization__srv__ToggleFilterProcessing_Request__FIELD_NAME__on, 2, 2},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
robot_localization__srv__ToggleFilterProcessing_Request__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {robot_localization__srv__ToggleFilterProcessing_Request__TYPE_NAME, 53, 53},
      {robot_localization__srv__ToggleFilterProcessing_Request__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char robot_localization__srv__ToggleFilterProcessing_Response__FIELD_NAME__status[] = "status";

static rosidl_runtime_c__type_description__Field robot_localization__srv__ToggleFilterProcessing_Response__FIELDS[] = {
  {
    {robot_localization__srv__ToggleFilterProcessing_Response__FIELD_NAME__status, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
robot_localization__srv__ToggleFilterProcessing_Response__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {robot_localization__srv__ToggleFilterProcessing_Response__TYPE_NAME, 54, 54},
      {robot_localization__srv__ToggleFilterProcessing_Response__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char robot_localization__srv__ToggleFilterProcessing_Event__FIELD_NAME__info[] = "info";
static char robot_localization__srv__ToggleFilterProcessing_Event__FIELD_NAME__request[] = "request";
static char robot_localization__srv__ToggleFilterProcessing_Event__FIELD_NAME__response[] = "response";

static rosidl_runtime_c__type_description__Field robot_localization__srv__ToggleFilterProcessing_Event__FIELDS[] = {
  {
    {robot_localization__srv__ToggleFilterProcessing_Event__FIELD_NAME__info, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__ToggleFilterProcessing_Event__FIELD_NAME__request, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {robot_localization__srv__ToggleFilterProcessing_Request__TYPE_NAME, 53, 53},
    },
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__ToggleFilterProcessing_Event__FIELD_NAME__response, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {robot_localization__srv__ToggleFilterProcessing_Response__TYPE_NAME, 54, 54},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription robot_localization__srv__ToggleFilterProcessing_Event__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__ToggleFilterProcessing_Request__TYPE_NAME, 53, 53},
    {NULL, 0, 0},
  },
  {
    {robot_localization__srv__ToggleFilterProcessing_Response__TYPE_NAME, 54, 54},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
robot_localization__srv__ToggleFilterProcessing_Event__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {robot_localization__srv__ToggleFilterProcessing_Event__TYPE_NAME, 51, 51},
      {robot_localization__srv__ToggleFilterProcessing_Event__FIELDS, 3, 3},
    },
    {robot_localization__srv__ToggleFilterProcessing_Event__REFERENCED_TYPE_DESCRIPTIONS, 4, 4},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = robot_localization__srv__ToggleFilterProcessing_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = robot_localization__srv__ToggleFilterProcessing_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[3].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "bool on\n"
  "---\n"
  "bool status";

static char srv_encoding[] = "srv";
static char implicit_encoding[] = "implicit";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
robot_localization__srv__ToggleFilterProcessing__get_individual_type_description_source(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {robot_localization__srv__ToggleFilterProcessing__TYPE_NAME, 45, 45},
    {srv_encoding, 3, 3},
    {toplevel_type_raw_source, 24, 24},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
robot_localization__srv__ToggleFilterProcessing_Request__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {robot_localization__srv__ToggleFilterProcessing_Request__TYPE_NAME, 53, 53},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
robot_localization__srv__ToggleFilterProcessing_Response__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {robot_localization__srv__ToggleFilterProcessing_Response__TYPE_NAME, 54, 54},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
robot_localization__srv__ToggleFilterProcessing_Event__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {robot_localization__srv__ToggleFilterProcessing_Event__TYPE_NAME, 51, 51},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
robot_localization__srv__ToggleFilterProcessing__get_type_description_sources(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[6];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 6, 6};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *robot_localization__srv__ToggleFilterProcessing__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *robot_localization__srv__ToggleFilterProcessing_Event__get_individual_type_description_source(NULL);
    sources[3] = *robot_localization__srv__ToggleFilterProcessing_Request__get_individual_type_description_source(NULL);
    sources[4] = *robot_localization__srv__ToggleFilterProcessing_Response__get_individual_type_description_source(NULL);
    sources[5] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
robot_localization__srv__ToggleFilterProcessing_Request__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *robot_localization__srv__ToggleFilterProcessing_Request__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
robot_localization__srv__ToggleFilterProcessing_Response__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *robot_localization__srv__ToggleFilterProcessing_Response__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
robot_localization__srv__ToggleFilterProcessing_Event__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[5];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 5, 5};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *robot_localization__srv__ToggleFilterProcessing_Event__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *robot_localization__srv__ToggleFilterProcessing_Request__get_individual_type_description_source(NULL);
    sources[3] = *robot_localization__srv__ToggleFilterProcessing_Response__get_individual_type_description_source(NULL);
    sources[4] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
