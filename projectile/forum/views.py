from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .serializers import PostSerializer
from .models import Post, Category
from django.views import generic

# Started with this but then moved onto classes instead.
# Create your views here.
# def PostListView(request):
#     country = request.user.country
#     post_list = Post.objects.filter(
#         parent__isnull=True,
#         parent__country=country
#     ).order_by("-created_at")
#     template = loader.get_template("forum/PostListView.html")
#     context = {
#         "post_list" : post_list,
#     }
#     return HttpResponse(template.render(context, request))


class PostListView(generic.ListView):
    template_name = "forum/PostListView.html"

    def get_queryset(self):
        country = self.request.user.country
        post_list = Post.objects.filter(
            parent__isnull=True,
            parent__country=country
        ).order_by("-created_at")
        return post_list
        # return Post.objects.order_by("-created_at")

class PostGroupedByCategoryListView(generic.ListView):
    template_name = "forum/PostGroupedByCategoryListView.html"
    ##retrieve a list of unique category values
    ## I would want to create a method for the below query set getting, because we are duplicating the above code now. Maybe I will know how after Django course.
    def get_queryset(self):
        categories = Category.objects.values_list('title', flat=True).distinct()
        posts = Post.objects.filter(
        # parent__isnull=True,
        ).order_by("-created_at")
        return posts

class PostDetailView(generic.DetailView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        post = get_object_or_404(Post, id=id)
        post.increment_views()
        responses = post.get_responses().order_by(
            '-created_at'
        )
        posts = post | responses
        serializer = PostSerializer(posts, many=True)
        serializer.is_valid(raise_exception=True)
        return HttpResponse(serializer.data)


def PostCreateView(request):
    def post(self, request, *args, **kwargs):
        parent_id = request.kwargs.get('parent_id', None)
        categories = Category.objects.values_list("title", flat=True).distinct()
        new_post = Post.objects.create(parent=parent, category=category,)
        country = request.user.country
        serializer = PostSerializer(instance=new_post)
        serializer.is_valid(raise_exception=True)
        post.save()
        return HttpResponse(serializer.data)


# I don't think the below method is necessary since the above is already checking in to the parent_id, if it exists.
# def ResponseCreateView(request, parent):
#     def post(self, request, *args, **kwargs):
#         parent_id = request.kwargs.get('parent_id', None)
#         category = ...
#         new_post = Post.objects.create(parent=parent, category=category,)
#         serializer = PostSerializer(instance=new_post)
#         serializer.is_valid(raise_exception=True)
#         return HttpResponse(serializer.data)