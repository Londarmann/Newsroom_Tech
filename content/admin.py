from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import CategoryModel, ArticleModel, TagModel


class CategoryModelAdmin(TreeAdmin):
    form = movenodeform_factory(CategoryModel)


admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(ArticleModel)
admin.site.register(TagModel)