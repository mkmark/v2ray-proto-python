# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/log/command/config.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pp/log/command/config.proto\x12\x1av2ray.core.app.log.command\"\x08\n\x06\x43onfig\"\x16\n\x14RestartLoggerRequest\"\x17\n\x15RestartLoggerResponse\"\x12\n\x10\x46ollowLogRequest\"$\n\x11\x46ollowLogResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xf5\x01\n\rLoggerService\x12v\n\rRestartLogger\x12\x30.v2ray.core.app.log.command.RestartLoggerRequest\x1a\x31.v2ray.core.app.log.command.RestartLoggerResponse\"\x00\x12l\n\tFollowLog\x12,.v2ray.core.app.log.command.FollowLogRequest\x1a-.v2ray.core.app.log.command.FollowLogResponse\"\x00\x30\x01\x42o\n\x1e\x63om.v2ray.core.app.log.commandP\x01Z.github.com/v2fly/v2ray-core/v5/app/log/command\xaa\x02\x1aV2Ray.Core.App.Log.Commandb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.log.command.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.v2ray.core.app.log.commandP\001Z.github.com/v2fly/v2ray-core/v5/app/log/command\252\002\032V2Ray.Core.App.Log.Command'
  _globals['_CONFIG']._serialized_start=60
  _globals['_CONFIG']._serialized_end=68
  _globals['_RESTARTLOGGERREQUEST']._serialized_start=70
  _globals['_RESTARTLOGGERREQUEST']._serialized_end=92
  _globals['_RESTARTLOGGERRESPONSE']._serialized_start=94
  _globals['_RESTARTLOGGERRESPONSE']._serialized_end=117
  _globals['_FOLLOWLOGREQUEST']._serialized_start=119
  _globals['_FOLLOWLOGREQUEST']._serialized_end=137
  _globals['_FOLLOWLOGRESPONSE']._serialized_start=139
  _globals['_FOLLOWLOGRESPONSE']._serialized_end=175
  _globals['_LOGGERSERVICE']._serialized_start=178
  _globals['_LOGGERSERVICE']._serialized_end=423
# @@protoc_insertion_point(module_scope)
