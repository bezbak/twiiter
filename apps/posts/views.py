from django.shortcuts import render, redirect
from apps.posts.models import Posts
# Create your views here.
def update_post(request, id):
    if request.method == 'POST':
        post = Posts.objects.get(id = id)
        if request.user == post.user:
            file = request.FILES.get('file')
            text = request.POST.get('image')
            if file:    
                try:
                    post.image = file
                    return redirect('index')
                except:
                    post.video = file
                    return redirect('index')
            else:
                post.text=text
                return redirect('index')
        else:
            return redirect('update_post', post.id)
    context = {
        'post':post
    }    
    return render(request, 'update_post.html', context)