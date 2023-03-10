from django.urls import path,include
from auth_system import views
urlpatterns=[
    path('', views.login, name='login'),
    path('signup/',views.signup,name='signup'),
    path('home/', views.HomePage,name='home'),
    path('forms1/',views.forms1,name='forms1'),
    path('forms2/',views.forms2,name='forms2'),
    path('signout/',views.signout,name='signout'),
]