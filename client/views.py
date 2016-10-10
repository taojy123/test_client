from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, render_to_response


# Create your views here.


def index(request):

    if request.user.is_authenticated():
        redirect(settings.LOGIN_REDIRECT_URL)

    return render_to_response('index.html')


@login_required
def profile(request):
    provider = request.user.current_provider(request)
    return render_to_response('profile.html', locals())
