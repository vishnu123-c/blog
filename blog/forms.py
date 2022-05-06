from dataclasses import fields
from pyexpat import model
from django import forms
from .models import post

class NewPostForm(forms.ModelForm):
    class Meta :
        model=post
        fields=('title','content')