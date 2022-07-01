from rest_framework import serializers

from dictionary.models import Word, Meaning


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'created', 'last_modified']


class MeaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meaning
        fields = ['id', 'word', 'text', 'created', 'last_modified']
