from django.shortcuts import render
from fakerApp.models import Student
def view(r):
    s=Student.objects.all()
    d={'stud':s}
    return render(r,'fakerApp/1.html',d)
