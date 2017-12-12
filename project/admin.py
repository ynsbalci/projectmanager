from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['p_id',
                    'p_name',
                    # 'p_defination',
                    'p_type',
                    'p_begin',
                    'p_end',
                    'p_manager',
                    'p_status',
                    ]

    list_display_links = ['p_name']
    #list_filter = ['publishing_date']
    #search_fields = ['title', 'content']
    #list_editable = ['title']

    class Meta:
        model = Project
        

# Register your models here.
admin.site.register(Project, ProjectAdmin)
