from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.


def setPass(request):
    if request.user.is_authenticated:
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # update password
            update_session_auth_hash(request, form.cleaned_data['user'])
            return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, './change_pass.html', {'form': form})
    else:
        return redirect('login')


def changePass(request):
    if request.user.is_authenticated:
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # update password
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, './change_pass.html', {'form': form})
    else:
        return redirect('login')


def signout(request):
    logout(request)
    return redirect('login')


def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                # if user exist in database
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    # navigate to profile
                    return redirect('profile')
        else:
            form = AuthenticationForm()

        return render(request, './login.html', {'form': form})

    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        return render(request, './profile.html', {'user': request.user})
    return redirect('login')


def home(request):
    return render(request, './home.html')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account is created successfully')
                # messages.warning(request, 'Account is created successfully')
                # messages.info(request, 'Account is created successfully')
                form.save(commit=True)
                return redirect('profile')
        else:
            form = RegisterForm()
        return render(request, './signup.html', {'form': form})
    else:
        return redirect('profile')
