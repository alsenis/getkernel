from django.contrib.auth.decorators import login_required


from django.template import loader, Context
from django.http import HttpResponse
from getkernel.models import BlogPost

@login_required
def blog(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("blog/blog.html")
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))