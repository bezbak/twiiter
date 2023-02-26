from django.urls import path
from apps.posts.views import update_post, post_delete, search
urlpatterns = [
    path('update_post/<int:id>/', update_post, name='update_post'),
    path('post_delete/<int:id>/', post_delete, name='post_delete'),
    path('search/', search, name='search'),
]
