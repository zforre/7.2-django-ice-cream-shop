from django.urls import path

from . import views

app_name = 'icecream'

urlpatterns = [
    path('new/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('', views.IndexView.as_view(), name='index'),
    
]