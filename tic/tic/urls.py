from django.contrib import admin
from django.urls import path , include
from .views import *
from  . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_view, name='welcome_view'),
    path('rfid-detector', views.rfid_detector, name='rfid_detector'),

     path('post-button/', views.my_button_view, name='post_button'),

      path('blockchain/', include('blockchain.urls')),
]


