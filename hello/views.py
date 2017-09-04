# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User

from django.contrib import auth
from hello.forms import EditProfileForm,info,check
from hello.models import login,detail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def home(request):
    return render(request,'hello/home.html')

def log(request):
    if request.method=="POST":
        form=check(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request,'hello/login.html')
            else:
                render(request, 'hello/login.html')
        else:
            return HttpResponse("NO")

    else:
        form = check()
        args = {'form': form}
        return render(request, 'hello/login.html', args)



def register(request):
    if request.method == "POST":
        form = info(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
            )
            form.save()
            user.save()
            #register_user(request);

            return render(request, 'hello/after_reg.html')

    else:
        form = info()
        args = {'form': form}
        return render(request, 'hello/reg_form.html', args)
    #   return HttpResponse("Welcome")


def view_profile(request):
        args = {'user': request.user}
        return render(request, 'hello/profile.html', args)


def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/hello/profile')
        else:
            return HttpResponse("Form not valid")
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request,'hello/edit_profile.html',args)
