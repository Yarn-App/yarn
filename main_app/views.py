from django.shortcuts import render, redirect


# Authentication Related Views
def get_user_registration(request):
    return render(request, 'authentication/register.html')


def save_user_registration(request):
    return redirect('/dashboard')


def get_user_login(request):
    return render(request, 'authentication/login.html')


def authenticate_login(request):
    return redirect('/dashboard')


# Home Page & generic pages
def index(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about.html')


# Dashboard & User Profile
def user_dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def user_profile(request):
    return render(request, 'dashboard/profile.html')


def update_user_profile(request):
    return redirect('/dashboard')


# Yarn Related Views
def get_yarn_form(request):
    return render(request, 'yarn/yarn_form.html')


def save_yarn(request):
    return redirect('/')


# Thread Related Views
def get_thread_form(request):
    return render(request, 'thread/thread_form.html')


def save_thread(request):
    return redirect('/')
