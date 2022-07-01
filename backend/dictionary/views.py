from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from dictionary.models import Word, Meaning
from serializers import WordSerializer, MeaningSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [permissions.AllowAny, ]

    @action(methods=['GET'], detail=True)
    def meanings(self, request, pk=None):
        word = self.get_object()
        meanings = Meaning.objects.filter(word=word)
        serializer = MeaningSerializer(meanings, many=True)
        return Response(serializer.data)


class MeaningViewSet(viewsets.ModelViewSet):
    queryset = Meaning.objects.all()
    serializer_class = MeaningSerializer
    permission_classes = [permissions.AllowAny]
