from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display=['username','college_name','std_cell_no','college_name','emai_id']
    class meta:
        model=Student

admin.site.register(Student,StudentAdmin)
