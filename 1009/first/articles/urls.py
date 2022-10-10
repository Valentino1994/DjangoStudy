from django.urls import path
# 명시적으로 경로 표현하는 것을 Django에서 권장함
from . import views

urlpatterns = [
    # 두번째 인자가 어떤 view 파일을 실행시킬 것인가이다.
    path("index/", views.index, name="index"),
    path("greeting/", views.greeting, name="greeting"),
    path("dinner/", views.dinner, name="dinner"),
    path("throw/", views.throw, name="throw"),
    path("catch/", views.catch, name="catch"),
    # Variable Routing
    path("hello/<str:name>/", views.hello),
]
