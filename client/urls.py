
from django.conf.urls import url, include

from client.views import index

urlpatterns = [
    url(r'^/', index),
    url(r'^o/', include('django_sanction.urls')),
]
