from django.urls import path
from . import views



urlpatterns = [
    path('create/',views.create_post,name="create_post"),
    path('view/',views.view_posts,name='view_posts'),
    path('delete/<int:post_id>/',views.delete_post,name='delete_post')
]