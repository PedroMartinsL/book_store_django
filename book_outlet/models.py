from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    author = models.CharField(null=True, max_length=50, default='Unknown')
    is_bestselling = models.BooleanField(default=False)

    def get_deferred_fields(self):
        return reverse('book_detail', args=[self.id])

    def __str__(self):
        return self.title
