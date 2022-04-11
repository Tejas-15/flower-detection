from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='main_home'),
    path('About/', views.About , name='About'),
    path('Help/', views.Help , name='Help'),
    path('Test1/', views.dectection , name='Test1'),
    path('info_daisy/', views.info_daisy , name='info_daisy'),
    path('info_rose/', views.info_rose , name='info_rose'),
    path('info_dandelion/', views.info_dandelion , name='info_dandelion'),
    path('info_sunflower/', views.info_sunflower , name='info_sunflower'),
    path('info_tulip/', views.info_tulip , name='info_tulip'),
    path('info_lotus/', views.info_lotus , name='info_lotus'),
    
]
