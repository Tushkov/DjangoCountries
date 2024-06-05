from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries_list', views.countries_list),
    path('country/<country>', views.country),
    path('work', views.work),
]
