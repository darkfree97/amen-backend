from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True, primary_key=True)

    def __str__(self) -> str:
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    preview = models.URLField(max_length=256, blank=True)
    link = models.URLField(max_length=256, blank=True)
    date = models.DateField(null=True)

    def __str__(self) -> str:
        return self.title
