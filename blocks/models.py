from django.db import models

from content.models import ArticleModel


class BlockModel(models.Model):
    ARTICLE_CHOICES = [
        ('ST', 'Standard'),
        ('HO', 'Horizontal'),
        ('VE', 'Vertical'),
    ]

    title = models.CharField(max_length=250)
    show_title = models.BooleanField(default=False)
    choice_field = models.CharField(max_length=20, choices=ARTICLE_CHOICES)
    position = models.TextField()
    row = models.IntegerField()
    articles = models.ManyToManyField(ArticleModel)

