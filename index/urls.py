from django.urls import path

from index import views

# from main.views import main
urlpatterns = [
    path('', views.main)
]
