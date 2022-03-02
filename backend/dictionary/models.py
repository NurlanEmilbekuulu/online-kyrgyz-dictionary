from django.db import models


class WordEntry(models.Model):
    word = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Word entry'
        verbose_name_plural = 'Word entries'
        ordering = ['word']

    def __str__(self):
        return self.word


class Meaning(models.Model):
    word_entry = models.ForeignKey(
        'dictionary.WordEntry',
        on_delete=models.PROTECT,
        related_name='meanings'
    )
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Meaning'
        verbose_name_plural = 'Meanings'
        ordering = ['id']


class Example(models.Model):
    pass


class Proverb(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Proverb'
        verbose_name_plural = 'Proverbs'
        ordering = ['id']
