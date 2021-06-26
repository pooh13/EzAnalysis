from django import forms
from . import models


class UserInformFrom(forms.ModelForm):
    class Meta:
        model = models.UserInform
        fields = ['line_id', 'username', 'gender', 'birth', 'career_id']
        widgets = {
            'line_id': forms.TextInput(attrs={'id': 'userid', 'name': 'userid', 'type': 'hidden'}),
            'username': forms.TextInput(attrs={'id': 'disname', 'name': 'username', 'class': 'name_textbox', 'type': 'text', 'size': '20', 'maxlength': '20'}),
            'birth': forms.TextInput(attrs={'id': 'birth', 'name': 'agetextbox', 'class': 'age_textbox', 'type': 'date'}),
            'gender': forms.TextInput(attrs={'id': 'gender', 'type': 'hidden'}),
            'career_id': forms.TextInput(attrs={'id': 'job', 'type': 'hidden'}),
        }


class DiaryForm(forms.ModelForm):
    class Meta:
        model = models.Diary
        fields = ['line_id', 'date', 'mood', 'note', 'pic']
        widgets = {
            'line_id': forms.TextInput(attrs={'id': 'userid', 'name': 'userid', 'type': 'hidden'}),
            'mood': forms.TextInput(attrs={'id': 'mood', 'type': 'hidden'}),
        }


