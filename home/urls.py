from django.urls import path

from home import views

# from main.views import main
urlpatterns = [
    path('', views.show_home)
]
