from django.urls import path
from todo import views

urlpatterns = [
    # 其他URL配置...
    path('api/login/', views.login, name='login'),
]
