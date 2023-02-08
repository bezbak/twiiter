from django.shortcuts import render, redirect
from apps.settings.models import Settings
from apps.posts.models import Posts, Comment, Like
# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    posts = Posts.objects.all().order_by('-id')
    if request.method == 'POST':
        if 'create_post' in request.POST:
            post_text = request.POST.get('post_text')
            post_file = request.FILES.get('post_file')
            if post_file:
                try:
                    post = Posts.objects.create(image = post_file, user = request.user)
                    post.save()
                except:
                    post = Posts.objects.create(video = post_file, user = request.user)
                    post.save()
            else:
                post = Posts.objects.create(text = post_text, user = request.user)
                post.save()
        if 'like' in request.POST:
            post = request.POST.get('post')
            try:
                like = Like.objects.get(user = request.user, post_id = post)
                like.delete()
                return redirect('index')
            except:
                like = Like.objects.create(user = request.user, post_id = post)
                return redirect('index')
        if 'comment' in request.POST:
            text = request.POST.get('text')
            post = request.POST.get('post')
            try:
                comment = Comment.objects.create(post_id = post, user = request.user, text = text)
                comment.save()
                return redirect('index')
            except:
                return redirect('index')
    context = {
        'settings':settings,
        'posts':posts,
    }
    return render(request, 'feed.html', context)