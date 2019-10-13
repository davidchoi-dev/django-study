django 공부하면서 그냥 끄적이는 내용...

해당 내용은 [공식문서](https://docs.djangoproject.com/ko/2.2)를 참고하여 공부한 내용입니다.

관리자 쪽을 좀 더 수월하게 만들수 있지 않을까 하는 기대감을 가지며... 공부하는 중 

# 프로젝트 및 앱 생성 후 실행

- Django 설치

```bash
$ pip install django
```

- 프로젝트 생성

```bash
$ django-admin startproject [프로젝트 이름]

$ django-admin startproject mysite

mysite/ $ tree         # 프로젝트 구조 조회                                
.
├── manage.py
└── mysite
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

1 directory, 5 files
```

[`startproject`](https://docs.djangoproject.com/ko/2.2/ref/django-admin/#django-admin-startproject)로 mystie 프로젝트 생성

```
manage.py : Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티   https://docs.djangoproject.com/ko/2.2/ref/django-admin/ 여기서 자세한 정보 확인가능

mysite/ : 디렉터리 내부에는 프로젝트를 위한 실제 파이썬 패키지 저장됨. 이 디렉터리 이름을 이용하여 프로젝트 어디서나 파이썬 패키지를 가져옴

mysite/__init__.py : 파이썬에서 해당 디렉터리를 패키지라고 알려줌

mysite/setting.py : Django 프로젝트의 환경 및 구성저장.

mysite/urls.py : Django 프로젝트의 URL 선언을 저장. Django로 작성된 사이트의 '목차'라고 할 수 있음.

mysite/wsgi.py : 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입지점
```



- 개발서버 실행

```
$ python manage.py runserver [오픈포트]
```

오픈포트를 전달하지 않으면 기본값으로 8000사용

개발서버는 운영서버에서 사용하지 말것! 개발서버는 요청이 들어올 때마다 자동으로 파이썬 코드를 다시 불러옴. 코드가 수정될 때마다 서버를 재시작 하지 않아도 됨



- 앱 생성

```bash
$ python manage.py startapp [앱 이름]
$ python manage.py startapp polls

polls/ $ tree
.
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

1 directory, 7 files
```



- polls 앱 수정 후 등록

```python
# polls/views.py 수정
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

```python
# polls/urls.py 추가
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

polls 앱을 만들어 요청에 대한 응답을 등록한다.

```python
# mysite/urls.py 수정
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

요청에 대한 응답이 등록된 polls 앱을 mysite 프로젝트(최상위 **`URLconf`**)에 추가한다. **`admin.site.urls`**를 제외한 나머지 **`urlpatterns`**는 **`include()`**를 이용하여 추가한다.

**`path()`** 함수는 2개의 필수 인수 **route**와 **view**를 받습니다. 추가적으로 kwargs와 name을 이용하여 2개의 인수를 더 받아 총 4개의 인수를 받을 수 있습니다.

1. route: url 패턴을 가진 **문자열**. django는 **urlpatterns**의 첫 번째 패턴부터 시작하여, 일치하는 패턴을 찾을 때 까지 요청된 url을 각 패턴과 리스트의 순서로 비교. 패턴들은 GET이나 POST같은 요청 메소드 또는 도메인 이름을 검색하지 않음. 
2. view: django에서 일치하는 패턴을 찾으면 **HttpRequest** 객체를 첫 번째 인수로 하고, 경로로 부터 '캡처된' 값을 키워드 인수로하여 특정한 view 함수 호출
3. kwargs: 임의의 키워드 인수들은 목표한 view에 사전형으로 전달됨
4. name: URL에 이름을 지으면, 템플릿을 포함한 Django 어디에서나 명확하게 참조할 수 있음. 이 기능을 이용하면, 단 하나의 파일만 수정해도 project 내의 모든 URL 패턴을 바꿀 수 있음.

- 앱 실행

```bash
$ python manage.py runserver
```

/admin 또는 /polls로 접속하지 않을경우 에러페이지를 띄운다.

# 데이터베이스

- 엔진선택 및 설정

**mysite/settings.py**에서 수정

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

django는 sqlite3을 기본값으로 사용 

- [`ENGINE`](https://docs.djangoproject.com/ko/2.2/ref/settings/#std:setting-DATABASE-ENGINE) -- `'django.db.backends.sqlite3'`, `'django.db.backends.postgresql'`, `'django.db.backends.mysql'`, 또는 `'django.db.backends.oracle'`. 그외에 [서드파티 백엔드](https://docs.djangoproject.com/ko/2.2/ref/databases/#third-party-notes) 참조.
- [`NAME`](https://docs.djangoproject.com/ko/2.2/ref/settings/#std:setting-NAME) -- 데이터베이스의 이름. 만약 SQLite를 사용 중이라면, 데이터베이스는 당신의 컴퓨터의 파일로서 저장됩니다. 이 경우, [`NAME`](https://docs.djangoproject.com/ko/2.2/ref/settings/#std:setting-NAME) 는 파일명을 포함한 절대경로로 지정해야 합니다. 기본값은 `os.path.join(BASE_DIR, 'db.sqlite3')`로 정의되어 있으며, 프로젝트 디렉토리 내에 `db.sqlite3` 파일로 저장됩니다

만약 sqlite3 이외의 데이터베이스를 설정할 경우 다음과 같이 수정

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
				'HOST': '127.0.0.1',
      	'USER': 'mydatabaseuser',
      	'PASSWORD': 'password',
        'NAME': 'mydatabase',
        'PORT': 3000
    },
}
```



- settings.py 더 알아보기

**`TIME_ZONE`**을 이용하여 시간대 수정가능

**`INSTALLED_APPS`**는Django 인스턴스에서 활성화된모든 Django 어플리케이션 이름을 가지고 있음. 앱 들은 다수의 프로젝트에서 사용될 수 있고, 다른 프로젝트에서 쉽게 사용도리 수 있도록 패키징하여 배포할 수 있음. 다음은 기본적으로 가지고 있는 INSTALLED_APPS 입니다.

```
django.contrib.admin -- 관리용 사이트. 곧 사용하게 될 겁니다.
django.contrib.auth -- 인증 시스템.
django.contrib.contenttypes -- 컨텐츠 타입을 위한 프레임워크.
django.contrib.sessions -- 세션 프레임워크.
django.contrib.messages -- 메세징 프레임워크.
django.contrib.staticfiles -- 정적 파일을 관리하는 프레임워크.
```

이러한 기본 어플리케이션 중 몇몇은 하나 이상의 데이터베이스 테이블을 사용하는데, 그러기 위해서는 데이터베이스에서 테이블을 미리 만들필요가 있음. 이때는 다음 명령어를 이용

```bash
$ python manage.py migrate
```

**`migrate`** 명령어는 INSTALLED_APPS의 설정을 탐색하여, mysite/settings.py의 데이터베이스 설정과 app과 함께 제공되는 데이터베이스에 따라 필요한데이터베이스 테이블을 생성. migrate는 INSTALLED_APPS에 등록된 어플리케이션에 한하여 실행



- 모델

```python
# polls/models.py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

모델생성

```python
# mysite/settings.py
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

앱 추가

PollsConfig 클래스는 polls/apps.py 파일 내에 존재. 

```bash
$ python manage.py makemigrations polls

Migrations for 'polls':
  polls/migrations/0001_initial.py:
    - Create model Choice
    - Create model Question
    - Add field question to choice
```

**` makemigrations`**는 모델을 변경시킨 사실과(새로 만든것도 포함) 이 변경사항을 migration으로 저장시키고 싶다는 걸 django에게 알림

migration은 Django가 모델의 변경사항을 저장하는 방법으로 디스크상의 파일로 존재. **`polls/migrations/0001_initial.py`** 파일로 저장된 새 모델에 대한 migration을 읽어볼 수 있음. **`migrate`**는 migration을 실행시켜주고, 자동으로 데이터베이스 스키마를 관리해주는 명령어

0001_x.py에서 0001 숫자는 순차적으로 늘어난다. 또생 새롭게 생성됬는지, 수정됬는지 삭제 됬는지에 따라 x자리에 initial, remove 등이 온다.

```bash
$ python manage.py sqlmigrate polls 0001
```

```sql
BEGIN;
--
-- Create model Choice
--
CREATE TABLE "polls_choice" (
    "id" serial NOT NULL PRIMARY KEY,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL
);
--
-- Create model Question
--
CREATE TABLE "polls_question" (
    "id" serial NOT NULL PRIMARY KEY,
    "question_text" varchar(200) NOT NULL,
    "pub_date" timestamp with time zone NOT NULL
);
--
-- Add field question to choice
--
ALTER TABLE "polls_choice" ADD COLUMN "question_id" integer NOT NULL;
ALTER TABLE "polls_choice" ALTER COLUMN "question_id" DROP DEFAULT;
CREATE INDEX "polls_choice_7aa0f6ee" ON "polls_choice" ("question_id");
ALTER TABLE "polls_choice"
  ADD CONSTRAINT "polls_choice_question_id_246c99a640fbbd72_fk_polls_question_id"
    FOREIGN KEY ("question_id")
    REFERENCES "polls_question" ("id")
    DEFERRABLE INITIALLY DEFERRED;

COMMIT;
```

```bash
$ python manage.py migrate
```

migrate 하게되면 `INSTALLED_APPS`에 추가된 앱에서 앞에서 생성한 migrations/*.py에서 적용되지 않은 순으로 적용시킨다.

- 정리

1. `models.py`에서 모델 생성 및 변경, 삭제
2. `python manage.py makemigrations [앱 이름]`를 통해 변경사항에 대한 마이그레이션 생성
3. `python manage.py migrate`를 통해 변경사항을 데이터베이스에 적용

이때 `python manage.py sqlmigrate polls 0001`의 형태로 해당 마이그레이션에서 실행될 sql 구문확인할 수 있음. polls은 앱 이름이며 0001은 makemigrations로 생성된 파일 넘버링

# 데이터베이스 API 가지고 놀기

Django를 좀 더 유연하게 가지고 놀 수 있는 쉘을 다뤄봄

```bash
$ python manage.py shell
```

