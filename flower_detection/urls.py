from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='main_home'),
    path('upload/', views.upload , name='upload'),
    path('test/', views.test , name='test_home'),
    path('daisy/', views.daisy , name='daisy'),
    path('yellow_rose/', views.yellow_rose , name='yellow_rose'),
    path('pink_rose/', views.pink_rose , name='pink_rose'),
    path('Test1/', views.Test1 , name='Test1'),
    
]
