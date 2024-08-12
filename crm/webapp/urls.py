from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name="home"),

    path('register', views.register ,name="register"),

    path('mylogin', views.mylogin, name='mylogin'),

    path('userlogout', views.userlogout, name="userlogout"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('createrecord', views.createrecord, name='createrecord'),

    path('updaterecord/<int:pk>',views.updaterecord,name="updaterecord"),

    path('readrecord/<int:pk>',views.readrecord,name="readrecord"),

    path('deleterecord/<int:pk>',views.deleterecord, name='deleterecord'),

]
