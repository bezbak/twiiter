from django.urls import path
from apps.users.views import register,user_login
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', register, name='register'),
    path('user_login/', user_login, name='user_login'),
    path('logout/', LogoutView.as_view(next_page='user_login'), name='logout'),
]
