from django import forms
from tinymce.widgets import TinyMCE
from .models import User


class CustomUserForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'image', 'description', 'is_author')
        widgets = {
            'description': TinyMCE(),
        }


