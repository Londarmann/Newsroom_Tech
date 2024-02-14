from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from treebeard.mp_tree import MP_Node

from users.models import User


class CategoryModel(MP_Node):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='uploads/')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='categories')

    node_order_by = ['name']

    def __str__(self):
        return self.name


class TagModel(models.Model):
    name = models.CharField(max_length=320)

    def __str__(self):
        return self.name


class ArticleModel(models.Model):

    title = models.CharField(max_length=500)
    description = HTMLField(blank=True, null=True)
    upload_time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,  blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(CategoryModel,  blank=True, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(TagModel)
    image = models.ImageField(upload_to='uploads/')
    published = models.BooleanField()
    # block = models.ForeignKey(BlockModel, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
