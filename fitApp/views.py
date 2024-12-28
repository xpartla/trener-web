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
    target_groups = [
        {"name": "Začiatočník"},
        {"name": "Pokročilý"},
        {"name": "Kulturistika"},
        {"name": "Silový trojboj"},
        {"name": "Nabranie hmotnosti"},
        {"name": "Kondičná príprava"},
        {"name": "Formovanie"},
        {"name": "Fyzické testy"},
        {"name": "Chudnutie"},
        {"name": "Šport"},
    ]
    context = {"target_groups": target_groups}
    return render(request, 'training.html', context)

def show_coaching(request):
    return render(request, 'coaching.html')