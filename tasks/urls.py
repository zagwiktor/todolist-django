from django.urls import path
from .views import tasks_page, login_page, register_page, HomePage, logout_user, TaskDetails, AddTask
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', tasks_page, name="task_page"),
    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register_page"),
    path('home/', login_required(HomePage.as_view()), name="home_page"),
    path('home/<int:pk>', login_required(TaskDetails.as_view()), name="task_details"),
    path('home/addtask>', login_required(AddTask.as_view()), name="add_task"),
    path('logout/', logout_user, name="logout"),
]