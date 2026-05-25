from django import forms
from .models import comment
class CommentForm(forms.ModelForm):
    class Meta:
        exclude = {"post"}
        labels = {"user_name":"your name","email_addr":"email"}