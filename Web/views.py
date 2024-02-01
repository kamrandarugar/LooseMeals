from django.shortcuts import render
from django.http import HttpResponse
from Web.models import Review

# Create your views here.
def dashboard(request):
    return render(request, 'Web/dashboard.html')

def contact(request):
    return render(request, 'Web/contact.html')

def ratings(request):
   reviews = [
       {
          'id': 1,
           'title': 'Some Great Place',
           'description': 'Eat at this place, it is amazing! I ate the calamari and it was the best I have ever had. The service was great and the atmosphere was very nice.',
           'image': 'food/mamouns2.png',
           'location': 'New York, NY',
           'rating': 10,
           'google_maps': 'https://maps.app.goo.gl/ydUp42JeNjMVKM7FA',
       },
       {
           'id': 2,
           'title': 'Another Place',
           'description': "Don't eat here, they only serve hard boiled bricks",
          'image': 'food/mamouns2.png',
           'location': ', Sardinia, Italy',
           'rating': 1.2,
           'google_maps': 'https://maps.app.goo.gl/ydUp42JeNjMVKM7FA',
       },


   ]
   reviews = Review.objects.all()
   return render(request, 'Web/ratings.html', context={'reviews': reviews})

def about(request):
    return render(request, 'Web/about.html')

def index(request):
    return render(request, 'Web/dashboard.html')

def shop(request):
    return render(request, 'Web/shop.html')