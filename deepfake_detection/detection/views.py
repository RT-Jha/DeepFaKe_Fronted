from django.shortcuts import render, HttpResponse
from django.conf import settings

# Create your views here.

def index(request):
    context = {
        "var1":"aarti is hot",
        "var2":"love yourself"
    }
    return render(request, 'index.html',{'STATIC_URL':settings.STATIC_URL})

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")