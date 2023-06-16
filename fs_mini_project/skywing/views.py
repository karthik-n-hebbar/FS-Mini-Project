from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    file_path = 'static/flights.txt' 

    # For Departure Cities

    departure_cities = []

    with open(file_path, 'r') as file:
        for line in file:
            fields = line.split('|')
            departure_city = fields[3].strip().split(': ')[1]  # Extract only the city name
            departure_cities.append(departure_city)

    # context_1 = {'departure_cities': departure_cities}

    # For Arrival Cities

    arrival_cities = []

    with open(file_path, 'r') as file:
        for line in file:
            fields = line.split('|')
            arrival_city = fields[5].strip().split(': ')[1]  # Extract only the city name
            arrival_cities.append(arrival_city)

    context = {'arrival_cities': arrival_cities, 'departure_cities': departure_cities}

    return render(request, 'home.html', context)

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
    