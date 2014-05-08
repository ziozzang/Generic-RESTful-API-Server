# -*- coding:utf-8 -*-
#
# DB 커넥션 구현 코드
#
# - code by Jioh L. Jung (ziozzang@gmail.com)
#

# pysqlpool installation//
# apt-get install python-pip python-mysqldb
# pip install pysqlpool
import PySQLPool

def set_conninfo(conn_info, max_pool_count = 3):
  conn = PySQLPool.getNewConnection(
           host     = conn_info["hostname"],
           username = conn_info["username"],
           password = conn_info["password"],
           schema   = conn_info["schema"]
         )
  PySQLPool.getNewPool().maxActiveConnections = max_pool_count

  return conn

def get_secret(conn, api_key):
  res = None

  query = PySQLPool.getNewQuery(connection=conn)
  r = query.Query("SELECT SVC_SECRETKEY FROM TBMB_ISSVC WHERE SVC_APIKEY = %s", (api_key))
  if r == 1:
    res = query.record[0]['SVC_SECRETKEY']

  return res

def get_id(conn, api_key):
  res = None

  query = PySQLPool.getNewQuery(connection=conn)
  r = query.Query("SELECT MEM_SQ FROM TBMB_ISSVC WHERE  SVC_APIKEY = %s", (api_key))
  if r == 1:
    res = query.record[0]['MEM_SQ']

  return res
