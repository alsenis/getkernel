from utils import render_response
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render_response(request, 'dashboard.html')

@login_required
def blog(request):
    return render_response(request, 'blog.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/account/loggedin/")
    else:
        return HttpResponseRedirect("/account/invalid/")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/account/loggedout/")