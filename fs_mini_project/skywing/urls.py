from django.urls import path


from skywing import views

urlpatterns = [
    path('', views.home, name='home')
]
