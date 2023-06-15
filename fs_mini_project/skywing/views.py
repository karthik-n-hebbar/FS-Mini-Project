from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    file_path = 'static/flights.txt' 
    lines = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    return render(request, 'home.html', {'lines' : lines} )

    # return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def booking(request):
    return render(request, "booking.html")
    
def flights(request):
    return render(request, "flights.html")

def my_bookings(request):
    return render(request, "my_bookings.html")

def flight_status(request):
    return render(request, "flight_status.html")
    