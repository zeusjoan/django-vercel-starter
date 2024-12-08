from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import django
import sys
from .forms import UserRegistrationForm

def home(request):
    context = {
        'title': 'Dashboard',
        'django_version': django.get_version(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'debug': settings.DEBUG
    }
    return render(request, 'main/home.html', context)

@login_required
def profile(request):
    return render(request, 'main/profile.html', {
        'title': 'Profile'
    })

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now login.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {
        'form': form,
        'title': 'Register'
    })
