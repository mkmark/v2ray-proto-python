# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/trojan/simplified/config.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2ray_proto.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2
from v2ray_proto.common.net import address_pb2 as common_dot_net_dot_address__pb2
from v2ray_proto.common.net.packetaddr import config_pb2 as common_dot_net_dot_packetaddr_dot_config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$proxy/trojan/simplified/config.proto\x12\"v2ray.core.proxy.trojan.simplified\x1a common/protoext/extensions.proto\x1a\x18\x63ommon/net/address.proto\x1a\"common/net/packetaddr/config.proto\"x\n\x0cServerConfig\x12\r\n\x05users\x18\x01 \x03(\t\x12\x42\n\x0fpacket_encoding\x18\x02 \x01(\x0e\x32).v2ray.core.net.packetaddr.PacketAddrType:\x15\x82\xb5\x18\x11\n\x07inbound\x12\x06trojan\"z\n\x0c\x43lientConfig\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32!.v2ray.core.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x10\n\x08password\x18\x03 \x01(\t:\x16\x82\xb5\x18\x12\n\x08outbound\x12\x06trojanB\x87\x01\n&com.v2ray.core.proxy.trojan.simplifiedP\x01Z6github.com/v2fly/v2ray-core/v5/proxy/trojan/simplified\xaa\x02\"V2Ray.Core.Proxy.Trojan.Simplifiedb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy.trojan.simplified.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.v2ray.core.proxy.trojan.simplifiedP\001Z6github.com/v2fly/v2ray-core/v5/proxy/trojan/simplified\252\002\"V2Ray.Core.Proxy.Trojan.Simplified'
  _globals['_SERVERCONFIG']._options = None
  _globals['_SERVERCONFIG']._serialized_options = b'\202\265\030\021\n\007inbound\022\006trojan'
  _globals['_CLIENTCONFIG']._options = None
  _globals['_CLIENTCONFIG']._serialized_options = b'\202\265\030\022\n\010outbound\022\006trojan'
  _globals['_SERVERCONFIG']._serialized_start=172
  _globals['_SERVERCONFIG']._serialized_end=292
  _globals['_CLIENTCONFIG']._serialized_start=294
  _globals['_CLIENTCONFIG']._serialized_end=416
# @@protoc_insertion_point(module_scope)
