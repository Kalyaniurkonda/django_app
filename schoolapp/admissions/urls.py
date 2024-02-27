from django.urls import path
from admissions import views

urlpatterns = [
    path('createadmissions/',views.admissions1),
    path('viewadmissions/',views.admissions2),
     
 ]
 