from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='main_home'),
    # path('upload/', views.upload , name='upload'),
    path('About/', views.About , name='About'),
    path('Test1/', views.dectection , name='Test1'),

    
]
