# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/blackhole/config.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_proto.common.serial import typed_message_pb2 as common_dot_serial_dot_typed__message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cproxy/blackhole/config.proto\x12\x14xray.proxy.blackhole\x1a!common/serial/typed_message.proto\"\x0e\n\x0cNoneResponse\"\x0e\n\x0cHTTPResponse\"<\n\x06\x43onfig\x12\x32\n\x08response\x18\x01 \x01(\x0b\x32 .xray.common.serial.TypedMessageB^\n\x18\x63om.xray.proxy.blackholeP\x01Z)github.com/xtls/xray-core/proxy/blackhole\xaa\x02\x14Xray.Proxy.Blackholeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy.blackhole.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.xray.proxy.blackholeP\001Z)github.com/xtls/xray-core/proxy/blackhole\252\002\024Xray.Proxy.Blackhole'
  _globals['_NONERESPONSE']._serialized_start=89
  _globals['_NONERESPONSE']._serialized_end=103
  _globals['_HTTPRESPONSE']._serialized_start=105
  _globals['_HTTPRESPONSE']._serialized_end=119
  _globals['_CONFIG']._serialized_start=121
  _globals['_CONFIG']._serialized_end=181
# @@protoc_insertion_point(module_scope)
