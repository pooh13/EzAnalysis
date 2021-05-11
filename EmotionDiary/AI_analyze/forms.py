from django import forms
from . import models


class UserInformFrom(forms.ModelForm):
    # GENDER_CHOICES = (
    #     ('M', 0),
    #     ('F', 1),
    # )
    class Meta:
        model = models.UserInform
        fields = ['line_id', 'username', 'gender', 'career_id']
        widgets = {
            'line_id': forms.TextInput(attrs={'id': 'userid', 'type': 'hidden'}),
            'username': forms.TextInput(attrs={'id': 'disname', 'class': 'nametextbox', 'type': 'text', 'size': '20', 'maxlength': '20'}),
            # 'birth': forms.TextInput(attrs={'id': 'yearold', 'class': 'agetextbox', 'type': 'text', 'size': '20', 'maxlength': '20'}),
            'gender': forms.TextInput(attrs={'id': 'gender', 'type': 'hidden'}),
            'career_id': forms.TextInput(attrs={'id': 'job', 'type': 'hidden'}),
        }

    # kelly-------------------------------------------------------
    # class Meta:
    #     model = models.UserInform
    #     fields = ['username', 'gender', 'birth', 'career_id']
    # ------------------------------------------------------------

