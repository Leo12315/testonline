from django.urls import path

from ChineseModel import views

# from main.views import main
urlpatterns = [
    path("", views.show_chinese_model)

]
