from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CreateNewUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Task


# Create your views here.
def tasks_page(request):
    return render(request, "tasks/tasks.html")


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, "tasks/login.html")


def logout_user(request):
    logout(request)
    return redirect('login_page')


def register_page(request):
    form = CreateNewUser()

    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f"User: {user}, was created")
            return redirect('login_page')

    context = {'form': form}
    return render(request, "tasks/register.html", context)



class HomePage(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/home.html'


class TaskDetails(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_details.html'


class AddTask(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'tasks/add.html'
    success_url = reverse_lazy('home_page')


