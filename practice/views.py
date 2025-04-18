from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from practice.models import Post

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(request, "practice/index.html", {
        "post_list": qs,
    } )    

def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    return render(request, "practice/post_detail.html", {
        "post": post,
    } )