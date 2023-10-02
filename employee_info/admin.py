from django.contrib import admin
from .models import Department , Information

# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department',)


@admin.register(Information)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'gender', 'age', 'elevel', 'department')