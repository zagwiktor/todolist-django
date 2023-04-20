from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_page, name="task_page"),
    path('login/', views.login_page, name="login_page"),
    path('register/', views.register_page, name="register_page"),
    path('home/', views.home_page, name="home_page"),
    path('logout/', views.logout_user, name="logout"),
]