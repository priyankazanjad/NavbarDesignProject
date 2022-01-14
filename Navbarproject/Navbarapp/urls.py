from django.urls import path
from . import views

urlpatterns = [
    path('enq/',views.enquiryview,name='enquiry'),
    path('ho/',views.homeview,name='home'),
]