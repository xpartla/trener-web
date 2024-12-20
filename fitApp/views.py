from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

def show_superuser_name(request):
    superuser = User.objects.filter(is_superuser=True).first()
    return render(request, 'superuser.html', {'superuser': superuser.username if superuser else "No superuser found"})

def show_index(request):
    return render(request, 'index.html')

def show_diet(request):
    return render(request, 'diet.html')

def show_training(request):
    return render(request, 'training.html')

def show_coaching(request):
    return render(request, 'coaching.html')