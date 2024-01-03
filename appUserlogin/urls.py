from django.urls import path
from . import views
urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('passchange/', views.pass_change, name='passchange'),
]