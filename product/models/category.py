from django.db import models

class Category(models.Model):
    title= models.TextField(max_length=100)
    slug= models.SlugField(unique=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title