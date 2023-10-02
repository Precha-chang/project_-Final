from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('purchasing', views.purchasing, name='purchasing'),
    path('providing/', views.providing, name='providing'),
    path('aftersale/', views.aftersale, name='aftersale'),
    path('about', views.about, name="about"),


]