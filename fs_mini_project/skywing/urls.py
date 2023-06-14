from django.urls import path
#from skywing.views import view_file


from skywing import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('booking', views.booking, name='booking')
    #path('booking', views.view_file, name='view_file')
]
