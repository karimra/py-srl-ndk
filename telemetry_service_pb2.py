# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: telemetry_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sdk_common_pb2 as sdk__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='telemetry_service.proto',
  package='srlinux.sdk',
  syntax='proto3',
  serialized_options=b'Z\034nokia.com/srlinux/sdk/protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17telemetry_service.proto\x12\x0bsrlinux.sdk\x1a\x10sdk_common.proto\"\x1f\n\x0cTelemetryKey\x12\x0f\n\x07js_path\x18\x01 \x01(\t\"%\n\rTelemetryData\x12\x14\n\x0cjson_content\x18\x01 \x01(\t\"a\n\rTelemetryInfo\x12&\n\x03key\x18\x01 \x01(\x0b\x32\x19.srlinux.sdk.TelemetryKey\x12(\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1a.srlinux.sdk.TelemetryData\"C\n\x16TelemetryUpdateRequest\x12)\n\x05state\x18\x01 \x03(\x0b\x32\x1a.srlinux.sdk.TelemetryInfo\"W\n\x17TelemetryUpdateResponse\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.srlinux.sdk.SdkMgrStatus\x12\x11\n\terror_str\x18\x02 \x01(\t\"@\n\x16TelemetryDeleteRequest\x12&\n\x03key\x18\x01 \x03(\x0b\x32\x19.srlinux.sdk.TelemetryKey\"W\n\x17TelemetryDeleteResponse\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.srlinux.sdk.SdkMgrStatus\x12\x11\n\terror_str\x18\x02 \x01(\t2\xdd\x01\n\x16SdkMgrTelemetryService\x12\x63\n\x14TelemetryAddOrUpdate\x12#.srlinux.sdk.TelemetryUpdateRequest\x1a$.srlinux.sdk.TelemetryUpdateResponse\"\x00\x12^\n\x0fTelemetryDelete\x12#.srlinux.sdk.TelemetryDeleteRequest\x1a$.srlinux.sdk.TelemetryDeleteResponse\"\x00\x42\x1eZ\x1cnokia.com/srlinux/sdk/protosb\x06proto3'
  ,
  dependencies=[sdk__common__pb2.DESCRIPTOR,])




_TELEMETRYKEY = _descriptor.Descriptor(
  name='TelemetryKey',
  full_name='srlinux.sdk.TelemetryKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='js_path', full_name='srlinux.sdk.TelemetryKey.js_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=89,
)


_TELEMETRYDATA = _descriptor.Descriptor(
  name='TelemetryData',
  full_name='srlinux.sdk.TelemetryData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='json_content', full_name='srlinux.sdk.TelemetryData.json_content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=128,
)


_TELEMETRYINFO = _descriptor.Descriptor(
  name='TelemetryInfo',
  full_name='srlinux.sdk.TelemetryInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='srlinux.sdk.TelemetryInfo.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='srlinux.sdk.TelemetryInfo.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=227,
)


_TELEMETRYUPDATEREQUEST = _descriptor.Descriptor(
  name='TelemetryUpdateRequest',
  full_name='srlinux.sdk.TelemetryUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='srlinux.sdk.TelemetryUpdateRequest.state', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=296,
)


_TELEMETRYUPDATERESPONSE = _descriptor.Descriptor(
  name='TelemetryUpdateResponse',
  full_name='srlinux.sdk.TelemetryUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='srlinux.sdk.TelemetryUpdateResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_str', full_name='srlinux.sdk.TelemetryUpdateResponse.error_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=385,
)


_TELEMETRYDELETEREQUEST = _descriptor.Descriptor(
  name='TelemetryDeleteRequest',
  full_name='srlinux.sdk.TelemetryDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='srlinux.sdk.TelemetryDeleteRequest.key', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=387,
  serialized_end=451,
)


_TELEMETRYDELETERESPONSE = _descriptor.Descriptor(
  name='TelemetryDeleteResponse',
  full_name='srlinux.sdk.TelemetryDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='srlinux.sdk.TelemetryDeleteResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_str', full_name='srlinux.sdk.TelemetryDeleteResponse.error_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=453,
  serialized_end=540,
)

