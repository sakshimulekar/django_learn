from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LoginView

app_name = 'restaurant'
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('menu/', views.menu, name='menu'),
    path('create/', views.create_dish, name='create_dish'),
    path('edit/<int:dish_id>/', views.edit_dish, name='edit_dish'),
    path('delete/<int:dish_id>/', views.delete_dish, name='delete_dish'),
    path('place_order/<int:dish_id>/', views.place_order, name='place_order'),
    path('', views.home, name='home'),
    path('staff_orders/', views.staff_orders, name='staff_orders'),
    path('my_orders/remove_dish/<int:order_id>/<int:dish_id>/', views.remove_dish, name='remove_dish'),
    path('order/<int:dish_id>',views.my_orders,name='order')
]