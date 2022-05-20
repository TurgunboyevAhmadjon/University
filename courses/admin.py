from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

# admin.site.register(Speciality)
# admin.site.register(Teacher)
# admin.site.register(Subject)
# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(ModelAdmin):
    search_fields = ('first_name', 'last_name',)
    list_filter = ('first_name', 'degree',)
    list_display = ('first_name', 'last_name', 'degree',)

@admin.register(Speciality)
class SpecialityAdmin(ModelAdmin):
    list_filter = ('id','name', 'code',)
    search_fields = ('start_code',)
    list_display = ('code','name', 'start_date', 'is_active',)

@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    search_fields = ('name',)
    # autocomplete_fields = ('Speciality', 'Teacher',)