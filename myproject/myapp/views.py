from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Cat
from django.db.models.functions import Lower

def index(request):
    # return render(request, 'index.html'
    # students = Student.objects.all()
    students = Student.objects.order_by(Lower('secondName'))
    cats = Cat.objects.all().order_by("name")

    return render(request, 'index.html',{'students':students} )


def pets(request):
    cats = Cat.objects.all().order_by("name")
    return render(request, 'pets.html',{'cats':cats} )

