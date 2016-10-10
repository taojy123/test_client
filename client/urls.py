
from django.conf.urls import url, include

from client import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^profile', views.profile),
    url(r'^o/', include('django_sanction.urls')),
]
