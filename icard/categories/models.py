from django.db import models


CategoryType = (
    ("PRO", "pro"),
    ("ING", "ing")
)


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=250, null=True, blank=True)
    categoryType = models.CharField(
        max_length=255, choices=CategoryType, default="pro")

    def __str__(self):
        return self.title
