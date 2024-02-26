from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def finance1(request):
    return HttpResponse("<h1>welcome<h1> <h2>this is finance page of girls<h2>")

def finance2(request):
    return HttpResponse("<h1>welcome<h1> <h2>this is finance page of boys<h2>")
    
