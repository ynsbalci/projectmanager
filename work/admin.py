from django.contrib import admin
from .models import Work

class WorkAdmin(admin.ModelAdmin):
    list_display = ['w_id',
                    'w_task',
                    'w_employee',
                    ]
                    
    # list_display_links = ['p_name']
    
    class Meta:
        model = Work


# Register your models here.
admin.site.register(Work, WorkAdmin)
