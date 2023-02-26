from django.shortcuts import render, redirect
from apps.posts.models import Posts
from apps.users.models import User
from apps.settings.models import Settings
from django.db.models import Q
# Create your views here.
def update_post(request, id):
    post = Posts.objects.get(id = id)
    settings = Settings.objects.latest('id')

    if request.user == post.user:
        if request.method == 'POST':
            file = request.FILES.get('file')
            text = request.POST.get('text')
            if text:  
                post.text=text
                post.video = file
                post.image = file
                post.save()
                return redirect('index')  
            else:
                try:
                    post.image = file
                    post.video = file
                    post.text=text
                    post.save()
                    return redirect('index')
                except:
                    post.video = file
                    post.image = file
                    post.text=text
                    post.save()
                    return redirect('index')
    else:
        return redirect('index')
    context = {
        'post':post,
        'settings':settings
    }    
    return render(request, 'posts/update_post.html', context)

def post_delete(request, id):
    post = Posts.objects.get(id = id)
    if request.user == post.user:
        if request.method == 'POST':
            post.delete()
            return redirect('index')
    else:
        return redirect('index')
    return render(request, 'posts/post_delete.html')

def search(request):
    posts = Posts.objects.all()
    users = User.objects.all()
    search_key = request.GET.get('key')
    if search_key:
        posts = Posts.objects.all().filter(Q(text__icontains = search_key))
        users = User.objects.all().filter(Q(username__icontains = search_key))
    context = {
        'users':users,
        'posts':posts,
    }
    return render(request, 'posts/search.html', context)