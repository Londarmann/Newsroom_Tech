from django.contrib import admin

from blocks.models import BlockModel


class ArticleInline(admin.TabularInline):
    model = BlockModel.articles.through
    extra = 1


class BlockModelAdmin(admin.ModelAdmin):
    model = BlockModel
    inlines = [ArticleInline]


admin.site.register(BlockModel, BlockModelAdmin)
