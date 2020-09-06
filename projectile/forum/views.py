from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Post

# Create your views here.
def PostListView(request):
    post_list = Post.objects.order_by("-created_at")
    template = loader.get_template("forum/PostListView.html")
    context = {
        "post_list" : post_list,
    }
    return HttpResponse(template.render(context, request))
# def PostGroupedByCategoryListView(request):

# def PostDetailView(request):

# def PostCreateView(request):

# def ResponseCreateView(request, parent):