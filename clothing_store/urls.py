from django.urls import path
from .views import index, product_list, login_view, register_view, dashboard_view, profile_view, logout_view

urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list, name='product_list'),
    path('login/', login_view, name='login'),
    path('signup/', register_view, name='signup'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
]
