# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: log_logs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='log_logs.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0elog_logs.proto\"Z\n\x03Log\x12\x0c\n\x04Time\x18\x01 \x02(\r\x12\x1e\n\x08\x43ontents\x18\x02 \x03(\x0b\x32\x0c.Log.Content\x1a%\n\x07\x43ontent\x12\x0b\n\x03Key\x18\x01 \x02(\t\x12\r\n\x05Value\x18\x02 \x02(\t\"O\n\x08LogGroup\x12\x12\n\x04Logs\x18\x01 \x03(\x0b\x32\x04.Log\x12\x10\n\x08Reserved\x18\x02 \x01(\t\x12\r\n\x05Topic\x18\x03 \x01(\t\x12\x0e\n\x06Source\x18\x04 \x01(\t\",\n\x0cLogGroupList\x12\x1c\n\tLogGroups\x18\x01 \x03(\x0b\x32\t.LogGroup')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LOG_CONTENT = _descriptor.Descriptor(
  name='Content',
  full_name='Log.Content',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Key', full_name='Log.Content.Key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Value', full_name='Log.Content.Value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=108,
)

_LOG = _descriptor.Descriptor(
  name='Log',
  full_name='Log',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Time', full_name='Log.Time', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Contents', full_name='Log.Contents', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_LOG_CONTENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=108,
)


_LOGGROUP = _descriptor.Descriptor(
  name='LogGroup',
  full_name='LogGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Logs', full_name='LogGroup.Logs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Reserved', full_name='LogGroup.Reserved', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Topic', full_name='LogGroup.Topic', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Source', full_name='LogGroup.Source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=189,
)


_LOGGROUPLIST = _descriptor.Descriptor(
  name='LogGroupList',
  full_name='LogGroupList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='LogGroups', full_name='LogGroupList.LogGroups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=235,
)

_LOG_CONTENT.containing_type = _LOG
_LOG.fields_by_name['Contents'].message_type = _LOG_CONTENT
_LOGGROUP.fields_by_name['Logs'].message_type = _LOG
_LOGGROUPLIST.fields_by_name['LogGroups'].message_type = _LOGGROUP
DESCRIPTOR.message_types_by_name['Log'] = _LOG
DESCRIPTOR.message_types_by_name['LogGroup'] = _LOGGROUP
DESCRIPTOR.message_types_by_name['LogGroupList'] = _LOGGROUPLIST

Log = _reflection.GeneratedProtocolMessageType('Log', (_message.Message,), dict(

  Content = _reflection.GeneratedProtocolMessageType('Content', (_message.Message,), dict(
    DESCRIPTOR = _LOG_CONTENT,
    __module__ = 'log_logs_pb2'
    # @@protoc_insertion_point(class_scope:Log.Content)
    ))
  ,
  DESCRIPTOR = _LOG,
  __module__ = 'log_logs_pb2'
  # @@protoc_insertion_point(class_scope:Log)
  ))
_sym_db.RegisterMessage(Log)
_sym_db.RegisterMessage(Log.Content)

LogGroup = _reflection.GeneratedProtocolMessageType('LogGroup', (_message.Message,), dict(
  DESCRIPTOR = _LOGGROUP,
  __module__ = 'log_logs_pb2'
  # @@protoc_insertion_point(class_scope:LogGroup)
  ))
_sym_db.RegisterMessage(LogGroup)

LogGroupList = _reflection.GeneratedProtocolMessageType('LogGroupList', (_message.Message,), dict(
  DESCRIPTOR = _LOGGROUPLIST,
  __module__ = 'log_logs_pb2'
  # @@protoc_insertion_point(class_scope:LogGroupList)
  ))
_sym_db.RegisterMessage(LogGroupList)


# @@protoc_insertion_point(module_scope)
