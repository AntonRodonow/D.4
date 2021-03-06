from django.urls import path
from .views import PostList, PostDetailView, PostAddView, PostListFilter

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add/', PostAddView.as_view(), name='post_add'),
    path('search/', PostListFilter.as_view()),
]
