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
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name