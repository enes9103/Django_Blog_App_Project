from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content','post_image','category','status')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('body',)
        labels={'body':'Comment'}