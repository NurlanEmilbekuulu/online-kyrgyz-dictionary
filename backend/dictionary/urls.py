from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dictionary import views

router = DefaultRouter()
router.register(r'words', views.WordViewSet)
router.register(r'meanings', views.MeaningViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
