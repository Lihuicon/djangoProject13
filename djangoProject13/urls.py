from django.urls import path
from todo import views
from todo.views import StudentList

urlpatterns = [
    # 其他URL配置...
    path('api/login/', views.login, name='login'),
    path('api/students/', StudentList.as_view(), name='student-list'),
]
