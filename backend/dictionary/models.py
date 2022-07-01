from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Word'
        verbose_name_plural = 'Words'
        ordering = ['word']

    def __str__(self):
        return self.word


class Meaning(models.Model):
    word = models.ForeignKey(
        'dictionary.Word',
        on_delete=models.PROTECT,
        related_name='meanings',
        related_query_name='meaning'
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
