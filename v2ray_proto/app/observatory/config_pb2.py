# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/observatory/config.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2ray_proto.common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pp/observatory/config.proto\x12\x1av2ray.core.app.observatory\x1a common/protoext/extensions.proto\"O\n\x11ObservationResult\x12:\n\x06status\x18\x01 \x03(\x0b\x32*.v2ray.core.app.observatory.OutboundStatus\"v\n\x1bHealthPingMeasurementResult\x12\x0b\n\x03\x61ll\x18\x01 \x01(\x03\x12\x0c\n\x04\x66\x61il\x18\x02 \x01(\x03\x12\x11\n\tdeviation\x18\x03 \x01(\x03\x12\x0f\n\x07\x61verage\x18\x04 \x01(\x03\x12\x0b\n\x03max\x18\x05 \x01(\x03\x12\x0b\n\x03min\x18\x06 \x01(\x03\"\xdc\x01\n\x0eOutboundStatus\x12\r\n\x05\x61live\x18\x01 \x01(\x08\x12\r\n\x05\x64\x65lay\x18\x02 \x01(\x03\x12\x19\n\x11last_error_reason\x18\x03 \x01(\t\x12\x14\n\x0coutbound_tag\x18\x04 \x01(\t\x12\x16\n\x0elast_seen_time\x18\x05 \x01(\x03\x12\x15\n\rlast_try_time\x18\x06 \x01(\x03\x12L\n\x0bhealth_ping\x18\x07 \x01(\x0b\x32\x37.v2ray.core.app.observatory.HealthPingMeasurementResult\"F\n\x0bProbeResult\x12\r\n\x05\x61live\x18\x01 \x01(\x08\x12\r\n\x05\x64\x65lay\x18\x02 \x01(\x03\x12\x19\n\x11last_error_reason\x18\x03 \x01(\t\"#\n\tIntensity\x12\x16\n\x0eprobe_interval\x18\x01 \x01(\r\"s\n\x06\x43onfig\x12\x18\n\x10subject_selector\x18\x02 \x03(\t\x12\x11\n\tprobe_url\x18\x03 \x01(\t\x12\x16\n\x0eprobe_interval\x18\x04 \x01(\x03:$\x82\xb5\x18 \n\x07service\x12\x15\x62\x61\x63kgroundObservatoryBo\n\x1e\x63om.v2ray.core.app.observatoryP\x01Z.github.com/v2fly/v2ray-core/v5/app/observatory\xaa\x02\x1aV2Ray.Core.App.Observatoryb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.observatory.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.v2ray.core.app.observatoryP\001Z.github.com/v2fly/v2ray-core/v5/app/observatory\252\002\032V2Ray.Core.App.Observatory'
  _globals['_CONFIG']._options = None
  _globals['_CONFIG']._serialized_options = b'\202\265\030 \n\007service\022\025backgroundObservatory'
  _globals['_OBSERVATIONRESULT']._serialized_start=94
  _globals['_OBSERVATIONRESULT']._serialized_end=173
  _globals['_HEALTHPINGMEASUREMENTRESULT']._serialized_start=175
  _globals['_HEALTHPINGMEASUREMENTRESULT']._serialized_end=293
  _globals['_OUTBOUNDSTATUS']._serialized_start=296
  _globals['_OUTBOUNDSTATUS']._serialized_end=516
  _globals['_PROBERESULT']._serialized_start=518
  _globals['_PROBERESULT']._serialized_end=588
  _globals['_INTENSITY']._serialized_start=590
  _globals['_INTENSITY']._serialized_end=625
  _globals['_CONFIG']._serialized_start=627
  _globals['_CONFIG']._serialized_end=742
# @@protoc_insertion_point(module_scope)
