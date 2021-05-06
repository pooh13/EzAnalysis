from django import forms
from . import models


class UserInformFrom(forms.ModelForm):
    class Meta:
        model = models.UserInform
        fields = ['username', 'gender', 'birth', 'career_id']
