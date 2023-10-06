from django.shortcuts import render, redirect
from .forms import SignUp, UserInfoForm, UserProfileForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account created for {username}! Login now')
            return redirect('login')
    else:
        form = SignUp()
    return render(request, 'user_register/signup.html', {'form':form})


def profile(request):
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            return redirect('profile')
    else:
        user_form = UserInfoForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    return render(request, 'user_register/profile.html', {'u_form':user_form, 'p_form':profile_form})


class SignIn(LoginView):
    template_name = 'user_register/login.html'


class SignOut(LogoutView):
    template_name = 'user_register/logout.html'