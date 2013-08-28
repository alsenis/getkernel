from utils import render_response
from django.conf import settings

def dashboard(request):
	return render_response(request, 'dashboard.html') 

from django.contrib import auth

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:

        auth.login(request, user)

        return HttpResponseRedirect("/account/loggedin/")
    else:

        return HttpResponseRedirect("/account/invalid/")

from django.contrib import auth

def logout(request):
    auth.logout(request)

    return HttpResponseRedirect("/account/loggedout/")