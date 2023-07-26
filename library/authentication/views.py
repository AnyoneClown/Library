# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import auth, messages
from .models import CustomUser
from .forms import *

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from .serializers import *

@permission_classes([IsAdminUser])
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            role = form.cleaned_data['role']

            if password == confirm_password:
                if CustomUser.objects.filter(email=email).exists():
                    messages.info(request, 'Email is already taken')
                    return redirect('register')
                else:
                    if role == 1:
                        user = CustomUser.objects.create_superuser(email=email, password=password, first_name=first_name, middle_name=middle_name, last_name=last_name, role=role)
                        user.save()
                        return redirect('login_user')
                    else:
                        user = CustomUser.objects.create_user(middle_name=middle_name, password=password, email=email, first_name=first_name, last_name=last_name, role=role)
                        user.save()
                        return redirect('login_user')
            else:
                messages.info(request, 'Both passwords do not match')
                return redirect('register')

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            user = CustomUser.objects.authenticate(request=request, email=email, password=password, role=role)

            if user is not None:
                user.is_active = True
                user.save()

                login(request, user)

                return redirect('index')
            else:
                messages.info(request, 'Invalid Email or Password')
                return redirect('login_user')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def logout_user(request):
    user = request.user
    user.is_active = False
    user.save()

    auth.logout(request)
    return redirect('index')

