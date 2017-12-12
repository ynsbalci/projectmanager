from django import forms
from .models import Project
from vote.models import Vote
from task.models import Task


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'p_name',
            'p_type',
            'p_begin',
            'p_end',
            'p_defination',

        ]


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'p_name',
            'p_type',
            'p_begin',
            'p_end',
            'p_manager',
            'p_defination',

        ]


class ProjectVoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = [
            'v_vote',
        ]


class ProjectTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            't_name',
            't_defination',
            't_end',

        ]
#asd


