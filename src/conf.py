# -*- coding:utf-8 -*-
#
# 설정 파일.
#
# - code by Jioh L. Jung (ziozzang@gmail.com)
#

import logging

#- 리스닝 포트 
LISTEN_PORT = 7878

#- 디버그 옵션 (stdout 출력)
DEBUG_FLAG = True

#- 로깅 옵션
LOG_LEVEL = logging.INFO

# API URL
API_URL = '/api'

# 출력 기본 양식을 지정 한다
OUTPUT_DEFAULT = "xml"

######################################################################
# 에러 핸들링//
# 오류가 발생 했을때 기본적으로 웹서버에서 전달할 코드
# 이건 바디에서 전달되는 오류코드와 다르다..
# 왜 이렇게 나눠뒀는지는 모르겠음. - HTTP 스펙이랑 좀 다름..
WEBSERVER_ERROR_CODE = 500

# 오류가 났을때 기본적으로 보내는 최상위 엘리먼트.
# Python client 에서는 "errorresponse"로 잡고 있음..
ERROR_ELEMENT = "defaultresponse"

# DB 접속 정보
DB_CONN_INFO = {
  "hostname" : "127.0.0.1",
  "username" : "DB_ID_HERE",
  "password" : "DB_PW_HERE",
  "schema"   : "DB_NAME_HERE",
}

DB_CONN_POOL_COUNT = 3
