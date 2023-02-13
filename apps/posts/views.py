from django.shortcuts import render, redirect
from apps.posts.models import Posts
# Create your views here.
def update_post(request, id):
    post = Posts.objects.get(id = id)
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
        'post':post
    }    
    return render(request, 'update_post.html', context)

def post_delete(request, id):
    post = Posts.objects.get(id = id)
    if request.user == post.user:
        if request.method == 'POST':
            post.delete()
    else:
        return redirect('index')
    return render(request, 'post_delete.html')