from django.shortcuts import redirect,render
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

# ---------HOME----------
def home(request):                              #?????????????????????????
    posts=Post.objects.all()
    context={'posts':posts}

    return render(request, 'home.html',context)

# ---------ADD----------
def post_add(request):
    form = PostForm(request.POST)
    
    if request.method=="POST" :
        form = PostForm(request.POST)
        if form.is_valid:
            post_form=form.save()
            if 'post_image' in request.FILES :
                post_form.post_image = request.FILES.get('post_image')
                post_form.save()
            return redirect("home")
    context={
        "form":form
    }
    return render(request, "blog/blog_add.html",context)

# ---------UPDATE----------
def blog_update(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(instance=post)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    
    context = {
        "form" : form
    }
    return render(request, "blog/blog_update.html", context)

# ---------DELETE----------
def blog_delete(request, id):
    post = Post.objects.get(id=id)
    
    if request.method == "POST":
        post.delete()
        return redirect("home")
    
    context = {
        'post':post
    }
    
    return render(request, "blog/blog_delete.html", context)

# ---------DETAİL----------
def blog_detail(request, id):        
    post = Post.objects.get(id=id)
    context = {
        'post':post
    }
    return render(request, 'blog/blog_detail.html', context)