_TELEMETRYINFO.fields_by_name['key'].message_type = _TELEMETRYKEY
_TELEMETRYINFO.fields_by_name['data'].message_type = _TELEMETRYDATA
_TELEMETRYUPDATEREQUEST.fields_by_name['state'].message_type = _TELEMETRYINFO
_TELEMETRYUPDATERESPONSE.fields_by_name['status'].enum_type = sdk__common__pb2._SDKMGRSTATUS
_TELEMETRYDELETEREQUEST.fields_by_name['key'].message_type = _TELEMETRYKEY
_TELEMETRYDELETERESPONSE.fields_by_name['status'].enum_type = sdk__common__pb2._SDKMGRSTATUS
DESCRIPTOR.message_types_by_name['TelemetryKey'] = _TELEMETRYKEY
DESCRIPTOR.message_types_by_name['TelemetryData'] = _TELEMETRYDATA
DESCRIPTOR.message_types_by_name['TelemetryInfo'] = _TELEMETRYINFO
DESCRIPTOR.message_types_by_name['TelemetryUpdateRequest'] = _TELEMETRYUPDATEREQUEST
DESCRIPTOR.message_types_by_name['TelemetryUpdateResponse'] = _TELEMETRYUPDATERESPONSE
DESCRIPTOR.message_types_by_name['TelemetryDeleteRequest'] = _TELEMETRYDELETEREQUEST
DESCRIPTOR.message_types_by_name['TelemetryDeleteResponse'] = _TELEMETRYDELETERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TelemetryKey = _reflection.GeneratedProtocolMessageType('TelemetryKey', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYKEY,
  '__module__' : 'telemetry_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.TelemetryKey)
  })
_sym_db.RegisterMessage(TelemetryKey)

TelemetryData = _reflection.GeneratedProtocolMessageType('TelemetryData', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYDATA,
  '__module__' : 'telemetry_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.TelemetryData)
  })
_sym_db.RegisterMessage(TelemetryData)

TelemetryInfo = _reflection.GeneratedProtocolMessageType('TelemetryInfo', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYINFO,
  '__module__' : 'telemetry_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.TelemetryInfo)
  })
_sym_db.RegisterMessage(TelemetryInfo)

TelemetryUpdateRequest = _reflection.GeneratedProtocolMessageType('TelemetryUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYUPDATEREQUEST,
  '__module__' : 'telemetry_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.TelemetryUpdateRequest)
  })
_sym_db.RegisterMessage(TelemetryUpdateRequest)

TelemetryUpdateResponse = _reflection.GeneratedProtocolMessageType('TelemetryUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYUPDATERESPONSE,
  '__module__' : 'telemetry_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.TelemetryUpdateResponse)
  })
_sym_db.RegisterMessage(TelemetryUpdateResponse)

TelemetryDeleteRequest = _reflection.GeneratedProtocolMessageType('TelemetryDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYDELETEREQUEST,
  '__module__' : 'telemetry_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.TelemetryDeleteRequest)
  })
_sym_db.RegisterMessage(TelemetryDeleteRequest)

TelemetryDeleteResponse = _reflection.GeneratedProtocolMessageType('TelemetryDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYDELETERESPONSE,
  '__module__' : 'telemetry_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.TelemetryDeleteResponse)
  })
_sym_db.RegisterMessage(TelemetryDeleteResponse)


DESCRIPTOR._options = None

_SDKMGRTELEMETRYSERVICE = _descriptor.ServiceDescriptor(
  name='SdkMgrTelemetryService',
  full_name='srlinux.sdk.SdkMgrTelemetryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=543,
  serialized_end=764,
  methods=[
  _descriptor.MethodDescriptor(
    name='TelemetryAddOrUpdate',
    full_name='srlinux.sdk.SdkMgrTelemetryService.TelemetryAddOrUpdate',
    index=0,
    containing_service=None,
    input_type=_TELEMETRYUPDATEREQUEST,
    output_type=_TELEMETRYUPDATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TelemetryDelete',
    full_name='srlinux.sdk.SdkMgrTelemetryService.TelemetryDelete',
    index=1,
    containing_service=None,
    input_type=_TELEMETRYDELETEREQUEST,
    output_type=_TELEMETRYDELETERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SDKMGRTELEMETRYSERVICE)

DESCRIPTOR.services_by_name['SdkMgrTelemetryService'] = _SDKMGRTELEMETRYSERVICE

# @@protoc_insertion_point(module_scope)
