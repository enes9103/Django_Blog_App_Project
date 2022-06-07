from django.contrib.auth.models import User
from .models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email')
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        
class UpdateProfileForm(forms.ModelForm):
   
    portfolio=forms.URLField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'portfolio']

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
    required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']