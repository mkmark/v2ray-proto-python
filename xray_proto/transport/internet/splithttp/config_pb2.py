# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/splithttp/config.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)transport/internet/splithttp/config.proto\x12!xray.transport.internet.splithttp\"\xf2\x03\n\x06\x43onfig\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x45\n\x06header\x18\x03 \x03(\x0b\x32\x35.xray.transport.internet.splithttp.Config.HeaderEntry\x12P\n\x14scMaxConcurrentPosts\x18\x04 \x01(\x0b\x32\x32.xray.transport.internet.splithttp.RandRangeConfig\x12N\n\x12scMaxEachPostBytes\x18\x05 \x01(\x0b\x32\x32.xray.transport.internet.splithttp.RandRangeConfig\x12P\n\x14scMinPostsIntervalMs\x18\x06 \x01(\x0b\x32\x32.xray.transport.internet.splithttp.RandRangeConfig\x12\x13\n\x0bnoSSEHeader\x18\x07 \x01(\x08\x12M\n\x11responseOkPadding\x18\x08 \x01(\x0b\x32\x32.xray.transport.internet.splithttp.RandRangeConfig\x1a-\n\x0bHeaderEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x0fRandRangeConfig\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x05\x12\n\n\x02to\x18\x02 \x01(\x05\x42\x85\x01\n%com.xray.transport.internet.splithttpP\x01Z6github.com/xtls/xray-core/transport/internet/splithttp\xaa\x02!Xray.Transport.Internet.SplitHttpb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transport.internet.splithttp.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%com.xray.transport.internet.splithttpP\001Z6github.com/xtls/xray-core/transport/internet/splithttp\252\002!Xray.Transport.Internet.SplitHttp'
  _globals['_CONFIG_HEADERENTRY']._options = None
  _globals['_CONFIG_HEADERENTRY']._serialized_options = b'8\001'
  _globals['_CONFIG']._serialized_start=81
  _globals['_CONFIG']._serialized_end=579
  _globals['_CONFIG_HEADERENTRY']._serialized_start=534
  _globals['_CONFIG_HEADERENTRY']._serialized_end=579
  _globals['_RANDRANGECONFIG']._serialized_start=581
  _globals['_RANDRANGECONFIG']._serialized_end=624
# @@protoc_insertion_point(module_scope)
