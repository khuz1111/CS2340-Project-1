from django.urls import path
from .views import index, register, login_view, logout_view

urlpatterns = [
    path("register/", register, name="register"),
    path('', index, name='home'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name="logout"),
]