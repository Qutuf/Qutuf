"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from webservice.views import index

urlpatterns = [
    # HomePage
    url(r'^$', index, name='index')
]
