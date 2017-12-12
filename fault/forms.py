from django import forms
from .models import Fault


class AddForm(forms.ModelForm):

    class Meta:
        model = Fault
        fields = [
            'f_name',
            'f_task',
            'f_defination',
        ]


class UpdateForm(forms.ModelForm):

    class Meta:
        model = Fault
        fields = [
            'f_name',
            'f_status',
            'f_defination',
        ]




