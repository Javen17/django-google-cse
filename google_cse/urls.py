from django.urls import re_path
from .views import search

app_name = 'google_cse'

urlpatterns = [
    url(r'^$', search, name='search'),
]
