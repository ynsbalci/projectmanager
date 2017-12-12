from django.contrib import admin
from .models import Vote


class VoteAdmin(admin.ModelAdmin):
    list_display = ['v_id',
                    'v_project',
                    'v_voter',
                    'v_vote',

                    ]


    # list_display_links = ['p_name']

    class Meta:
        model = Vote



# Register your models here.
admin.site.register(Vote, VoteAdmin)