from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib import messages
from .forms import UpdateProfileForm, UpdateUserForm, UserForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm


# -----REGİSTER---------
def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()

    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)

        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False)   # commit=False -> User bu aşamada bilinmediği için jayıt beklesin.
            profile.user = user                         # User ataması yapıldı artık kayıt yapabiliriz.
            profile.save()

            login(request, user)                        # Kayıt yaptıktan sonra kullanıcı login olsun.
            messages.success(request, 'Register Successfull!')

            return redirect('home')                     # Kayıt yaptıktan sonra home sayfasına yönlendir.

    context = {
        "form_user": form_user,
        "form_profile": form_profile
    }

    return render(request, 'users/register.html',context)


# -----LOGİN---------
def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')

    return render(request, 'users/user_login.html', {"form":form})

# -----LOGOUT---------
def user_logout(request):
    messages.success(request, 'You logged out!')
    logout(request)
    return redirect('home')

# -----PROFİLE---------
def profile(request,id):
    user = User.objects.get(id=id)
    user_form =  UpdateUserForm(instance=user)
    form = UpdateProfileForm(instance=user)
    profile_pic=UserProfile.objects.filter(user=user)
    
    if request.method == "POST":
        user_form =  UpdateUserForm(request.POST, instance=user)
        
        form = UpdateProfileForm(request.POST, instance=user)
        if form.is_valid():
            user_form.save()
            form.save()
            return redirect("home")
    
    context = {
        "user_form" : user_form,
        "form" : form,
        'profile_pic':profile_pic
    }
    return render(request, "users/profile.html", context)