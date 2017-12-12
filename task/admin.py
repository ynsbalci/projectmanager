from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['t_id',
                    't_name',
                    't_project',
                    # 't_defination',
                    't_begin',
                    't_end',
                    't_status',
                    ]

    list_display_links = ['t_name']

    class Meta:
        model = Task



# Register your models here.
admin.site.register(Task, TaskAdmin)