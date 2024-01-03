from django.shortcuts import render,redirect
# from . import forms 
from .forms import userChange, RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login, logout, update_session_auth_hash


# Create your views here.
def signup(req):
    if not req.user.is_authenticated:
        if req.method=='POST':
            reg_form = RegisterForm(req.POST)
            if reg_form.is_valid():
                messages.success(req, 'account creatd successfully')
                reg_form.save()
                print(reg_form.cleaned_data)
        else:
            reg_form = RegisterForm()
        return render(req, 'signup.html', {'form': reg_form})
    else:
        return redirect('profile')


def user_login(req):
    if not req.user.is_authenticated:
        if req.method == 'POST':
            login_form = AuthenticationForm(request=req, data = req.POST)
            if login_form.is_valid():
                name = login_form.cleaned_data['username']
                userpass = login_form.cleaned_data['password']
                user = authenticate(username=name, password = userpass)
                if user is not None:
                    login(req, user)
                    return redirect('profile')
        else:
            login_form = AuthenticationForm()
        return render(req, 'login.html', {'form':login_form})
    else:
        return redirect('profile')

def profile(req):
    if req.user.is_authenticated:
        if req.method=='POST':
            update_form = userChange(req.POST, instance= req.user)
            if update_form.is_valid():
                messages.success(req, 'account Updated successfully')
                update_form.save()
        else:
            update_form = userChange(instance= req.user)
        return render(req, 'profile.html', {'form': update_form})
    else:
        return redirect('signup')


def userLogout(req):
    logout(req)
    return redirect('login')

def pass_change(req):
    if req.method == 'POST':
        form = PasswordChangeForm(user=req.user, data = req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user = req.user)
    return render(req, 'passchange.html', {'form': form})

def changeuser(req):
    if req.user.is_authenticated:
        if req.method=='POST':
            update_form = userChange(req.POST, instance= req.user)
            if update_form.is_valid():
                messages.success(req, 'account Updated successfully')
                update_form.save()
                print(update_form.cleaned_data)
        else:
            update_form = userChange()
        return render(req, 'profile.html', {'form': update_form})
    else:
        return redirect('signup')