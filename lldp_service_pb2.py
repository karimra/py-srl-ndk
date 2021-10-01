# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lldp_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sdk_common_pb2 as sdk__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lldp_service.proto',
  package='srlinux.sdk',
  syntax='proto3',
  serialized_options=b'Z\034nokia.com/srlinux/sdk/protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12lldp_service.proto\x12\x0bsrlinux.sdk\x1a\x10sdk_common.proto\"N\n\x1fLldpNeighborSubscriptionRequest\x12+\n\x03key\x18\x01 \x01(\x0b\x32\x1e.srlinux.sdk.LldpNeighborKeyPb\"\xb3\x02\n\x11LldpNeighborKeyPb\x12\x16\n\x0einterface_name\x18\x01 \x01(\t\x12\x12\n\nchassis_id\x18\x02 \x01(\t\x12\x42\n\x0c\x63hassis_type\x18\x03 \x01(\x0e\x32,.srlinux.sdk.LldpNeighborKeyPb.ChassisIdType\"\xad\x01\n\rChassisIdType\x12\x0c\n\x08RESERVED\x10\x00\x12\x15\n\x11\x43HASSIS_COMPONENT\x10\x01\x12\x13\n\x0fINTERFACE_ALIAS\x10\x02\x12\x12\n\x0ePORT_COMPONENT\x10\x03\x12\x0f\n\x0bMAC_ADDRESS\x10\x04\x12\x13\n\x0fNETWORK_ADDRESS\x10\x05\x12\x12\n\x0eINTERFACE_NAME\x10\x06\x12\x14\n\x10LOCALLY_ASSIGNED\x10\x07\"\xbc\x03\n\x12LldpNeighborDataPb\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12>\n\tport_type\x18\x02 \x01(\x0e\x32+.srlinux.sdk.LldpNeighborDataPb.PortSubType\x12-\n\nsource_mac\x18\x03 \x01(\x0b\x32\x19.srlinux.sdk.MacAddressPb\x12\x32\n\x10\x62gp_peer_address\x18\x04 \x03(\x0b\x32\x18.srlinux.sdk.IpAddressPb\x12\x14\n\x0c\x62gp_group_id\x18\x05 \x01(\r\x12\x13\n\x0bsystem_name\x18\x06 \x01(\t\x12\x1a\n\x12system_description\x18\x07 \x01(\t\"\xaa\x01\n\x0bPortSubType\x12\x0c\n\x08RESERVED\x10\x00\x12\x13\n\x0fINTERFACE_ALIAS\x10\x01\x12\x12\n\x0ePORT_COMPONENT\x10\x02\x12\x0f\n\x0bMAC_ADDRESS\x10\x03\x12\x13\n\x0fNETWORK_ADDRESS\x10\x04\x12\x12\n\x0eINTERFACE_NAME\x10\x05\x12\x14\n\x10\x41GENT_CIRCUIT_ID\x10\x06\x12\x14\n\x10LOCALLY_ASSIGNED\x10\x07\"\xa0\x01\n\x18LldpNeighborNotification\x12(\n\x02op\x18\x01 \x01(\x0e\x32\x1c.srlinux.sdk.SdkMgrOperation\x12+\n\x03key\x18\x02 \x01(\x0b\x32\x1e.srlinux.sdk.LldpNeighborKeyPb\x12-\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1f.srlinux.sdk.LldpNeighborDataPbB\x1eZ\x1cnokia.com/srlinux/sdk/protosb\x06proto3'
  ,
  dependencies=[sdk__common__pb2.DESCRIPTOR,])



_LLDPNEIGHBORKEYPB_CHASSISIDTYPE = _descriptor.EnumDescriptor(
  name='ChassisIdType',
  full_name='srlinux.sdk.LldpNeighborKeyPb.ChassisIdType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESERVED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHASSIS_COMPONENT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERFACE_ALIAS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PORT_COMPONENT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAC_ADDRESS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NETWORK_ADDRESS', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERFACE_NAME', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOCALLY_ASSIGNED', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=268,
  serialized_end=441,
)
_sym_db.RegisterEnumDescriptor(_LLDPNEIGHBORKEYPB_CHASSISIDTYPE)

_LLDPNEIGHBORDATAPB_PORTSUBTYPE = _descriptor.EnumDescriptor(
  name='PortSubType',
  full_name='srlinux.sdk.LldpNeighborDataPb.PortSubType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESERVED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERFACE_ALIAS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PORT_COMPONENT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAC_ADDRESS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NETWORK_ADDRESS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERFACE_NAME', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AGENT_CIRCUIT_ID', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOCALLY_ASSIGNED', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=718,
  serialized_end=888,
)
_sym_db.RegisterEnumDescriptor(_LLDPNEIGHBORDATAPB_PORTSUBTYPE)


_LLDPNEIGHBORSUBSCRIPTIONREQUEST = _descriptor.Descriptor(
  name='LldpNeighborSubscriptionRequest',
  full_name='srlinux.sdk.LldpNeighborSubscriptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='srlinux.sdk.LldpNeighborSubscriptionRequest.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=53,
  serialized_end=131,
)


