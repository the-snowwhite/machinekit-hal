# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: machinetalk/protobuf/nanopb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='machinetalk/protobuf/nanopb.proto',
  package='',
  syntax='proto2',
  serialized_options=_b('\n\030fi.kapsi.koti.jpa.nanopb'),
  serialized_pb=_b('\n!machinetalk/protobuf/nanopb.proto\x1a google/protobuf/descriptor.proto\"\x80\x02\n\rNanoPBOptions\x12\x10\n\x08max_size\x18\x01 \x01(\x05\x12\x11\n\tmax_count\x18\x02 \x01(\x05\x12&\n\x08int_size\x18\x07 \x01(\x0e\x32\x08.IntSize:\nIS_DEFAULT\x12$\n\x04type\x18\x03 \x01(\x0e\x32\n.FieldType:\nFT_DEFAULT\x12\x18\n\nlong_names\x18\x04 \x01(\x08:\x04true\x12\x1c\n\rpacked_struct\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x0cskip_message\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x18\n\tno_unions\x18\x08 \x01(\x08:\x05\x66\x61lse\x12\r\n\x05msgid\x18\t \x01(\r*Z\n\tFieldType\x12\x0e\n\nFT_DEFAULT\x10\x00\x12\x0f\n\x0b\x46T_CALLBACK\x10\x01\x12\x0e\n\nFT_POINTER\x10\x04\x12\r\n\tFT_STATIC\x10\x02\x12\r\n\tFT_IGNORE\x10\x03*D\n\x07IntSize\x12\x0e\n\nIS_DEFAULT\x10\x00\x12\x08\n\x04IS_8\x10\x08\x12\t\n\x05IS_16\x10\x10\x12\t\n\x05IS_32\x10 \x12\t\n\x05IS_64\x10@:E\n\x0enanopb_fileopt\x12\x1c.google.protobuf.FileOptions\x18\xf2\x07 \x01(\x0b\x32\x0e.NanoPBOptions:G\n\rnanopb_msgopt\x12\x1f.google.protobuf.MessageOptions\x18\xf2\x07 \x01(\x0b\x32\x0e.NanoPBOptions:E\n\x0enanopb_enumopt\x12\x1c.google.protobuf.EnumOptions\x18\xf2\x07 \x01(\x0b\x32\x0e.NanoPBOptions:>\n\x06nanopb\x12\x1d.google.protobuf.FieldOptions\x18\xf2\x07 \x01(\x0b\x32\x0e.NanoPBOptionsB\x1a\n\x18\x66i.kapsi.koti.jpa.nanopb')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_FIELDTYPE = _descriptor.EnumDescriptor(
  name='FieldType',
  full_name='FieldType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FT_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_CALLBACK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_POINTER', index=2, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_STATIC', index=3, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_IGNORE', index=4, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=330,
  serialized_end=420,
)
_sym_db.RegisterEnumDescriptor(_FIELDTYPE)

FieldType = enum_type_wrapper.EnumTypeWrapper(_FIELDTYPE)
_INTSIZE = _descriptor.EnumDescriptor(
  name='IntSize',
  full_name='IntSize',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IS_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_8', index=1, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_16', index=2, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_32', index=3, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_64', index=4, number=64,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=422,
  serialized_end=490,
)
_sym_db.RegisterEnumDescriptor(_INTSIZE)

IntSize = enum_type_wrapper.EnumTypeWrapper(_INTSIZE)
FT_DEFAULT = 0
FT_CALLBACK = 1
FT_POINTER = 4
FT_STATIC = 2
FT_IGNORE = 3
IS_DEFAULT = 0
IS_8 = 8
IS_16 = 16
IS_32 = 32
IS_64 = 64

NANOPB_FILEOPT_FIELD_NUMBER = 1010
nanopb_fileopt = _descriptor.FieldDescriptor(
  name='nanopb_fileopt', full_name='nanopb_fileopt', index=0,
  number=1010, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
NANOPB_MSGOPT_FIELD_NUMBER = 1010
nanopb_msgopt = _descriptor.FieldDescriptor(
  name='nanopb_msgopt', full_name='nanopb_msgopt', index=1,
  number=1010, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
NANOPB_ENUMOPT_FIELD_NUMBER = 1010
nanopb_enumopt = _descriptor.FieldDescriptor(
  name='nanopb_enumopt', full_name='nanopb_enumopt', index=2,
  number=1010, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
NANOPB_FIELD_NUMBER = 1010
nanopb = _descriptor.FieldDescriptor(
  name='nanopb', full_name='nanopb', index=3,
  number=1010, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)


_NANOPBOPTIONS = _descriptor.Descriptor(
  name='NanoPBOptions',
  full_name='NanoPBOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_size', full_name='NanoPBOptions.max_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_count', full_name='NanoPBOptions.max_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_size', full_name='NanoPBOptions.int_size', index=2,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='NanoPBOptions.type', index=3,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_names', full_name='NanoPBOptions.long_names', index=4,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packed_struct', full_name='NanoPBOptions.packed_struct', index=5,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skip_message', full_name='NanoPBOptions.skip_message', index=6,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_unions', full_name='NanoPBOptions.no_unions', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msgid', full_name='NanoPBOptions.msgid', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=328,
)

_NANOPBOPTIONS.fields_by_name['int_size'].enum_type = _INTSIZE
_NANOPBOPTIONS.fields_by_name['type'].enum_type = _FIELDTYPE
DESCRIPTOR.message_types_by_name['NanoPBOptions'] = _NANOPBOPTIONS
DESCRIPTOR.enum_types_by_name['FieldType'] = _FIELDTYPE
DESCRIPTOR.enum_types_by_name['IntSize'] = _INTSIZE
DESCRIPTOR.extensions_by_name['nanopb_fileopt'] = nanopb_fileopt
DESCRIPTOR.extensions_by_name['nanopb_msgopt'] = nanopb_msgopt
DESCRIPTOR.extensions_by_name['nanopb_enumopt'] = nanopb_enumopt
DESCRIPTOR.extensions_by_name['nanopb'] = nanopb
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NanoPBOptions = _reflection.GeneratedProtocolMessageType('NanoPBOptions', (_message.Message,), dict(
  DESCRIPTOR = _NANOPBOPTIONS,
  __module__ = 'machinetalk.protobuf.nanopb_pb2'
  # @@protoc_insertion_point(class_scope:NanoPBOptions)
  ))
_sym_db.RegisterMessage(NanoPBOptions)

nanopb_fileopt.message_type = _NANOPBOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(nanopb_fileopt)
nanopb_msgopt.message_type = _NANOPBOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(nanopb_msgopt)
nanopb_enumopt.message_type = _NANOPBOPTIONS
google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(nanopb_enumopt)
nanopb.message_type = _NANOPBOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(nanopb)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
