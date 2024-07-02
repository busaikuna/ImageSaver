from django import forms
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Image, Users


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = None
            
    class Meta:
        model = Users
        fields = ('email', 'username', 'password1')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = {'legend', 'image'}
        labels = {'image': "Image", "legend": 'legenda'}

