# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profile.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rprofile.proto\x12\x0eprofileservice\"L\n\x14\x43reateProfileRequest\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"C\n\x15\x43reateProfileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t2p\n\x0eProfileService\x12^\n\rCreateProfile\x12$.profileservice.CreateProfileRequest\x1a%.profileservice.CreateProfileResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'profile_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CREATEPROFILEREQUEST']._serialized_start=33
  _globals['_CREATEPROFILEREQUEST']._serialized_end=109
  _globals['_CREATEPROFILERESPONSE']._serialized_start=111
  _globals['_CREATEPROFILERESPONSE']._serialized_end=178
  _globals['_PROFILESERVICE']._serialized_start=180
  _globals['_PROFILESERVICE']._serialized_end=292
# @@protoc_insertion_point(module_scope)
