from django.shortcuts import render, HttpResponse, redirect, render_to_response


# Create your views here.


def index(request):

    if request.user.is_authenticated():
        print('logined')

    return render_to_response('index.html')
