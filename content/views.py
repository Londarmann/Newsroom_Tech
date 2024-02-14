from django.http import JsonResponse
from ninja import NinjaAPI

from .models import ArticleModel, CategoryModel

api = NinjaAPI(urls_namespace='content')


@api.get("/category/")
def category_list(request, limit: int = 10, offset: int = 0):
    categories = CategoryModel.objects.all()[offset:offset + limit]
    serialized_category = [{'id': category.id,
                        'parent': category.parent} for category in categories]
    return JsonResponse(status=200, data={'categories': serialized_category})


@api.get("/articles/")
def article_list(request, limit: int = 10, offset: int = 0):
    articles = ArticleModel.objects.all()[offset:offset + limit]
    serialized_articles = [{'id': article.id, 'title': article.title, 'description': article.description,
                            'upload_time': article.upload_time,
                            'author': article.author.username if article.author else None,
                            'category': article.category.name if article.category else None,
                            'tags': [tag.name for tag in article.tags.all()], 'image_url': article.image.url,
                            'published': article.published} for article in articles]
    return JsonResponse(status=200, data={'articles': serialized_articles})


@api.get("/articles/tag/{tag_name}/")
def articles_by_tag(request, tag_name: str, limit: int = 10, offset: int = 0):
    articles = ArticleModel.objects.filter(tags__name=tag_name)[offset:offset + limit]
    serialized_articles = [{'id': article.id, 'title': article.title, 'description': article.description,
                            'upload_time': article.upload_time,
                            'author': article.author.username if article.author else None,
                            'category': article.category.name if article.category else None,
                            'tags': [tag.name for tag in article.tags.all()], 'image_url': article.image.url,
                            'published': article.published} for article in articles]
    return JsonResponse(status=200, data={'articles': serialized_articles})
