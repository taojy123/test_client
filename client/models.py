from datetime import datetime, timedelta
from time import mktime

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, UserManager
from lazy import lazy
from sanction import Client as SanctionClient


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    username = models.CharField(_('username'), max_length=30, unique=True)
    first_name = models.CharField(_('first name'), max_length=100, blank=True)
    last_name = models.CharField(_('last name'), max_length=100, blank=True)

    objects = UserManager()

    @lazy
    def providers(self):
        return dict((p.name, p) for p in Provider.objects.filter(user=self))

    def current_provider(self, request):
        return self.providers[request.session['__sp']]

    @staticmethod
    def fetch_user(provider, client):
        print('----------------- fetch_user ---------------------')
        return getattr(User, 'fetch_{}'.format(provider))(client)

    @staticmethod
    def fetch_weibo(client):
        print('weibo access_token:', client.access_token)
        resp = client.request('/get_token_info', method='POST')
        print(resp)
        normalized = {
            'id': resp['uid'],
            'provider': 'weibo',
            'access_token': client.access_token,
        }
        return User._get(normalized)

    @staticmethod
    def fetch_heyshop(client):
        print('heyshop access_token:', client.access_token)
        normalized = {
            'id': client.access_token,
            'provider': 'heishop',
            'access_token': client.access_token,
        }
        return User._get(normalized)

    @staticmethod
    def get_user(user_id):
        return User.objects.get(id=user_id)

    @staticmethod
    def _get(data):
        try:
            provider = Provider.objects.get(name=data['provider'],
                                            pid=data['id'])
        except Provider.DoesNotExist:
            user = User.objects.create(username='{}_{}'.format(data['provider'], data['id']))
            user.save()

            provider = Provider()
            provider.name = data['provider']
            provider.user = user
            provider.pid = data['id']
            provider.access_token = data['access_token']
            provider.save()

        return provider.user


class Provider(models.Model):
    name = models.CharField(_('provider'), max_length=50)
    user = models.ForeignKey(User)
    email = models.EmailField(_('email address'), blank=True)
    pid = models.CharField(_('provider id'), max_length=50)
    access_token = models.CharField(_('access token'), max_length=100,
                                    blank=True)
    refresh_token = models.CharField(_('refresh token'), max_length=100,
                                     blank=True, null=True)
    token_expires = models.FloatField(default=-1)

    @lazy
    def resource(self):
        provider = settings.SANCTION_PROVIDERS[self.name]
        c = SanctionClient(auth_endpoint=provider['auth_endpoint'],
                           token_endpoint=provider['token_endpoint'],
                           resource_endpoint=provider['resource_endpoint'],
                           client_id=provider['client_id'],
                           client_secret=provider['client_secret'])

        c.refresh_token = self.refresh_token
        c.access_token = self.access_token
        c.token_expires = self.token_expires
        return c

    def refresh(self):
        assert self.refresh_token is not None
        self.resource.refresh()
        self.access_token = self.resource.access_token
        self.token_expires = self.resource.token_expires
        self.save()
