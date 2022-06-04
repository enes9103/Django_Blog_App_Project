from django.urls import path
from .views import user_logout, register, user_login,profile

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',user_login,name='user_login'),
    path('logout/',user_logout,name='logout'),
    path('profile/<int:id>/',profile,name='profile'),

]