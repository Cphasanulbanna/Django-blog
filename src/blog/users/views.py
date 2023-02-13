import email
from email import message
from multiprocessing import context
from django.shortcuts import render, reverse

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http.response import HttpResponseRedirect
from posts.models import Author

from users.forms import UserForms
from django.contrib.auth.models import User
from main.functions import generate_form_errors


def login(request):
    if request.method == "POST": 
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request,user)

                return HttpResponseRedirect("/")
        context = {
        "title" : "login",
        "error" : True,
        "message" : "Invaid user or password",
        }
        return render(request, "users/login.html",context=context)
    else:
        context = {
        "title" : "signup",
        }
        return render(request, "users/login.html",context=context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("web:index"))


def signup(request):
    if request.method == "POST":
        form = UserForms(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            user = User.objects.create_user(
                username = instance.username,
                password = instance.password,
                email = instance.email,
                first_name = instance.first_name,
                last_name = instance.last_name,
            )

            Author.objects.create(name=instance.first_name, user=user)

            user = authenticate(request, username=instance.username, password=instance.password)
            auth_login(request,user)

            return HttpResponseRedirect(reverse("web:index"))
        else:
            message = generate_form_errors(form)
            
            form = UserForms()
            context = {
                "title" : "Signup",
                "error" : True,
                "message" : message,
                "form": form,
            }
            return render(request, "users/signup.html", context=context)
    else:
        form = UserForms()
        context = {
            "title" : "signup",
            "form" : form,
        }
        return render(request, "users/signup.html", context=context)