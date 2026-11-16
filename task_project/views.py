from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *

def home(request):
    return render(request, 'home.html')

def registration(request):
    if request.method == 'POST':
        data = request.POST
        if data:
            User.objects.create_user(
                username=data['username'],
                password=data['password'],
            )
        else:
            return redirect("registration")
        return redirect("login")
    return render(request, 'registration.html')

def login_user(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(
            request,
            username=data['username'],
            password=data['password']
        )
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            return redirect("login")
    return render(request, 'login.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def create_task(request):
    if request.method == 'POST':
        data = request.POST
        Task.objects.create(
            title=data['title'],
            caption=data['caption'],
            user_id=request.user
        )
        return redirect("my_task")
    return render(request, 'create_task.html')


@login_required
def show_task(request):
    tasks = Task.objects.filter(user_id=request.user)
    return render(request, 'show_task.html', {"tasks": tasks})


@login_required
def update_task(request, id):
    task = Task.objects.get(id=id, user_id=request.user)

    if request.method == 'POST':
        data = request.POST
        task.title = data['title']
        task.caption = data['caption']
        task.save()
        return redirect("my_task")

    return render(request, 'update_task.html', {"task": task})


@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id, user_id=request.user)

    if request.method == 'POST':
        task.delete()
    return redirect("my_task")


@login_required
def complete_task(request, id):
    task = Task.objects.get(id=id, user_id=request.user)

    if request.method == 'POST':
        task.status = not task.status
        task.save()

    return redirect("my_task")