from django.urls import path

from ChineseModel.views import show_chinese_model
from EnglishModel.views import show_english_model
from MathModel.views import show_math_model

# from main.views import main
urlpatterns = [
    # path("", show_subject),
    path("math-index/", show_math_model),
    path("chinese-index/", show_chinese_model),
    path("english-index/", show_english_model),

]
