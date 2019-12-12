from django.urls import re_path
from .views import search

app_name = 'google_cse'

urlpatterns = [
    re_path(r'^$', search, name='search'),
]
