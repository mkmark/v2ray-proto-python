# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/tun/config.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2ray_proto.app.proxyman import config_pb2 as app_dot_proxyman_dot_config__pb2
from v2ray_proto.app.router.routercommon import common_pb2 as app_dot_router_dot_routercommon_dot_common__pb2
from v2ray_proto.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2
from v2ray_proto.common.net.packetaddr import config_pb2 as common_dot_net_dot_packetaddr_dot_config__pb2
from v2ray_proto.transport.internet import config_pb2 as transport_dot_internet_dot_config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61pp/tun/config.proto\x12\x12v2ray.core.app.tun\x1a\x19\x61pp/proxyman/config.proto\x1a$app/router/routercommon/common.proto\x1a common/protoext/extensions.proto\x1a\"common/net/packetaddr/config.proto\x1a\x1ftransport/internet/config.proto\"\xd1\x03\n\x06\x43onfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03mtu\x18\x02 \x01(\r\x12\x12\n\nuser_level\x18\x03 \x01(\r\x12\x42\n\x0fpacket_encoding\x18\x04 \x01(\x0e\x32).v2ray.core.net.packetaddr.PacketAddrType\x12\x0b\n\x03tag\x18\x05 \x01(\t\x12\x35\n\x03ips\x18\x06 \x03(\x0b\x32(.v2ray.core.app.router.routercommon.CIDR\x12\x38\n\x06routes\x18\x07 \x03(\x0b\x32(.v2ray.core.app.router.routercommon.CIDR\x12\x1f\n\x17\x65nable_promiscuous_mode\x18\x08 \x01(\x08\x12\x17\n\x0f\x65nable_spoofing\x18\t \x01(\x08\x12\x44\n\x0fsocket_settings\x18\n \x01(\x0b\x32+.v2ray.core.transport.internet.SocketConfig\x12\x42\n\x11sniffing_settings\x18\x0b \x01(\x0b\x32\'.v2ray.core.app.proxyman.SniffingConfig:\x12\x82\xb5\x18\x0e\n\x07service\x12\x03tunBW\n\x16\x63om.v2ray.core.app.tunP\x01Z&github.com/v2fly/v2ray-core/v5/app/tun\xaa\x02\x12V2Ray.Core.App.Tunb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.tun.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.v2ray.core.app.tunP\001Z&github.com/v2fly/v2ray-core/v5/app/tun\252\002\022V2Ray.Core.App.Tun'
  _globals['_CONFIG']._options = None
  _globals['_CONFIG']._serialized_options = b'\202\265\030\016\n\007service\022\003tun'
  _globals['_CONFIG']._serialized_start=213
  _globals['_CONFIG']._serialized_end=678
# @@protoc_insertion_point(module_scope)
