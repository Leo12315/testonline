from django.urls import path

from MathModel import views

urlpatterns = [
    path("", views.show_math_model)

]
