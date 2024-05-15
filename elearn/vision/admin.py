from django.contrib import admin

# from django.contrib.admin import AdminSite
# from django.utils.translation import ugettext_lazy

from vision.models import course 
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display=['id','name','price','std','cat','cdetail','is_active']
    list_filter=['cat','is_active']

class notesAdmin(admin.ModelAdmin):
    list_display=['id','name','cat','cdata','is_active']
    list_filter=['cat','is_active']

admin.site.register(course,CourseAdmin)
