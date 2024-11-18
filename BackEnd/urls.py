from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    path('test_token/', views.test_token),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('change_password/',views.change_password),
    path('view_profile/',views.view_profile),
]