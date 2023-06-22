from django.urls import path

from skywing import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('search_flights', views.search_flights, name='search_flights'),
    path('flights', views.flights, name='flights'),
    path('process_booking', views.process_booking, name="process_booking"),
    path('my_booking', views.my_booking, name='my_booking'),
    path('flight_status', views.flight_status, name='flight_status')
]