from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request, 'Web/dashboard.html')

def contact(request):
    return render(request, 'Web/contact.html')

def ratings(request):
    return render(request, 'Web/ratings.html')

def about(request):
    return render(request, 'Web/about.html')

def index(request):
    return render(request, 'Web/dashboard.html')

def shop(request):
    return render(request, 'Web/shop.html')