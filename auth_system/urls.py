from django.urls import path,include
from auth_system import views
urlpatterns=[
    path('', views.HomePage, name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('forms1/',views.forms1,name='forms1'),
    path('forms2/',views.forms2,name='forms2')
]