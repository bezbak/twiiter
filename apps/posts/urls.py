from django.urls import path
from apps.posts.views import update_post
urlpatterns = [
    path('update_post/<int:id>/', update_post, name='update_post'),
]
