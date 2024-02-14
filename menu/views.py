from django.http import JsonResponse

from .models import MenuModel
from ninja import NinjaAPI


api = NinjaAPI(urls_namespace='menu')


@api.get("/menu/")
def menu_list(request, limit: int = 10, offset: int = 0):
    menus = MenuModel.objects.all()[offset:offset + limit]
    serialized_menus = [{'id': menu.id, 'name': menu.name, 'categories':
        [{'id': menu.category.id, 'name': menu.category.name}]} for menu in menus if menu.category]
    return JsonResponse(status=200, data={'menus': serialized_menus})
