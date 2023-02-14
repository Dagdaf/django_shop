from django.urls import path
from shop.views import *

urlpatterns = [
    path('', Home, name='home'),
]