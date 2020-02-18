from django.urls import path

from . import views

app_name= 'home_page'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    
]