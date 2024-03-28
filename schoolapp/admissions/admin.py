from django.contrib import admin
from admissions.models import student

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display=['id']


admin.site.register(student,studentAdmin)
