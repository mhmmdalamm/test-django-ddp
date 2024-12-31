from django.shortcuts import render
from django.http import HttpResponse

def salam(request):
    return HttpResponse("Selamat Belajar")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')