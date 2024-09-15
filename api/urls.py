from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login,name='login' ),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('changepass',views.change_password,name='changepass'),
    path('updatedata',views.update_user_data,name='updatedata')
]