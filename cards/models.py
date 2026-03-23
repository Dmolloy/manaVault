from django.db import models

# Create your models here.
class Card(models.Model):
    RARITY_CHOICES = [
        ('common', 'Common'),
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('mythic', 'Mythic Rare'),
    ]

    CONDITION_CHOICES = [
        ('nm', 'Near Mint'),
        ('lp', 'Lightly Played'),
        ('mp', 'Moderately Played'),
        ('hp', 'Heavily Played'),
    ]

    name = models.CharField(max_length=255)
    set_name = models.CharField(max_length=255)
    card_type = models.CharField(max_length=255)
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    mana_cost = models.CharField(max_length=50, blank=True)
    color_identity = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='cards/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name