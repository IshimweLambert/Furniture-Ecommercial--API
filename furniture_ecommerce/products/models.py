from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('chair', 'Chair'),
        ('table', 'Table'),
        ('sofa', 'Sofa'),
        ('bed', 'Bed'),
        ('cabinet', 'Cabinet'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

