from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserForm
from .models import User

# Create your views here.

def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users':users})

def create_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('home'))
    return render(request, 'create_user.html', {'form': form})

def show_user(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'show_user.html', {'user':user})

def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect(reverse('home'))
    return render(request, 'edit_user.html', {'user':user, 'form':form})

def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect(reverse('home'))