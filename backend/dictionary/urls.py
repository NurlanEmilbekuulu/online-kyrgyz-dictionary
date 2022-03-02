from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dictionary import views

router = DefaultRouter()
router.register(r'word-entries', views.WordEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
