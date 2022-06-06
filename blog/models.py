from django.db import models
from django.contrib.auth.models import User
from urllib import request

CATEGORY = (
    (None, 'Choose...'),
    ('Technology','Technology'),
    ('Software','Software'),
    ('Business','Business'),
    ('Fashion','Fashion'),
    ('Lifestyle','Lifestyle'),
    ('Travel','Travel'),
    ('Food','Food'),
)
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    post_image=models.ImageField(upload_to='post_image', blank=True)
    category=models.CharField(max_length=50,choices=CATEGORY, blank=True,verbose_name="category")
    publish_date=models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    blog_views = models.PositiveIntegerField(default=0)
    blog_like = models.PositiveIntegerField(default=0)
    blog_comment = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title


# ----------LİKE-----------
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    

# ---------COMMENT----------
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['date_added']

    # def __str__(self):
    #     return self.comment