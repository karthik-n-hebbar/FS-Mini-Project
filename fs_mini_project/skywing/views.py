from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def home(request):
#     file_path = 'static/flights.txt'

#     # For Departure Cities
#     departure_cities = []

#     with open(file_path, 'r') as file:
#         for line in file:
#             fields = line.split('|')
#             departure_city = fields[3].strip().split(': ')[1]  # Extract only the city name
#             departure_cities.append(departure_city)

#     departure_cities = list(set(departure_cities))  # Remove duplicate departure cities

#     # For Arrival Cities
#     arrival_cities = []

#     with open(file_path, 'r') as file:
#         for line in file:
#             fields = line.split('|')
#             arrival_city = fields[5].strip().split(': ')[1]  # Extract only the city name
#             arrival_cities.append(arrival_city)

#     arrival_cities = list(set(arrival_cities))  # Remove duplicate arrival cities

#     context = {'arrival_cities': arrival_cities, 'departure_cities': departure_cities}

#     return render(request, 'home.html', context)


def home(request):
    file_path = 'static/flights.txt'

    # For Departure Cities
    departure_cities = []

    with open(file_path, 'r') as file:
        for line in file:
            fields = line.split('|')
            departure_city = fields[3].strip().split(': ')[1]  # Extract only the city name
            departure_cities.append(departure_city)

    departure_cities = list(set(departure_cities))  # Remove duplicate departure cities

    context = {'departure_cities': departure_cities}

    if request.method == 'POST':
        departure_city = request.POST.get('departure_city')

        # For Arrival Cities
        arrival_cities = []

        with open(file_path, 'r') as file:
            for line in file:
                fields = line.split('|')
                current_departure_city = fields[3].strip().split(': ')[1]
                current_arrival_city = fields[5].strip().split(': ')[1]
                if current_departure_city == departure_city:
                    arrival_cities.append(current_arrival_city)

        arrival_cities = list(set(arrival_cities))  # Remove duplicate arrival cities

        context['arrival_cities'] = arrival_cities
        context['selected_departure'] = departure_city

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