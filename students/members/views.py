from django.shortcuts import render
from .models import Student

# def index(request):
#     data=Student.objects.all().order_by('id')
#     a={
#         "data":data
#     }
#     return render(request,'')
def home(request):
    return render(request, 'home.html')


def table(request):
    students = Student.objects.all()
    return render(request, 'table.html', {'students': students})


def cards(request):
    students = Student.objects.all()
    return render(request, 'cards.html', {'students': students})