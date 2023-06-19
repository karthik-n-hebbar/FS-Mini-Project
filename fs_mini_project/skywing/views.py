from django.http import HttpResponse
from django.shortcuts import render, redirect
import csv
import re

# Create your views here.

selected_departure_city = ""
selected_arrival_city = ""
context = {}

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

     # For Arrival Cities
    arrival_cities = []

    with open(file_path, 'r') as file:
        for line in file:
            fields = line.split('|')
            # current_departure_city = fields[3].strip().split(': ')[1]
            current_arrival_city = fields[5].strip().split(': ')[1]
            # if current_departure_city == departure_city:
            arrival_cities.append(current_arrival_city)

        arrival_cities = list(set(arrival_cities))  # Remove duplicate arrival cities

    context['arrival_cities'] = arrival_cities
    context['selected_departure'] = departure_city

    return render(request, 'home.html', context)

def search_flights(request):
    if request.method == 'POST':
        selected_departure_city = request.POST.get('departure_city')
        selected_arrival_city = request.POST.get('arrival_city')

        # departure_city = 'Bangalore'
        # arrival_city = 'Chennai'

        print(selected_departure_city, selected_arrival_city)
        
        # Read flights.txt file and filter flights based on departure and arrival cities
        flights = []
        file_path = 'static/flights.txt'

        with open(file_path, 'r') as file:
            for line in file:
                flight_details = line.split('|')
                flight_number = flight_details[0].split(':')[1].strip()
                airline = flight_details[1].split(':')[1].strip()
                aircraft_type = flight_details[2].split(':')[1].strip()
                departure_city = flight_details[3].split(':')[1].strip()
                departure_airport = flight_details[4].split(':')[1].strip()
                arrival_city = flight_details[5].split(':')[1].strip()
                arrival_airport = flight_details[6].split(':')[1].strip()
                seat_capacity = flight_details[7].split(':')[1].strip()
                    
                # Extract and format departure time
                departure_time_match = re.search(r'Departure Time: (\d{2}:\d{2} [AP]M)', line)
                if departure_time_match:
                    departure_time = departure_time_match.group(1)
                else:
                    departure_time = ""
                    
                # Extract and format arrival time
                arrival_time_match = re.search(r'Arrival Time: (\d{2}:\d{2} [AP]M)', line)
                if arrival_time_match:
                    arrival_time = arrival_time_match.group(1)
                else:
                    arrival_time = ""
                    
                if selected_departure_city == departure_city and selected_arrival_city == arrival_city:
                    flights.append({
                        'flight_number': flight_number,
                        'airline': airline,
                        'aircraft_type': aircraft_type,
                        'departure_city': departure_city,
                        'departure_airport': departure_airport,
                        'arrival_city': arrival_city,
                        'arrival_airport': arrival_airport,
                        'seat_capacity': seat_capacity,
                        'departure_time': departure_time,
                        'arrival_time': arrival_time,
                    })
        
        context = {
            'flights': flights
        }
    return render(request, 'flights.html', context)

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def booking(request):
    if request.method == 'POST':
        posted_flight_number = request.POST.get('flight_number')

        file_path = 'static/flights.txt'

        with open(file_path, 'r') as file:
            for line in file:
                flight_details = line.split('|')
                flight_number = flight_details[0].split(':')[1].strip()
                airline = flight_details[1].split(':')[1].strip()
                aircraft_type = flight_details[2].split(':')[1].strip()
                departure_city = flight_details[3].split(':')[1].strip()
                departure_airport = flight_details[4].split(':')[1].strip()
                arrival_city = flight_details[5].split(':')[1].strip()
                arrival_airport = flight_details[6].split(':')[1].strip()
                seat_capacity = flight_details[7].split(':')[1].strip()
                    
                # Extract and format departure time
                departure_time_match = re.search(r'Departure Time: (\d{2}:\d{2} [AP]M)', line)
                if departure_time_match:
                    departure_time = departure_time_match.group(1)
                else:
                    departure_time = ""
                    
                # Extract and format arrival time
                arrival_time_match = re.search(r'Arrival Time: (\d{2}:\d{2} [AP]M)', line)
                if arrival_time_match:
                    arrival_time = arrival_time_match.group(1)
                else:
                    arrival_time = ""

                if posted_flight_number == flight_number:
                    context = {
                        'flight_number': flight_number,
                        'airline': airline,
                        'aircraft_type': aircraft_type,
                        'departure_city': departure_city,
                        'departure_airport': departure_airport,
                        'arrival_city': arrival_city,
                        'arrival_airport': arrival_airport,
                        'seat_capacity': seat_capacity,
                        'departure_time': departure_time,
                        'arrival_time': arrival_time,
                    }

            return render(request, 'booking.html', context)

    return render(request, 'booking.html')

def process_booking(request):
    if request.method == 'POST':
        # Retrieve form data
        flight_number = request.POST.get('flight_number')
        airline = request.POST.get('airline')
        aircraft_type = request.POST.get('aircraft_type')
        departure_city = request.POST.get('departure_city')
        departure_airport = request.POST.get('departure_airport')
        arrival_city = request.POST.get('arrival_city')
        arrival_airport = request.POST.get('arrival_airport')
        departure_time = request.POST.get('departure_time')
        arrival_time = request.POST.get('arrival_time')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        # Combine data with delimiter
        data_line = f'{flight_number}|{airline}|{aircraft_type}|{departure_city}|{departure_airport}|{arrival_city}|{arrival_airport}|{departure_time}|{arrival_time}|{first_name}|{last_name}|{age}|{gender}|{mobile}|{email}'

        file_path = 'static/booking.txt'

        # Write data to file
        with open(file_path, 'a') as file:
            file.write(data_line + '\n')

        print(data_line)

    return render(request, "booking_confirm.html")
    
def flights(request):
    return render(request, "flights.html")

def my_bookings(request):
    return render(request, "my_bookings.html")

def flight_status(request):
    return render(request, "flight_status.html")