# -*- coding:utf-8 -*-
#
# 시그니처 계산 코드
# - same logics from Cloudstack
#
# - code by Jioh L. Jung (ziozzang@gmail.com)
#


from base64 import b64encode
from urllib import quote, unquote
import hmac
import hashlib
from utils import *

def calc(params, secret, sig_key, verbose=False):
  """
  파라미터들을 보고 시그니처를 생성한다.
  """
  args = params.copy()
  if sig_key in args:
    del args[sig_key]

  query = '&'.join(
            '='.join([k, quote(args[k])]) \
              for k in sorted(args.keys(), key=str.lower))

  signature = b64encode(hmac.new(
                secret,
                msg=query.lower(),
                digestmod=hashlib.sha1
              ).digest())
  if verbose:
    print "Signature(Calculated): %s" % signature

  return signature

def check(params, secret, verbose=False):
  """
  시그니처가 동일한지 검증 한다.
  """
  k = get_key("signature", params)
  sig = calc(params, secret, k, verbose=verbose)
  if verbose:
    print "Signature(Input)     : %s" % params["signature"]
  if get_val("signature", params) == sig:
    return True
  else:
    return False
