from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def admissions1(request):
    values = {'Name':'Kalyani','Age':23,'Adress':'hyd'}
    return render(request,'admissions/newadmissions.html',values)

def admissions2(request):
    values = {'Name':'Kalyani','Age':23,'Adress':'hyd'}
    return render(request,'admissions/oldadmissions.html',values)
 



 