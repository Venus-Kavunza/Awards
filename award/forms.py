from django import forms
from .models import Posts,Ratings,UserProfile
from django.forms.widgets import Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignupForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User  
        fields= ['username','email','password1','password2']
        
        help_texts = { 'username': None, 'password2': None, }


User._meta.get_field('email')._unique = True 

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'profile_picture', 'bio', 'phone_number']
        
        widgets = {
            'bio': Textarea(attrs={'cols': 20, 'rows': 5}),
        }

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ['design', 'usability', 'content']

class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('photo', 'title', 'url', 'description', 'technologies_used',)