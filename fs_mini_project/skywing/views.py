from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")



def booking(request):
    return render(request, "booking.html")
    file_path = 'fs_mini_project\skywing\booking.txt'  # Replace with the actual file path in your project's base directory

    with open(file_path, 'r') as file:
        file_contents = file.read()

    context = {'file_contents': file_contents}
    return render(request, 'booking.html', context)

from django.shortcuts import render

#def view_file(request):
    