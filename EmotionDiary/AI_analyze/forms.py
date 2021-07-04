from django import forms
from . import models


class UserInformFrom(forms.ModelForm):
    class Meta:
        model = models.UserInform
        fields = ['line_id', 'username', 'gender', 'birth', 'career_id']
        widgets = {
            'line_id': forms.TextInput(attrs={'id': 'userid', 'name': 'userid', 'type': 'hidden'}),
            'username': forms.TextInput(attrs={'id': 'disname', 'name': 'username', 'type': 'text', 'class': 'name_textbox', 'size': '20', 'maxlength': '20'}),
            'gender': forms.TextInput(attrs={'id': 'gender', 'type': 'hidden'}),
            'birth': forms.TextInput(attrs={'id': 'birth', 'name': 'agetextbox', 'type': 'date', 'class': 'age_textbox'}),
            'career_id': forms.TextInput(attrs={'id': 'job', 'type': 'hidden'}),
        }


class DiaryForm(forms.ModelForm):
    class Meta:
        model = models.Diary
        fields = ['line_id', 'date', 'mood', 'pic']
        widgets = {
            'line_id': forms.TextInput(attrs={'id': 'userid', 'name': 'userid', 'type': 'hidden'}),
            'date': forms.TextInput(attrs={'id': 'diary_date', 'type': 'hidden'}),
            'mood': forms.TextInput(attrs={'id': 'mood', 'type': 'hidden'}),
            'pic': forms.FileInput(attrs={'id': 'photo', 'name': 'pic', 'onchange': 'readURL(this);'}),
        }


