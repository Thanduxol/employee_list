from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['first_name', 'last_name']}),
        ('Job Information',
         {'fields': ['job_title', 'description']}),
        ('Publication Date',
         {'fields': ['employment_date']}),
        ('Image',
         {'fields': ['photo']}),
    ]
    list_display = ('first_name', 'last_name')
    list_filter = ['employment_date']
    search_fields = ['first_name', 'last_name']


admin.site.register(Employee, EmployeeAdmin)
