from django import forms
from .models import Tweet,comment,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):

    class Meta:
        model=Tweet
        fields=['text','photo']
        

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model=comment
        fields=['tweet_comment']
        widgets = {
            'tweet_comment': forms.Textarea(attrs={
                'placeholder': 'Write a comment...',
                'rows': 1,
                'class': 'flex-1 border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 resize-none overflow-hidden'

            })
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profile_pic','bio','location']
        

        def __init__(self, *args, **kwargs):
            super(ProfileForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs.update({
                    'class': 'w-full mt-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-pink-500'
                })
