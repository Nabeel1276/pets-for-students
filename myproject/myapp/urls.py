from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('pets/', views.pets, name='pets')
]
