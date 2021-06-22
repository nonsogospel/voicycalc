# Importing things
from django.urls import path
from . import views

# The links
urlpatterns = [
    path('', views.index, name='index'),
    path("voice_calculator.html", views.voice_calculator, name="voice_calculator"),
    path("run_script", views.run_script, name="run_script"),
    path("help_script", views.help_script, name="help_script"),
]