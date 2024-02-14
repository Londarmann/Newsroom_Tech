from django.contrib import admin
from django.urls import path, include

from content import views as content_urls
from menu import views as menu_urls
from blocks import views as block_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('content/', content_urls.api.urls),
    path('menu/', menu_urls.api.urls),
    path('block/', block_urls.api.urls)
]
