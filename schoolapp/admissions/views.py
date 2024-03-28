from django.shortcuts import render
# from django.http import HttpResponse
from admissions.models import student
from admissions.forms import studentModelForm

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def admissions1(request):
    # values = {'Name':'Kalyani','Age':23,'Adress':'hyd'}
    form=studentModelForm
    studentform={'form':form}
    return render(request,'admissions/newadmissions.html',studentform)

def admissions2(request):
    # values = {'Name':'Kalyani','Age':23,'Adress':'hyd'}
    result = student.objects.all()#select*from student
    students={'allstudents':result}
    return render(request,'admissions/oldadmissions.html',students)
 



 