from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='PostListView'),
    path('<int:id>/', views.PostDetailView.as_view(), name='PostDetailView'),
    path('categorylist/', views.PostGroupedByCategoryListView.as_view(), name='PostGroupedByCategoryListView'),
    path('createpost', views.PostCreateView, name='PostCreateView'),
    ##unsure if this is necessary, the above already looks if there is a parent..
    # path('createresponse', views.PostCreateView, name="PostCreateView"),
]
