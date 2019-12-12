from django.urls import patterns, url
from .views import search

app_name = 'google_cse'

urlpatterns = patterns(
    '', url(r'^$', search, name='search'),
)
