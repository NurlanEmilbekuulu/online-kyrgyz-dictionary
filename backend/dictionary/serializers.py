from rest_framework import serializers

from dictionary.models import WordEntry


class WordEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WordEntry
        fields = ['id', 'word', 'created', 'last_modified']
