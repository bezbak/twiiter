from django.urls import path
from apps.users.views import register,user_login,account, account_settings
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', register, name='register'),
    path('user_login/', user_login, name='user_login'),
    path('logout/', LogoutView.as_view(next_page='user_login'), name='logout'),
    path('account/<str:username>/', account,name='account'),
    path('account_settings/<str:username>/', account_settings,name='account_settings'),
]
