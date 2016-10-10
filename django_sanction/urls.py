# -*- coding: utf-8 -*- 
""" The URLs defined by django-sanction

django_sanction should be initialized in your project's urls.py as such:

.. code-block:: python

   urlpatterns = patterns('',
       url(r'^o/', include('django_sanction.urls')),
   )

The prefix ``o`` can be replaced by any path you would like to use for the
sanction auth flow. Two views are registered under this path:

* ``[prefix]/logout/``, and
* ``[prefix]/login/(\w+)``

:note: The parameter for the login flow *must* match a key used in
       ``SANCTION_PROVIDERS`` in your project settings file.
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import logout
import views

urlpatterns = [
    url(r'^logout/$', logout, {
        'next_page': settings.LOGIN_URL}),
    url(r'^login/(\w+)', views.login),
]
