from django.urls import path
from . import views  # views.py에서 함수 가져오기

urlpatterns = [
    path('', views.event_main, name='event_main'),  # /event/
]