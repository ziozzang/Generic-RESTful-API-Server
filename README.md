Generic RESTful API Server
==========================
Python 으로 범용의 RESTful API 서버를 구현 해봄.


설치
====

코드는 DB 커넥션부 구현을 위하여 pysqlpool 을 사용 하고 있다. 이 모듈은 MySQL 에 대하여 커넥션 풀링을 구현하여 준다.


```
apt-get install python-pip python-mysqldb
pip install pysqlpool
```

코드는 xml 출력을 위하여 dict2xml 을 사용 하고 있다.

```
pip install dict2xml
```

테스트 클라이언트
=================

해당 서버는 Cloudstack 의 시그니처 생성 로직에 호환된다. 해당 부분을 지원하는 ucloud python 클라이언트를 통하여 테스트가 가능하다.

https://github.com/ziozzang/ucloud


Flask 에서 사용
===============

코드는 웹 프레임워크로 Flask 를 사용 하고 있다. 이 모듈은 Python 웹 프레임워크를 구현 하여 주고 있다.

```
apt-get install python-flask
```

웹서버를 구동하기 위하여 gunicorn 을 사용 하고 있다.

```
apt-get install gunicorn
```


Django 에서 사용
================

Django 에서 사용하기 위해서 다음과 같이 설정 하도록 한다.

장고 설치

```
pip install django
```

프로젝트 생성
```
django-admin.py startproject mysite
```

앱 설정
```
./manage.py startapp hello
```

- 앱 안에 views.py 를 포함한 py 소스 복사.
- commands.py 수정

urls 에 다음의 형식으로 url 설정

```

from api_server import views
urlpatterns = patterns('',
    url(r'^api$', views.generic_api_call)
)
```

테스트 장고 서버 실행
```
./manage.py runserver 0.0.0.0:7878
```

한계점 : 오류 코드 리턴에 이슈가 있음


테스트 API
==========

현재 테스트 API로 echo 가 있음. params 아래에 응답을 돌려주도록 되어 있음
