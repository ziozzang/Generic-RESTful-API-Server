#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# 플라스크 구동 코드
#
# - code by Jioh L. Jung (ziozzang@gmail.com)
#

#- 기본 파이썬 모듈
import sys
import os
import re
import logging
from logging.handlers import SysLogHandler

#- 플라스크 모듈
from flask import \
  Flask, redirect, url_for, request, Response, render_template

#- 내부 작성 모듈
import conf
import core

app = Flask(__name__)
application = app  # for easy gunicorn

@app.route(conf.API_URL, methods=["GET", "POST"])
def generic_api_call():
  get_params = request.args
  post_params = {}

  if request.method == "POST":
    post_params = request.form

  res = core.generic_api_core(get_params, post_params)

  return Response(response    =res["response"],
                      status      =res["status"],
                      content_type=res["content_type"],
                 )

# 만일 디버깅을 위하여 직접 실행 할경우 아래 코드로 실행
if __name__ == '__main__':
  app.run(
    #processes=5,
    debug=conf.DEBUG_FLAG, host='0.0.0.0', port=conf.LISTEN_PORT)
