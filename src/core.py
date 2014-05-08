#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# 서버 메인 코드
#
# - code by Jioh L. Jung (ziozzang@gmail.com)
#

#- 기본 파이썬 모듈
import re

#- 내부 작성 모듈
import signature
import dbquery
import commands
import conf
from utils import *

conn = dbquery.set_conninfo(conf.DB_CONN_INFO, conf.DB_CONN_POOL_COUNT)

def generic_api_core(get_dict, post_dict):
  # 초기값 설정
  res = {}
  rescode = 200
  params = get_dict

  # Prerequisites //=====================================================
  # 1. apiKey 가 있는지 확인 한다.
  if "apikey" in [ i.lower() for i in params.keys()]:
    # 있으면 secret 을 얻어온다.
    apikey = get_val("apikey", params)
    secret = dbquery.get_secret(conn,apikey)
    if secret is None:
      # 그런 사람 없음. api_key 를 못찾음.
      return rtn_error(401, "No such API Keys")
  else:
    # 요청 쿼리에 apikey없으면 오류 발생.
    return rtn_error(401, "No API Keys on Query")

  # 2. command 가 있는지 확인 한다.
  if "command" in [ i.lower() for i in params.keys()]:
    command = get_val("command", params)
  else:
    # 없으면 오류 발생.
    return rtn_error(437, "No command on Query")

  # 3. 시그니처를 검증 하도록 한다.
  if "signature" in [ i.lower() for i in params.keys()]:
    checks = signature.check(params, secret, verbose=conf.DEBUG_FLAG)
    if not checks:
      # 시그니처가 맞지 않음.
      return rtn_error(431, "Not Matched Signature")
  else:
    # 시그니처가 존재 하지 않음. 오류 발생
    return rtn_error(431, "No Signature Keys on Query")

  # 4. 응답 타입을 설정 한다
  resptype = conf.OUTPUT_DEFAULT
  if "response" in [ i.lower() for i in params.keys()]:
    resptype = get_val("response", params)

  # 5. 요청 파라미터를 정리 한다.
  reqs = {}
  for i in get_dict.keys():
    reqs[i] = get_dict[i]
  for i in post_dict.keys():
    reqs[i] = post_dict[i]

  # Main Code //=====================================================
  # 1. 실제 커맨드에 따라 명령어 분기.
  if command in commands.clist:
    res = commands.clist[command](reqs)
  else:
    # 커맨드를 실제 찾을수 없었음. 오류 처리
    return rtn_error(432, "The given command is not supported.")

  # 2. 실제 커맨드 결과를 정리하여 전달.
  rres = {}
  rtag = "%s%s" % (command, "response")
  rres[rtag] = res

  # Post-processing //=====================================================
  # 1. 출력을 응답 타입에 맞추어서 변경한다.
  contents = output_as(rres, resptype)
  rval = {}
  rval["response"] = contents
  rval["status"] = rescode
  rval["content_type"] = content_type(resptype)

  return rval
