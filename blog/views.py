from django.shortcuts import redirect,render
from .forms import PostForm, CommentForm
from .models import Post, Comment, Like
from django.contrib.auth.decorators import login_required

# ---------HOME----------
def home(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request, 'home.html',context)

# ---------ADD----------
@login_required
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
@login_required
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
@login_required
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
    comment_form = CommentForm()
    comments = Comment.objects.filter(post=post.id)
    post.blog_views += 1
    post.save()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            post.blog_comment += 1
            comment.user = request.user
            post.save()
            comment.save()
            return redirect('detail', id=id)
    context = {
        'post':post, 'comment_form':comment_form, 'comments':comments}
    return render(request, 'blog/blog_detail.html', context)

# ---------LİKE----------
def blog_like(request, id):
    post = Post.objects.get(id=id)
    # like = Like.objects.get_or_create(user=request.user, instance=post.id)
    # like.save()
    post.blog_like += 1
    post.save()
    return redirect("detail", id=id)