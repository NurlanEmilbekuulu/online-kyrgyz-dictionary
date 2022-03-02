from django.http import HttpResponse
from rest_framework import permissions
from rest_framework import viewsets

from dictionary.models import WordEntry
from dictionary.serializers import WordEntrySerializer


class WordEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WordEntry.objects.all()
    serializer_class = WordEntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
