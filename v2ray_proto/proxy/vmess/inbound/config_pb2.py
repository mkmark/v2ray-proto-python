# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/vmess/inbound/config.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2ray_proto.common.protocol import user_pb2 as common_dot_protocol_dot_user__pb2
from v2ray_proto.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n proxy/vmess/inbound/config.proto\x12\x1ev2ray.core.proxy.vmess.inbound\x1a\x1a\x63ommon/protocol/user.proto\x1a common/protoext/extensions.proto\"\x1a\n\x0c\x44\x65tourConfig\x12\n\n\x02to\x18\x01 \x01(\t\"0\n\rDefaultConfig\x12\x10\n\x08\x61lter_id\x18\x01 \x01(\r\x12\r\n\x05level\x18\x02 \x01(\r\"\xd6\x01\n\x06\x43onfig\x12.\n\x04user\x18\x01 \x03(\x0b\x32 .v2ray.core.common.protocol.User\x12>\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\x0b\x32-.v2ray.core.proxy.vmess.inbound.DefaultConfig\x12<\n\x06\x64\x65tour\x18\x03 \x01(\x0b\x32,.v2ray.core.proxy.vmess.inbound.DetourConfig\x12\x1e\n\x16secure_encryption_only\x18\x04 \x01(\x08\"7\n\x10SimplifiedConfig\x12\r\n\x05users\x18\x01 \x03(\t:\x14\x82\xb5\x18\x10\n\x07inbound\x12\x05vmessB{\n\"com.v2ray.core.proxy.vmess.inboundP\x01Z2github.com/v2fly/v2ray-core/v5/proxy/vmess/inbound\xaa\x02\x1eV2Ray.Core.Proxy.Vmess.Inboundb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy.vmess.inbound.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.v2ray.core.proxy.vmess.inboundP\001Z2github.com/v2fly/v2ray-core/v5/proxy/vmess/inbound\252\002\036V2Ray.Core.Proxy.Vmess.Inbound'
  _globals['_SIMPLIFIEDCONFIG']._options = None
  _globals['_SIMPLIFIEDCONFIG']._serialized_options = b'\202\265\030\020\n\007inbound\022\005vmess'
  _globals['_DETOURCONFIG']._serialized_start=130
  _globals['_DETOURCONFIG']._serialized_end=156
  _globals['_DEFAULTCONFIG']._serialized_start=158
  _globals['_DEFAULTCONFIG']._serialized_end=206
  _globals['_CONFIG']._serialized_start=209
  _globals['_CONFIG']._serialized_end=423
  _globals['_SIMPLIFIEDCONFIG']._serialized_start=425
  _globals['_SIMPLIFIEDCONFIG']._serialized_end=480
# @@protoc_insertion_point(module_scope)
