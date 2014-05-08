#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# 장고용 코드
#
# - code by Jioh L. Jung (ziozzang@gmail.com)
#

from django.http import HttpResponse
import core

"""
# urls 에 다음과 같이 선언해서 사용 하면 됩니다.

from api_server import views
urlpatterns = patterns('',
    url(r'^api$', views.generic_api_call)
)
"""
def generic_api_call(request):
  get_params = {}
  for i in request.GET.keys():
    get_params[i.encode("UTF-8")] = request.GET[i].encode("UTF-8")

  post_params = {}
  for i in request.POST.keys():
    post_params[i.encode("UTF-8")] = request.POST[i].encode("UTF-8")

  res = core.generic_api_core(get_params, post_params)

  rsp = HttpResponse(res["response"])
  rsp.content_type=res["content_type"]
  rsp.status_code =res["status"]
  return rsp
