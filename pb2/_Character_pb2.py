# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: _Character.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    '_Character.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pb2._Item_pb2 as __Item__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10_Character.proto\x12\tDC.Packet\x1a\x0b_Item.proto\"X\n\rSSTORAGE_INFO\x12\x13\n\x0binventoryId\x18\x01 \x01(\r\x12\x32\n\x18\x43haracterStorageItemList\x18\x02 \x03(\x0b\x32\x10.DC.Packet.SItem\"\xe8\x02\n\x0fSCHARACTER_INFO\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x17\n\x0f\x61\x63\x63ountNickname\x18\x02 \x01(\t\x12.\n\x08nickName\x18\x03 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x16\n\x0e\x63haracterClass\x18\x04 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x05 \x01(\t\x12\x0e\n\x06gender\x18\x06 \x01(\r\x12\r\n\x05level\x18\x07 \x01(\r\x12\x13\n\x0bserviceGrpc\x18\x08 \x01(\t\x12+\n\x11\x43haracterItemList\x18\t \x03(\x0b\x32\x10.DC.Packet.SItem\x12\x32\n\x18\x43haracterStorageItemList\x18\n \x03(\x0b\x32\x10.DC.Packet.SItem\x12\x37\n\x15\x43haracterStorageInfos\x18\x0b \x03(\x0b\x32\x18.DC.Packet.SSTORAGE_INFO\"\x91\x02\n\x16SCHARACTER_FRIEND_INFO\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x17\n\x0f\x61\x63\x63ountNickname\x18\x02 \x01(\t\x12.\n\x08nickName\x18\x03 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x16\n\x0e\x63haracterClass\x18\x04 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x05 \x01(\t\x12\x0e\n\x06gender\x18\x06 \x01(\r\x12\r\n\x05level\x18\x07 \x01(\r\x12\x16\n\x0elocationStatus\x18\x08 \x01(\r\x12\x19\n\x11PartyMemeberCount\x18\t \x01(\r\x12\x1c\n\x14PartyMaxMemeberCount\x18\n \x01(\r\"\xe8\x02\n\x15SCHARACTER_PARTY_INFO\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x17\n\x0f\x61\x63\x63ountNickname\x18\x02 \x01(\t\x12.\n\x08nickName\x18\x03 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x16\n\x0e\x63haracterClass\x18\x04 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x05 \x01(\t\x12\x0e\n\x06gender\x18\x06 \x01(\r\x12\r\n\x05level\x18\x07 \x01(\r\x12\x15\n\risPartyLeader\x18\x08 \x01(\r\x12\x0f\n\x07isReady\x18\t \x01(\r\x12\x10\n\x08isInGame\x18\n \x01(\r\x12\'\n\requipItemList\x18\x0b \x03(\x0b\x32\x10.DC.Packet.SItem\x12\x10\n\x08partyIdx\x18\x0c \x01(\r\x12\x1f\n\x05perks\x18\r \x03(\x0b\x32\x10.DC.Packet.SPerk\x12\x11\n\tgearScore\x18\x0e \x01(\r\"\xda\x01\n\x15SCHARACTER_TRADE_INFO\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x17\n\x0f\x61\x63\x63ountNickname\x18\x02 \x01(\t\x12.\n\x08nickName\x18\x03 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x16\n\x0e\x63haracterClass\x18\x04 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x05 \x01(\t\x12\x0e\n\x06gender\x18\x06 \x01(\r\x12\r\n\x05level\x18\x07 \x01(\r\x12\x19\n\x11\x63haracterLocation\x18\x08 \x01(\r\"\x7f\n\x11SACCOUNT_NICKNAME\x12\x18\n\x10originalNickName\x18\x01 \x01(\t\x12\x1d\n\x15streamingModeNickName\x18\x02 \x01(\t\x12\x13\n\x0bkarmaRating\x18\x03 \x01(\x05\x12\x0e\n\x06rankId\x18\x04 \x01(\t\x12\x0c\n\x04\x66\x61me\x18\x05 \x01(\r\"\xab\x01\n\x10SBLOCK_CHARACTER\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x17\n\x0f\x61\x63\x63ountNickname\x18\x02 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x03 \x01(\t\x12.\n\x08nickName\x18\x04 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x16\n\x0e\x63haracterClass\x18\x05 \x01(\t\x12\x0e\n\x06gender\x18\x06 \x01(\r\"\xc8\x01\n\x1eSCHARACTER_GATHERING_HALL_INFO\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x17\n\x0f\x61\x63\x63ountNickname\x18\x02 \x01(\t\x12.\n\x08nickName\x18\x03 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x16\n\x0e\x63haracterClass\x18\x04 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x05 \x01(\t\x12\x0e\n\x06gender\x18\x06 \x01(\r\x12\r\n\x05level\x18\x07 \x01(\r\"0\n\tSGameStat\x12\x10\n\x08statType\x18\x01 \x01(\x05\x12\x11\n\tstatValue\x18\x02 \x01(\x05\"Z\n\rSRankUserInfo\x12\x0e\n\x06rankId\x18\x01 \x01(\t\x12\x14\n\x0c\x63urrentPoint\x18\x02 \x01(\r\x12\x11\n\tneedPoint\x18\x03 \x01(\r\x12\x10\n\x08gameType\x18\x04 \x01(\r*\x80\x01\n\x0f\x46riend_Location\x12\x18\n\x14\x46riend_Location_NONE\x10\x00\x12\x19\n\x15\x46riend_Location_LOBBY\x10\x01\x12\x1b\n\x17\x46riend_Location_DUNGEON\x10\x02\x12\x1b\n\x17\x46riend_Location_OFFLINE\x10\x03\x42$\n\x15\x63om.packets.characterB\tcharacterP\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, '_Character_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.packets.characterB\tcharacterP\000'
  _globals['_FRIEND_LOCATION']._serialized_start=2006
  _globals['_FRIEND_LOCATION']._serialized_end=2134
  _globals['_SSTORAGE_INFO']._serialized_start=44
  _globals['_SSTORAGE_INFO']._serialized_end=132
  _globals['_SCHARACTER_INFO']._serialized_start=135
  _globals['_SCHARACTER_INFO']._serialized_end=495
  _globals['_SCHARACTER_FRIEND_INFO']._serialized_start=498
  _globals['_SCHARACTER_FRIEND_INFO']._serialized_end=771
  _globals['_SCHARACTER_PARTY_INFO']._serialized_start=774
  _globals['_SCHARACTER_PARTY_INFO']._serialized_end=1134
  _globals['_SCHARACTER_TRADE_INFO']._serialized_start=1137
  _globals['_SCHARACTER_TRADE_INFO']._serialized_end=1355
  _globals['_SACCOUNT_NICKNAME']._serialized_start=1357
  _globals['_SACCOUNT_NICKNAME']._serialized_end=1484
  _globals['_SBLOCK_CHARACTER']._serialized_start=1487
  _globals['_SBLOCK_CHARACTER']._serialized_end=1658
  _globals['_SCHARACTER_GATHERING_HALL_INFO']._serialized_start=1661
  _globals['_SCHARACTER_GATHERING_HALL_INFO']._serialized_end=1861
  _globals['_SGAMESTAT']._serialized_start=1863
  _globals['_SGAMESTAT']._serialized_end=1911
  _globals['_SRANKUSERINFO']._serialized_start=1913
  _globals['_SRANKUSERINFO']._serialized_end=2003
# @@protoc_insertion_point(module_scope)
