# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/dokodemo/config.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2ray_proto.common.net import address_pb2 as common_dot_net_dot_address__pb2
from v2ray_proto.common.net import network_pb2 as common_dot_net_dot_network__pb2
from v2ray_proto.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bproxy/dokodemo/config.proto\x12\x19v2ray.core.proxy.dokodemo\x1a\x18\x63ommon/net/address.proto\x1a\x18\x63ommon/net/network.proto\x1a common/protoext/extensions.proto\"\xfc\x01\n\x06\x43onfig\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32!.v2ray.core.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x02 \x01(\r\x12<\n\x0cnetwork_list\x18\x03 \x01(\x0b\x32\".v2ray.core.common.net.NetworkListB\x02\x18\x01\x12\x30\n\x08networks\x18\x07 \x03(\x0e\x32\x1e.v2ray.core.common.net.Network\x12\x13\n\x07timeout\x18\x04 \x01(\rB\x02\x18\x01\x12\x17\n\x0f\x66ollow_redirect\x18\x05 \x01(\x08\x12\x12\n\nuser_level\x18\x06 \x01(\r\"\xc1\x01\n\x10SimplifiedConfig\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32!.v2ray.core.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x34\n\x08networks\x18\x03 \x01(\x0b\x32\".v2ray.core.common.net.NetworkList\x12\x17\n\x0f\x66ollow_redirect\x18\x04 \x01(\x08:\x1c\x82\xb5\x18\x18\n\x07inbound\x12\rdokodemo-doorBl\n\x1d\x63om.v2ray.core.proxy.dokodemoP\x01Z-github.com/v2fly/v2ray-core/v5/proxy/dokodemo\xaa\x02\x19V2Ray.Core.Proxy.Dokodemob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy.dokodemo.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.v2ray.core.proxy.dokodemoP\001Z-github.com/v2fly/v2ray-core/v5/proxy/dokodemo\252\002\031V2Ray.Core.Proxy.Dokodemo'
  _globals['_CONFIG'].fields_by_name['network_list']._options = None
  _globals['_CONFIG'].fields_by_name['network_list']._serialized_options = b'\030\001'
  _globals['_CONFIG'].fields_by_name['timeout']._options = None
  _globals['_CONFIG'].fields_by_name['timeout']._serialized_options = b'\030\001'
  _globals['_SIMPLIFIEDCONFIG']._options = None
  _globals['_SIMPLIFIEDCONFIG']._serialized_options = b'\202\265\030\030\n\007inbound\022\rdokodemo-door'
  _globals['_CONFIG']._serialized_start=145
  _globals['_CONFIG']._serialized_end=397
  _globals['_SIMPLIFIEDCONFIG']._serialized_start=400
  _globals['_SIMPLIFIEDCONFIG']._serialized_end=593
# @@protoc_insertion_point(module_scope)
