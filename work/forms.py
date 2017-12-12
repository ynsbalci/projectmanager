from django import forms
from .models import Work


class AddForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = [
            'w_task',
        ]

#
