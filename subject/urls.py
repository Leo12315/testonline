from django.urls import include, path

from subject import views

# from main.views import main
urlpatterns = [
    path("", views.show_subject),
    path("math-index", include('MathModel.urls')),
    path("chinese-index", include('ChineseModel.urls')),
    path("english-index", include('EnglishModel.urls'))

]
