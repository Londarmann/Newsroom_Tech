
from django.http import JsonResponse
from ninja import NinjaAPI

from .models import BlockModel

api = NinjaAPI(urls_namespace='block')


@api.get("/block/")
def block_list(request, limit: int = 10, offset: int = 0):
    blocks = BlockModel.objects.all()[offset:offset + limit]
    serialized_category = [{'id': block.id, "show_title": block.show_title,
                        'choice_field': block.chocie_field, "position": block.position, "row": block.row,
                            'articles': [block.title for tag in blocks.articles.all()]} for block in blocks]
    return JsonResponse(status=200, data={'categories': serialized_category})
