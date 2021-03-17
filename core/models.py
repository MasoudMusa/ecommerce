from django.db import models

TAG_CHOICES = (
    ('N', 'New'),
    ('S', 'Sale')    
)

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(blank=False)
    discount_price = models.FloatField(blank=True, null=True)
    tag = models.CharField(choices=TAG_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })    