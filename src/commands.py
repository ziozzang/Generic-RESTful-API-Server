# -*- coding:utf-8 -*-
#
# 실제 커맨드 바디 구현체
#
# - code by Jioh L. Jung (ziozzang@gmail.com)
#

def command_echo(params):
  """
  예제 함수
  """
  res = {}
  res["params"] = params
  return res


# 커맨드 목록을 아래에 나열 한다.
clist = {"echo": command_echo}
