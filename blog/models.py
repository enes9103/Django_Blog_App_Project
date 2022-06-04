from django.db import models
from django.contrib.auth.models import User

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

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']