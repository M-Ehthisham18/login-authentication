from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page,name='login_page'),
    path('register/',views.register_page, name='register_page'),
    path('dashborder/',views.dashborder,name='dashborder'),
    path('logout/',views.logout_page, name= 'logout')
]
