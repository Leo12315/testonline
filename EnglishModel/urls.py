from django.urls import path

from EnglishModel import views

# from main.views import main
urlpatterns = [
    path("", views.show_english_model)

]
