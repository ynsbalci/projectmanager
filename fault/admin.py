from django.contrib import admin
from .models import Fault


class FaultAdmin(admin.ModelAdmin):
    list_display = ['f_id',
                    'f_name',
                    'f_task',
                    'f_defination',
                    'f_date',
                    'f_status',
                    ]

    list_display_links = ['f_name']
    #list_filter = ['publishing_date']
    #search_fields = ['title', 'content']
    #list_editable = ['title']

    class Meta:
        model = Fault


admin.site.register(Fault, FaultAdmin)
