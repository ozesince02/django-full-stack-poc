from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Change 'home' to your homepage URL name
        else:
            return render(request, 'authapp/login.html', {'error': 'Invalid credentials'})
    return render(request, 'authapp/login.html')

# Registration View
def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'authapp/register.html', {'error': 'Username already exists'})
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('login')
        else:
            return render(request, 'authapp/register.html', {'error': 'Passwords do not match'})
    return render(request, 'authapp/register.html')

# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')
