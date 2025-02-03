from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import BodyPart, Exercises, Tags
from .forms import BodyPartForm

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

def body_part_list(request):
    body_parts = BodyPart.objects.all()
    return render(request, 'components/body_part_list.html', {'body_parts': body_parts})


def body_part_create(request):
    if request.method == "POST":
        form = BodyPartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('body_part_list')
    else:
        form = BodyPartForm()
    return render(request, 'components/body_part_form.html', {'form': form})


def body_part_update(request, pk):
    body_part = get_object_or_404(BodyPart, pk=pk)
    if request.method == "POST":
        form = BodyPartForm(request.POST, instance=body_part)
        if form.is_valid():
            form.save()
            return redirect('body_part_list')
    else:
        form = BodyPartForm(instance=body_part)
    return render(request, 'components/body_part_form.html', {'form': form})


def body_part_delete(request, pk):
    body_part = get_object_or_404(BodyPart, pk=pk)
    if request.method == "POST":
        body_part.delete()
        return redirect('body_part_list')
    return render(request, 'components/body_part_confirm_delete.html', {'body_part': body_part})