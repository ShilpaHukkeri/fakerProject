from django.contrib import admin
from fakerApp.models import Student
class StudentAdmin(admin.ModelAdmin):
    l=['name','roll','marks','dob','email']
admin.site.register(Student,StudentAdmin)