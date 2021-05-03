from django import forms
from . import models


class UserInformFrom(forms.ModelForm):
    # career_id = models.Career.objects.get(career_id='career_id')

    class Meta:
        model = models.UserInform
        fields = ['line_id', 'username', 'gender', 'age', 'career_id']

    # def __init__(self, *args, **kwargs):
    #     super(UserInformFrom, self).__init__(*args, **kwargs)
    #     self.fields['career_id'] = models.Career.objects.get(career_id=self.instance.career_id).career_name

