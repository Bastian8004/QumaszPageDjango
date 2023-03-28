from django import forms
from .models import Post, Opinion


class PostForm(forms.ModelForm):

    title = forms.CharField(help_text='maksymalnie 200 znaków')

    class Meta:
        model = Post
        fields = ['title','text','image']


class OpinionForm(forms.ModelForm):

    title = forms.CharField(help_text='maksymalnie 200 znaków')

    class Meta:
        model = Opinion
        fields = ['author','text']