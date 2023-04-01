from django import forms
from .models import info, FilesUpload
from django.forms import ModelForm



class InfoForm(ModelForm):
    class Meta:
        model = info
        fields = ['name', 'years_playing', 'genter', 'discord', 'facebook', 'instagram', 'Class', 'edition', 'discription', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class' : "form-control form-control-lg",
                'placeholder' : 'Enter your full name'
                }),
            'edition' : forms.Select(attrs={
                'class' : "form-control form-control-lg",
                'placeholder' : 'Select the edition you want to play'
                }),
            'Class' : forms.Select(attrs={
                'class' : "form-control form-control-lg",
                'placeholder': 'Select the class you want to play'
                }),
            'discription' : forms.Textarea(attrs={
                'class' : "form-control form-control-lg",
                'rows' : 3,
                'placeholder' : 'Write a short discription about yourself so people will get to know you...'
                }),
                'discord': forms.TextInput(attrs={
                'class' : "form-control form-control-lg",
                'placeholder' : 'Enter your discord account'
                }),
                'facebook': forms.TextInput(attrs={
                'class' : "form-control form-control-lg",
                'placeholder' : 'Enter your facebook account'
                }),
                'instagram': forms.TextInput(attrs={
                'class' : "form-control form-control-lg",
                'placeholder' : 'Enter your instagram account'
                }),
                'genter': forms.Select(attrs={
                'class' : "form-control form-control-lg",
                'placeholder' : 'Select your gender'
                }),
                'years_playing': forms.TextInput(attrs={
                'class' : "form-control form-control-lg",
                'placeholder' : 'How experianced are you?(In years)'
                }),
            }
