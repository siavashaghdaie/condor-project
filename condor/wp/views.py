from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'wp/home.html')

def company(request):
    return render (request, 'wp/company.html')

def contact(request):
    return render (request, 'wp/contact.html')

def knowHow(request):
    return render (request, 'wp/know-how.html')

def news(request):
    return render (request, 'wp/news.html')

def solutions(request):
    return render (request, 'wp/solutions.html')