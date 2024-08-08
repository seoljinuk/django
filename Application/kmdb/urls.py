from django.urls import path  # Django의 URL 관리 모듈을 임포트합니다.
from . import views          # 현재 디렉토리의 views 모듈을 임포트합니다.

# URL 패턴 리스트를 정의합니다.
urlpatterns = [
    path('', views.index, name='index'), # 기본 URL ('/')에 대해 views.index 뷰를 호출합니다.
                                          # 이 URL 패턴의 이름은 'index'입니다.
]