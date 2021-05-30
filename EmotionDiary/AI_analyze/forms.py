from django import forms
from . import models


class UserInformFrom(forms.ModelForm):
    class Meta:
        model = models.UserInform
        fields = ['line_id', 'username', 'gender', 'birth', 'career_id']
        widgets = {
            'line_id': forms.TextInput(attrs={'id': 'userid', 'name': 'userid', 'type': 'hidden'}),
            'username': forms.TextInput(attrs={'id': 'disname', 'name': 'username', 'class': 'nametextbox', 'type': 'text', 'size': '20', 'maxlength': '20'}),
            'birth': forms.TextInput(attrs={'id': 'birth', 'class': 'agetextbox','name': 'agetextbox', 'type': 'date'}),
            'gender': forms.TextInput(attrs={'id': 'gender', 'type': 'text'}),
            'career_id': forms.TextInput(attrs={'id': 'job', 'type': 'hidden'}),
        }


