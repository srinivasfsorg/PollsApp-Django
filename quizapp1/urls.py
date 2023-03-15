from django.urls import path

from . import views
app_name = 'quizapp1'
urlpatterns = [
    path('', views.index ),
]