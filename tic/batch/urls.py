from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from batch.views import UINViewSet

router = DefaultRouter()
router.register(r'uin', UINViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]