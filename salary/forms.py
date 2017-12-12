from django import forms
from .models import Salary


class AddForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = [
            's_choise',
            's_vote',
        ]



