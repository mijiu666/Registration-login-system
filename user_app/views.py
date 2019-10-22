from django.contrib.auth.hashers import check_password, make_password
from django.db.models import Q
from django.shortcuts import render,redirect
from user_app.models import UserInfo

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("passwd")
        sex = request.POST.get("sex")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        birthday = request.POST.get("date")

        UserInfo.objects.create(
            username=username,
            password=make_password(password),
            sex=sex,
            phone=phone,
            birthday=birthday,
            email=email
        )
        return redirect("/login/")
    return render(request,"demo1.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_objs = UserInfo.objects.filter(Q(username=username) | Q(email=username) | Q(phone=username))
        UserInfo.objects.filter(Q(username=username) | Q(email=username) | Q(phone=username))
        if user_objs and check_password(password, user_objs[0].password):
            return render(request, "index.html")
    return render(request,"login.html")

def test(request):
    return render(request,"test.html")