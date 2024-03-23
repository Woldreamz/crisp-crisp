from django.urls import path, include
from .views import *

app_name = 'total_urls'

urlpatterns = [
    path('add/', CountDetails.as_view(), name='total-increase'),
    path('view/', CountDetails.as_view(), name='total-view'),
]
