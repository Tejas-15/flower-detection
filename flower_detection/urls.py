from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='main_home'),
    # path('upload/', views.upload , name='upload'),
    path('About/', views.About , name='About'),
    path('daisy/', views.daisy , name='daisy'),
    path('yellow_rose/', views.yellow_rose , name='yellow_rose'),
    path('rose/', views.rose , name='rose'),
    path('hometest/', views.hometest , name='hometest'),
    path('Test1/', views.flower_info , name='Test1'),

    
]
