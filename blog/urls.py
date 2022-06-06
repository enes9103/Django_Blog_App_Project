from django.urls import path
from blog.views import post_add,blog_update,blog_delete,blog_detail,blog_like


urlpatterns = [
    path('new_post/',post_add,name='new_post'),
    path('update/<int:id>', blog_update, name='update'),
    path('delete/<int:id>', blog_delete, name='delete'),
    path('detail/<int:id>', blog_detail, name='detail'),
    path('like/<int:id>', blog_like, name='blog_like'),
]