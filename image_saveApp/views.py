import os
import requests
from django.shortcuts import render, redirect
from .models import Image
from django.conf import settings
from .forms import ImageForm, UserForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    context = {"form": form}
    return render(request, 'signup.html', context)

def login(request):
    return render(request, "login.html")

@login_required
def home(request):
    return render(request, "home.html")

@login_required
def all(request):
    images = Image.objects.filter(user=request.user)
    context = {"images": images}
    return render(request, "all.html", context)

@login_required
def newImage(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)

            new_image.user = request.user

            new_image.image_path = new_image.image.name
            new_image.save()

            return redirect('all')
    else:
        form = ImageForm()

    return render(request, 'newImage.html', {'form': form})