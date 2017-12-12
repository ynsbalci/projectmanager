from django.contrib import admin
from .models import Salary

class SalaryAdmin(admin.ModelAdmin):
    list_display = ['s_id',
                    's_date',
                    's_voter',
                    's_choise',
                    's_vote',
                    ]

    class Meta:
        model = Salary


# Register your models here.
admin.site.register(Salary, SalaryAdmin)
