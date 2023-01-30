from django.shortcuts import render
from apps.settings.models import Settings
from apps.posts.models import Posts
# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    posts = Posts.objects.all().order_by('-id')
    context = {
        'settings':settings,
        'posts':posts,
    }
    return render(request, 'feed.html', context)