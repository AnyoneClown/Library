from authentication.models import CustomUser
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

def index_users(request):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    context = {"user":request.user, "users_active": "active"}
    return render(request, "index_users.html",context=context)
def user_by_id(request, user_id):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    if request.user.id != user_id and request.user.role != 1:
        return HttpResponse("<h1>You can't see this user's profile</h1>")
    user_data = CustomUser.objects.get(id=user_id)
    context = {"user_data": user_data, "user": request.user, "users_active": "active"}
    return render(request, "user_by_id.html",context=context)

def all_users(request):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    if request.user.role != 1:
        return HttpResponse("<h1>Only admins allowed</h1>")
    users = CustomUser.objects.all()
    context = {"users": users, "users_active": "active"}
    return render(request, "all_users.html",context=context)

def update_user(request, user_id):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    if request.user.id != user_id and request.user.role != 1:
        return HttpResponse("<h1>You can't see this user's profile</h1>")
    first_name,middle_name,last_name,role = None,None,None,None

    user = CustomUser.get_by_id(user_id)
    if user.first_name != request.POST["first_name"]:
        first_name = request.POST["first_name"]
    if user.middle_name != request.POST["middle_name"]:
        middle_name = request.POST["middle_name"]
    if user.last_name != request.POST["last_name"]:
        last_name = request.POST["last_name"]
    try:
        if user.role != request.POST["user_role"]:
            role = request.POST["user_role"] 
    except:
        pass
    user.update(first_name=first_name, last_name=last_name, middle_name=middle_name, role=role)
    return redirect("user_by_id", user.id)

def delete_user(request, user_id):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    if request.user.role != 1:
        return HttpResponse("<h1>Only admins allowed</h1>")
    CustomUser.delete_by_id(user_id=user_id)
    return redirect("all_users")

def update_password(request, user_id):
    user = CustomUser.get_by_id(user_id)
    try:
        if user.password != request.POST["password"]:
            user.password = make_password(request.POST["password"]) 
            user.save()
    except:
        pass
    return redirect("login_user")