_LLDPNEIGHBORKEYPB = _descriptor.Descriptor(
  name='LldpNeighborKeyPb',
  full_name='srlinux.sdk.LldpNeighborKeyPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='interface_name', full_name='srlinux.sdk.LldpNeighborKeyPb.interface_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chassis_id', full_name='srlinux.sdk.LldpNeighborKeyPb.chassis_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chassis_type', full_name='srlinux.sdk.LldpNeighborKeyPb.chassis_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LLDPNEIGHBORKEYPB_CHASSISIDTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=441,
)


_LLDPNEIGHBORDATAPB = _descriptor.Descriptor(
  name='LldpNeighborDataPb',
  full_name='srlinux.sdk.LldpNeighborDataPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='port_id', full_name='srlinux.sdk.LldpNeighborDataPb.port_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port_type', full_name='srlinux.sdk.LldpNeighborDataPb.port_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_mac', full_name='srlinux.sdk.LldpNeighborDataPb.source_mac', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bgp_peer_address', full_name='srlinux.sdk.LldpNeighborDataPb.bgp_peer_address', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bgp_group_id', full_name='srlinux.sdk.LldpNeighborDataPb.bgp_group_id', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='system_name', full_name='srlinux.sdk.LldpNeighborDataPb.system_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='system_description', full_name='srlinux.sdk.LldpNeighborDataPb.system_description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LLDPNEIGHBORDATAPB_PORTSUBTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=444,
  serialized_end=888,
)


_LLDPNEIGHBORNOTIFICATION = _descriptor.Descriptor(
  name='LldpNeighborNotification',
  full_name='srlinux.sdk.LldpNeighborNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='srlinux.sdk.LldpNeighborNotification.op', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='srlinux.sdk.LldpNeighborNotification.key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='srlinux.sdk.LldpNeighborNotification.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=891,
  serialized_end=1051,
)

_LLDPNEIGHBORSUBSCRIPTIONREQUEST.fields_by_name['key'].message_type = _LLDPNEIGHBORKEYPB
_LLDPNEIGHBORKEYPB.fields_by_name['chassis_type'].enum_type = _LLDPNEIGHBORKEYPB_CHASSISIDTYPE
_LLDPNEIGHBORKEYPB_CHASSISIDTYPE.containing_type = _LLDPNEIGHBORKEYPB
_LLDPNEIGHBORDATAPB.fields_by_name['port_type'].enum_type = _LLDPNEIGHBORDATAPB_PORTSUBTYPE
_LLDPNEIGHBORDATAPB.fields_by_name['source_mac'].message_type = sdk__common__pb2._MACADDRESSPB
_LLDPNEIGHBORDATAPB.fields_by_name['bgp_peer_address'].message_type = sdk__common__pb2._IPADDRESSPB
_LLDPNEIGHBORDATAPB_PORTSUBTYPE.containing_type = _LLDPNEIGHBORDATAPB
_LLDPNEIGHBORNOTIFICATION.fields_by_name['op'].enum_type = sdk__common__pb2._SDKMGROPERATION
_LLDPNEIGHBORNOTIFICATION.fields_by_name['key'].message_type = _LLDPNEIGHBORKEYPB
_LLDPNEIGHBORNOTIFICATION.fields_by_name['data'].message_type = _LLDPNEIGHBORDATAPB
DESCRIPTOR.message_types_by_name['LldpNeighborSubscriptionRequest'] = _LLDPNEIGHBORSUBSCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['LldpNeighborKeyPb'] = _LLDPNEIGHBORKEYPB
DESCRIPTOR.message_types_by_name['LldpNeighborDataPb'] = _LLDPNEIGHBORDATAPB
DESCRIPTOR.message_types_by_name['LldpNeighborNotification'] = _LLDPNEIGHBORNOTIFICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LldpNeighborSubscriptionRequest = _reflection.GeneratedProtocolMessageType('LldpNeighborSubscriptionRequest', (_message.Message,), {
  'DESCRIPTOR' : _LLDPNEIGHBORSUBSCRIPTIONREQUEST,
  '__module__' : 'lldp_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.LldpNeighborSubscriptionRequest)
  })
_sym_db.RegisterMessage(LldpNeighborSubscriptionRequest)

LldpNeighborKeyPb = _reflection.GeneratedProtocolMessageType('LldpNeighborKeyPb', (_message.Message,), {
  'DESCRIPTOR' : _LLDPNEIGHBORKEYPB,
  '__module__' : 'lldp_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.LldpNeighborKeyPb)
  })
_sym_db.RegisterMessage(LldpNeighborKeyPb)

LldpNeighborDataPb = _reflection.GeneratedProtocolMessageType('LldpNeighborDataPb', (_message.Message,), {
  'DESCRIPTOR' : _LLDPNEIGHBORDATAPB,
  '__module__' : 'lldp_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.LldpNeighborDataPb)
  })
_sym_db.RegisterMessage(LldpNeighborDataPb)

LldpNeighborNotification = _reflection.GeneratedProtocolMessageType('LldpNeighborNotification', (_message.Message,), {
  'DESCRIPTOR' : _LLDPNEIGHBORNOTIFICATION,
  '__module__' : 'lldp_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.LldpNeighborNotification)
  })
_sym_db.RegisterMessage(LldpNeighborNotification)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
