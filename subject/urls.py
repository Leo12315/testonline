from django.urls import path

from subject import views

# from main.views import main
urlpatterns = [
    path('', views.show_subject)

]
