# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/shadowsocks/simplified/config.proto
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
from v2ray_proto.common.net import network_pb2 as common_dot_net_dot_network__pb2
from v2ray_proto.common.net.packetaddr import config_pb2 as common_dot_net_dot_packetaddr_dot_config__pb2
from v2ray_proto.proxy.shadowsocks import config_pb2 as proxy_dot_shadowsocks_dot_config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)proxy/shadowsocks/simplified/config.proto\x12\'v2ray.core.proxy.shadowsocks.simplified\x1a common/protoext/extensions.proto\x1a\x18\x63ommon/net/address.proto\x1a\x18\x63ommon/net/network.proto\x1a\"common/net/packetaddr/config.proto\x1a\x1eproxy/shadowsocks/config.proto\"\x82\x02\n\x0cServerConfig\x12J\n\x06method\x18\x01 \x01(\x0b\x32:.v2ray.core.proxy.shadowsocks.simplified.CipherTypeWrapper\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x34\n\x08networks\x18\x03 \x01(\x0b\x32\".v2ray.core.common.net.NetworkList\x12\x42\n\x0fpacket_encoding\x18\x04 \x01(\x0e\x32).v2ray.core.net.packetaddr.PacketAddrType:\x1a\x82\xb5\x18\x16\n\x07inbound\x12\x0bshadowsocks\"\xfd\x01\n\x0c\x43lientConfig\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32!.v2ray.core.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x02 \x01(\r\x12J\n\x06method\x18\x03 \x01(\x0b\x32:.v2ray.core.proxy.shadowsocks.simplified.CipherTypeWrapper\x12\x10\n\x08password\x18\x04 \x01(\t\x12,\n\"experiment_reduced_iv_head_entropy\x18\x91\xbf\x05 \x01(\x08:\x1f\x82\xb5\x18\x1b\n\x08outbound\x12\x0bshadowsocks\x90\xff)\x01\"L\n\x11\x43ipherTypeWrapper\x12\x37\n\x05value\x18\x01 \x01(\x0e\x32(.v2ray.core.proxy.shadowsocks.CipherTypeB\x96\x01\n+com.v2ray.core.proxy.shadowsocks.simplifiedP\x01Z;github.com/v2fly/v2ray-core/v5/proxy/shadowsocks/simplified\xaa\x02\'V2Ray.Core.Proxy.Shadowsocks.Simplifiedb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy.shadowsocks.simplified.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n+com.v2ray.core.proxy.shadowsocks.simplifiedP\001Z;github.com/v2fly/v2ray-core/v5/proxy/shadowsocks/simplified\252\002\'V2Ray.Core.Proxy.Shadowsocks.Simplified'
  _globals['_SERVERCONFIG']._options = None
  _globals['_SERVERCONFIG']._serialized_options = b'\202\265\030\026\n\007inbound\022\013shadowsocks'
  _globals['_CLIENTCONFIG']._options = None
  _globals['_CLIENTCONFIG']._serialized_options = b'\202\265\030\033\n\010outbound\022\013shadowsocks\220\377)\001'
  _globals['_SERVERCONFIG']._serialized_start=241
  _globals['_SERVERCONFIG']._serialized_end=499
  _globals['_CLIENTCONFIG']._serialized_start=502
  _globals['_CLIENTCONFIG']._serialized_end=755
  _globals['_CIPHERTYPEWRAPPER']._serialized_start=757
  _globals['_CIPHERTYPEWRAPPER']._serialized_end=833
# @@protoc_insertion_point(module_scope)
