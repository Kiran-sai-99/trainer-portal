from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.signup, name='signup'),
    path('', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
]