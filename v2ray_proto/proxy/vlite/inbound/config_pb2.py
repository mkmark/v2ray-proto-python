# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/vlite/inbound/config.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2ray_proto.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n proxy/vlite/inbound/config.proto\x12\x1ev2ray.core.proxy.vlite.inbound\x1a common/protoext/extensions.proto\"\xcd\x01\n\x11UDPProtocolConfig\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x17\n\x0fscramble_packet\x18\x04 \x01(\x08\x12\x12\n\nenable_fec\x18\x05 \x01(\x08\x12\x1c\n\x14\x65nable_stabilization\x18\x06 \x01(\x08\x12\x1c\n\x14\x65nable_renegotiation\x18\x07 \x01(\x08\x12&\n\x1ehandshake_masking_padding_size\x18\x08 \x01(\r:\x15\x82\xb5\x18\x11\n\x07inbound\x12\x06vliteuB{\n\"com.v2ray.core.proxy.vlite.inboundP\x01Z2github.com/v2fly/v2ray-core/v5/proxy/vlite/inbound\xaa\x02\x1eV2Ray.Core.Proxy.Vlite.Inboundb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy.vlite.inbound.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.v2ray.core.proxy.vlite.inboundP\001Z2github.com/v2fly/v2ray-core/v5/proxy/vlite/inbound\252\002\036V2Ray.Core.Proxy.Vlite.Inbound'
  _globals['_UDPPROTOCOLCONFIG']._options = None
  _globals['_UDPPROTOCOLCONFIG']._serialized_options = b'\202\265\030\021\n\007inbound\022\006vliteu'
  _globals['_UDPPROTOCOLCONFIG']._serialized_start=103
  _globals['_UDPPROTOCOLCONFIG']._serialized_end=308
# @@protoc_insertion_point(module_scope)
