from django.urls import path

from MathModel import views

# from main.views import main
urlpatterns = [
    path("", views.show_math_model)

]
