from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=30, blank=True)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=5.00
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title