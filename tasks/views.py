from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CreateNewUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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


@login_required(login_url='login')
def home_page(request):
    return render(request, "tasks/home.html")
