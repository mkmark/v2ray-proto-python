# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/config.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_proto.common.serial import typed_message_pb2 as common_dot_serial_dot_typed__message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ftransport/internet/config.proto\x12\x17xray.transport.internet\x1a!common/serial/typed_message.proto\"\x9e\x01\n\x0fTransportConfig\x12@\n\x08protocol\x18\x01 \x01(\x0e\x32*.xray.transport.internet.TransportProtocolB\x02\x18\x01\x12\x15\n\rprotocol_name\x18\x03 \x01(\t\x12\x32\n\x08settings\x18\x02 \x01(\x0b\x32 .xray.common.serial.TypedMessage\"\xc1\x02\n\x0cStreamConfig\x12@\n\x08protocol\x18\x01 \x01(\x0e\x32*.xray.transport.internet.TransportProtocolB\x02\x18\x01\x12\x15\n\rprotocol_name\x18\x05 \x01(\t\x12\x44\n\x12transport_settings\x18\x02 \x03(\x0b\x32(.xray.transport.internet.TransportConfig\x12\x15\n\rsecurity_type\x18\x03 \x01(\t\x12;\n\x11security_settings\x18\x04 \x03(\x0b\x32 .xray.common.serial.TypedMessage\x12>\n\x0fsocket_settings\x18\x06 \x01(\x0b\x32%.xray.transport.internet.SocketConfig\"7\n\x0bProxyConfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x1b\n\x13transportLayerProxy\x18\x02 \x01(\x08\"H\n\rCustomSockopt\x12\r\n\x05level\x18\x01 \x01(\t\x12\x0b\n\x03opt\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\"\x8d\x05\n\x0cSocketConfig\x12\x0c\n\x04mark\x18\x01 \x01(\x05\x12\x0b\n\x03tfo\x18\x02 \x01(\x05\x12@\n\x06tproxy\x18\x03 \x01(\x0e\x32\x30.xray.transport.internet.SocketConfig.TProxyMode\x12%\n\x1dreceive_original_dest_address\x18\x04 \x01(\x08\x12\x14\n\x0c\x62ind_address\x18\x05 \x01(\x0c\x12\x11\n\tbind_port\x18\x06 \x01(\r\x12\x1d\n\x15\x61\x63\x63\x65pt_proxy_protocol\x18\x07 \x01(\x08\x12@\n\x0f\x64omain_strategy\x18\x08 \x01(\x0e\x32\'.xray.transport.internet.DomainStrategy\x12\x14\n\x0c\x64ialer_proxy\x18\t \x01(\t\x12\x1f\n\x17tcp_keep_alive_interval\x18\n \x01(\x05\x12\x1b\n\x13tcp_keep_alive_idle\x18\x0b \x01(\x05\x12\x16\n\x0etcp_congestion\x18\x0c \x01(\t\x12\x11\n\tinterface\x18\r \x01(\t\x12\x0e\n\x06v6only\x18\x0e \x01(\x08\x12\x18\n\x10tcp_window_clamp\x18\x0f \x01(\x05\x12\x18\n\x10tcp_user_timeout\x18\x10 \x01(\x05\x12\x13\n\x0btcp_max_seg\x18\x11 \x01(\x05\x12\x14\n\x0ctcp_no_delay\x18\x12 \x01(\x08\x12\x11\n\ttcp_mptcp\x18\x13 \x01(\x08\x12=\n\rcustomSockopt\x18\x14 \x03(\x0b\x32&.xray.transport.internet.CustomSockopt\"/\n\nTProxyMode\x12\x07\n\x03Off\x10\x00\x12\n\n\x06TProxy\x10\x01\x12\x0c\n\x08Redirect\x10\x02*z\n\x11TransportProtocol\x12\x07\n\x03TCP\x10\x00\x12\x07\n\x03UDP\x10\x01\x12\x08\n\x04MKCP\x10\x02\x12\r\n\tWebSocket\x10\x03\x12\x08\n\x04HTTP\x10\x04\x12\x10\n\x0c\x44omainSocket\x10\x05\x12\x0f\n\x0bHTTPUpgrade\x10\x06\x12\r\n\tSplitHTTP\x10\x07*\xa9\x01\n\x0e\x44omainStrategy\x12\t\n\x05\x41S_IS\x10\x00\x12\n\n\x06USE_IP\x10\x01\x12\x0b\n\x07USE_IP4\x10\x02\x12\x0b\n\x07USE_IP6\x10\x03\x12\x0c\n\x08USE_IP46\x10\x04\x12\x0c\n\x08USE_IP64\x10\x05\x12\x0c\n\x08\x46ORCE_IP\x10\x06\x12\r\n\tFORCE_IP4\x10\x07\x12\r\n\tFORCE_IP6\x10\x08\x12\x0e\n\nFORCE_IP46\x10\t\x12\x0e\n\nFORCE_IP64\x10\nBg\n\x1b\x63om.xray.transport.internetP\x01Z,github.com/xtls/xray-core/transport/internet\xaa\x02\x17Xray.Transport.Internetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transport.internet.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.xray.transport.internetP\001Z,github.com/xtls/xray-core/transport/internet\252\002\027Xray.Transport.Internet'
  _globals['_TRANSPORTCONFIG'].fields_by_name['protocol']._options = None
  _globals['_TRANSPORTCONFIG'].fields_by_name['protocol']._serialized_options = b'\030\001'
  _globals['_STREAMCONFIG'].fields_by_name['protocol']._options = None
  _globals['_STREAMCONFIG'].fields_by_name['protocol']._serialized_options = b'\030\001'
  _globals['_TRANSPORTPROTOCOL']._serialized_start=1367
  _globals['_TRANSPORTPROTOCOL']._serialized_end=1489
  _globals['_DOMAINSTRATEGY']._serialized_start=1492
  _globals['_DOMAINSTRATEGY']._serialized_end=1661
  _globals['_TRANSPORTCONFIG']._serialized_start=96
  _globals['_TRANSPORTCONFIG']._serialized_end=254
  _globals['_STREAMCONFIG']._serialized_start=257
  _globals['_STREAMCONFIG']._serialized_end=578
  _globals['_PROXYCONFIG']._serialized_start=580
  _globals['_PROXYCONFIG']._serialized_end=635
  _globals['_CUSTOMSOCKOPT']._serialized_start=637
  _globals['_CUSTOMSOCKOPT']._serialized_end=709
  _globals['_SOCKETCONFIG']._serialized_start=712
  _globals['_SOCKETCONFIG']._serialized_end=1365
  _globals['_SOCKETCONFIG_TPROXYMODE']._serialized_start=1318
  _globals['_SOCKETCONFIG_TPROXYMODE']._serialized_end=1365
# @@protoc_insertion_point(module_scope)
