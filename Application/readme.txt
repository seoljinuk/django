----------------------------------------------------------------------------
data = [
        {"item": "장편", "cnt": 4913},
        {"item": "단편", "cnt": 3316},
        {"item": "옴니버스", "cnt": 591},
        {"item": "기타", "cnt": 106}
    ]
를 사용하여 데이터를 보여주는 장고 프로젝트를 생성하세요.
----------------------------------------------------------------------------
드라이브 D에 DjangoProject를 생성합니다.
Interpreter type : Project venv
Python version : 312버전

DjangoProject 내에서 진행
Terminal 창을 엽니다.
다음과 같이 Django를 설치합니다.
	pip install django

장고 관리자
	다음 명령어로 실습을 위한 Crawling 프로젝트를 생성합니다.
	django-admin startproject Crawling
	상위/하위에 Crawling 폴더가 생성되는 데 상위 폴더는 단순 파일을 합쳐 놓은 역할을 합니다.
	이름을 임의로 바꿔도 상관이 없으므로 다음과 같이 변경하도록 합니다.
		ren Crawling Application


Crawling\settings.py
	DATABASES 영역의 'db.sqlite3' → 'crawling.sqlite3'으로 변경


Application 하위 폴더로 이동
	cd .\Application\
	앱은 Django 프로젝트 내에서 특정 기능을 수행하는 모듈입니다.
	우리는 영화 진흥 위원회를 위한 kmdb 앱을 생성하도록 합니다.
	python manage.py startapp kmdb

프로젝트에 앱 추가하기
	생성된 앱을 프로젝트의 설정 파일에 추가합니다.
	Crawling/settings.py 파일을 열어 INSTALLED_APPS 리스트에 kmdb을 추가합니다.
		INSTALLED_APPS = [
			...
			'kmdb',
		]

URL 설정
	프로젝트의 URL 설정을 업데이트하여 앱의 뷰를 연결합니다.

	프로젝트 URL 설정
		Crawling/urls.py 파일을 열어 kmdb의 URL을 포함하도록 수정합니다.
			from django.contrib import admin
			from django.urls import path, include

			urlpatterns = [
				path('admin/', admin.site.urls),
				path('', include('kmdb.urls')),
			]

	앱 URL 설정
		kmdb 디렉토리 안에 urls.py 파일을 생성하고 아래 내용을 추가합니다.
			from django.urls import path
			from . import views

			urlpatterns = [
				path('', views.index, name='index'),
			]

뷰 생성
kmdb/views.py 파일을 열어 아래 내용을 추가합니다.

from django.shortcuts import render

def index(request):
    data = [
        {"item": "장편", "cnt": 4913},
        {"item": "단편", "cnt": 3316},
        {"item": "옴니버스", "cnt": 591},
        {"item": "기타", "cnt": 106}
    ]
    return render(request, 'index.html', {'data': data})

템플릿 생성
kmdb 디렉토리 안에 templates 디렉토리를 만들고 그 안에 index.html 파일을 생성합니다.
index.html 파일
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Item List</title>
</head>
<body>
    <h1>Item List</h1>
    <ul>
        {% for item in data %}
            <li>{{ item.item }}: {{ item.cnt }}</li>
        {% endfor %}
    </ul>
</body>
</html>


데이터베이스 마이그레이션
Django는 데이터베이스를 사용합니다.
초기 설정을 위해 데이터베이스 마이그레이션을 실행합니다.

python manage.py migrate

서버 실행
개발용 서버를 실행하여 프로젝트가 정상적으로 작동하는지 확인합니다.

python manage.py runserver

웹 브라우저에서 http://127.0.0.1:8000/에 접속하면 JSON 데이터가 웹 페이지에 표시된 것을 확인할 수 있습니다.
----------------------------------------------------------------------------
영화 진흥회 데이터를 위한 테이블을 만들어 주세요.
----------------------------------------------------------------------------
kmdb\models.py
    Movie 클래스를 구현합니다.

데이터베이스 마이그레이션
    모델을 생성한 후, SQLite 데이터베이스에 테이블을 생성해야 합니다.
    마이그레이션 파일 생성:
        python manage.py makemigrations
    마이그레이션 적용 (테이블 생성):
    python manage.py migrate

crawling.sqlite3 파일에 movies 테이블이 생성되었습니다.
테이블을 확인합니다.
----------------------------------------------------------------------------

----------------------------------------------------------------------------

----------------------------------------------------------------------------

----------------------------------------------------------------------------

----------------------------------------------------------------------------

----------------------------------------------------------------------------

----------------------------------------------------------------------------