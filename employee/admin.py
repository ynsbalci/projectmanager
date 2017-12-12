from django.contrib import admin
from .models import Employee
from django.contrib.auth.admin import UserAdmin

class EmployeeAdmin(UserAdmin):
    model = Employee

    # kalıtıma eklediğimz yerleri bildirdik
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': (
        'e_phone',
        'e_date_left',
        'e_qualification',
        'e_salary_rate',
    )}),)


admin.site.register(Employee, EmployeeAdmin)
