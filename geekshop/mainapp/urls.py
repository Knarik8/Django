from django.urls import path
from .views import categories

app_name = 'mainapp'

urlpatterns = [
    path('', categories, name = 'index'),
]