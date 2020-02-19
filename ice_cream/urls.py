from django.urls import path

from . import views

app_name = 'ice_cream'

urlpatterns = [
    path('add/', views.CreateView.as_view(), name='add'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('', views.IndexView.as_view(), name='index'),
    
]