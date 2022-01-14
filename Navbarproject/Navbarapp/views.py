from django.shortcuts import render

def enquiryview(request):
    template_name = 'Navbarapp/navbar.html'
    return render(request,template_name)

def homeview(request):
    template_name = 'Navbarapp/home.html'
    return render(request,template_name)






