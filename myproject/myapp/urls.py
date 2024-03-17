from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),

    #
    path('userhome/', views.user_login, name='userhome'),

    path('userlanding/', views.user_landing, name='userlanding'),
    path('userplan/', views.user_plan, name='userplan'),
    path('usermajor/', views.user_major, name='usermajor'),
    #

    # path('newuserinfo/', views.input_view, name='newuserinfo'),

    path('input/', views.input_view, name='input_view'),

]