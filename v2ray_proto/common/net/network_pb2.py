# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/net/network.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63ommon/net/network.proto\x12\x15v2ray.core.common.net\">\n\x0bNetworkList\x12/\n\x07network\x18\x01 \x03(\x0e\x32\x1e.v2ray.core.common.net.Network*B\n\x07Network\x12\x0b\n\x07Unknown\x10\x00\x12\x0e\n\x06RawTCP\x10\x01\x1a\x02\x08\x01\x12\x07\n\x03TCP\x10\x02\x12\x07\n\x03UDP\x10\x03\x12\x08\n\x04UNIX\x10\x04\x42`\n\x19\x63om.v2ray.core.common.netP\x01Z)github.com/v2fly/v2ray-core/v5/common/net\xaa\x02\x15V2Ray.Core.Common.Netb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.net.network_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.v2ray.core.common.netP\001Z)github.com/v2fly/v2ray-core/v5/common/net\252\002\025V2Ray.Core.Common.Net'
  _globals['_NETWORK'].values_by_name["RawTCP"]._options = None
  _globals['_NETWORK'].values_by_name["RawTCP"]._serialized_options = b'\010\001'
  _globals['_NETWORK']._serialized_start=115
  _globals['_NETWORK']._serialized_end=181
  _globals['_NETWORKLIST']._serialized_start=51
  _globals['_NETWORKLIST']._serialized_end=113
# @@protoc_insertion_point(module_scope)
