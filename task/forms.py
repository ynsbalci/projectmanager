from django import forms
from .models import Task
from work.models import Work
from fault.models import Fault


class AddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            't_project',
            't_name',
            't_defination',
            't_end',

        ]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            't_name',
            't_status',
            't_defination',
            't_end',
        ]


class TaskWorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = [
        ]


class TaskFaultForm(forms.ModelForm):
    class Meta:
        model = Fault
        fields = [
            'f_name',
            'f_defination',
        ]


