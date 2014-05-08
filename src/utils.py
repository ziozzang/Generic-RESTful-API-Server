# -*- coding:utf-8 -*-
#
# 유틸리티용 함수들
#
# - code by Jioh L. Jung (ziozzang@gmail.com)
#

#- 딕셔너리를 키가 대소문자 구분없이 조회할때...
def get_val(keys, params):
  for j in [ (i, i.lower()) for i in params.keys()]:
    if j[1] == keys.lower():
      return params[j[0]]
  else:
    raise KeyError(keys)

def get_key(keys, params):
  for j in [ (i, i.lower()) for i in params.keys()]:
    if j[1] == keys.lower():
      return j[0]
  else:
    raise KeyError(keys)

#- 출력물을 xml 또는 json 형태로 내보낼때 사용
from dict2xml import dict2xml
import json

def output_as(dicts, types):
  """
    파라미터를 원하는 형태로 출력 하도록 함.
  """
  strs = ""
  if types.lower() == "xml":
    strs = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n".dict2xml(dicts)
  elif types.lower() == "json":
    strs = json.dumps(dicts)
  return strs

_content_type = {
  "json": "application/json",
  "xml" : "application/xml",
}

def content_type(types):
  return _content_type[types]

#- 오류 메시지를 포매팅해서 출력
import conf
def rtn_error(code, msg, resptype=conf.OUTPUT_DEFAULT):
  """
    오류 메시지를 포매팅하여 얻음.
  """
  res = {}
  res[conf.ERROR_ELEMENT] = {}
  res[conf.ERROR_ELEMENT]["errorcode"] = code
  res[conf.ERROR_ELEMENT]["errortext"] = msg
  contents = output_as(res, resptype)

  rval = {}
  rval["response"] = contents
  rval["status"] = conf.WEBSERVER_ERROR_CODE
  rval["content_type"] = content_type(resptype)

  return rval
