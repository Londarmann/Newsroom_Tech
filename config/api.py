# # api.py
# from ninja import Router, Schema
# from typing import List
# from content.models import ArticleModel
#
# router = Router()
#
#
#
#
# @router.get("/articles/", response={200: List[ArticleSchema]})
# def get_articles(request, skip: int = 0, limit: int = 10):
#     articles = ArticleModel.objects.all()[skip: skip + limit]
#     return articles
#
#
# @router.get("/articles/tag/{tag_name}/", response={200: List[ArticleSchema]})
# def get_articles_by_tag(request, tag_name: str, skip: int = 0, limit: int = 10):
#     articles = ArticleModel.objects.filter(tags__name=tag_name)[skip: skip + limit]
#     return articles
