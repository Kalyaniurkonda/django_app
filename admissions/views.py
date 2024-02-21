from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def admissions1(request):
    return HttpResponse("this is new admissions page")
def admissions2(request):
    return HttpResponse("this is  old admissions  page")



