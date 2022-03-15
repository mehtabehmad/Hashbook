from django.urls import path 

from . import views

app_name = "HashbooApp"

urlpatterns = [
    path('', views.index, name = "index"),
    path('posts/', views.posts, name="posts"),
    path('post/<int:post_id>/', views.post, name="post"),
    path('newpost/',views.newpost, name="newpost"),
    path('comment/<int:post_id>/', views.comment, name="comment"),

    #For posts
    path('delete/<int:post_id>/', views.delete, name="delete"),
    path('edit/<int:post_id>/', views.edit, name="edit"),
    
    #For comments
    path('cdelete/<int:comment_id>/', views.cdelete, name="cdelete"),
    path('cedit/<int:comment_id>/', views.cedit, name="cedit"),

]