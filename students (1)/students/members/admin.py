from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'gender',
        'branch',
        'year',
        'cgpa',
    )

    search_fields = (
        'name',
        'branch',
        'city',
    )

    list_filter = (
        'gender',
        'branch',
        'year',
    )

# admin.site.register(Student)