from django.urls import path
from . import views

urlpatterns = [
    path('menu',views.menu_list ,name="menu_list"),
    path('edit_item/<int:item_id>', views.edit_item, name='edit_item'),
    path('del_item/<int:item_id>', views.del_item, name='del_item'),
    path('create_item',views.create_item,name='create_item')
]