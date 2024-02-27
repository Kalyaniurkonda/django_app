from django.urls import path
from finance.views import finance1
from finance.views import finance2

urlpatterns = [
    path('paybill/',finance1),
    path('due/',finance2),
     
 ]