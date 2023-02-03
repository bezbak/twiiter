from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.users.models import User
from apps.settings.models import Settings
# Create your views here.

def register(request):
    settings = Settings.objects.latest('id')
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone_number')
        profile_image = request.FILES.get('profile_image')
        gender = request.POST.get('gender')
        if password == confirm_password:
            try:
                user = User.objects.create(username = username, first_name = first_name, last_name = last_name, email = email, phone_number = phone_number, profile_image = profile_image, gender = gender)
                user.set_password(password)
                user.save()       
                user = User.objects.get(username = username)
                user = authenticate(username = username, password = password)
                login(request, user)
                return redirect('index')
            except:
                return redirect('register')
    context = {
        'settings':settings
    }
    return render(request, 'form-register.html', context)

def user_login(request):
    settings = Settings.objects.latest('id')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        user = authenticate(username = username, password = password)
        login(request,user)
        return redirect('index')
    context = {
        'settings':settings
    }
    return render(request, 'form-login.html', context)