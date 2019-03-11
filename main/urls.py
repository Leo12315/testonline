from django.urls import path

from main import views

# from main.views import main
urlpatterns = [
    path('', views.main)
]
