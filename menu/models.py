from django.db import models

from content.models import CategoryModel


class MenuModel(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    is_external = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, blank=True, null=True)

    def save(self, *args, **kwargs):
        print(self.category)
        if not self.category:
            if not self.name or not self.link:
                return
        super(MenuModel, self).save(*args, **kwargs)

