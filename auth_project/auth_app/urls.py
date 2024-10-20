from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_page, name='register_page'),
    path('',views.login_page,name='login_page'),
    path('dashborder/',views.dashborder,name='dashborder'),
    path('logout/',views.logout_page, name= 'logout')
]
