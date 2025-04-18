from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from practice.models import Post

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(request, "practice/index.html", {
        "post_list": qs,
    } )