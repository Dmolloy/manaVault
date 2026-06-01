from django.conf import settings
from django.db import models


class WishlistItem(models.Model):
    CONDITION_CHOICES = [
        ('near_mint', 'Near Mint'),
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('played', 'Played'),
        ('any', 'Any Condition'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='wishlist_items'
    )
    card_name = models.CharField(max_length=100)
    set_name = models.CharField(max_length=100, blank=True)
    desired_condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default='any'
    )
    max_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.card_name} - {self.user.username}"