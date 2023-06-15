from django.urls import path

from skywing import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('flights', views.flights, name='flights'),
    path('my_bookings', views.my_bookings, name='my_bookings'),
    path('flight_status', views.flight_status, name='flight_status')

]
