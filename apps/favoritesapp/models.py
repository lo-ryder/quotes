from __future__ import unicode_literals

from django.db import models
from ..logregapp .models import User
from ..quotableapp .models import Quote
# Create your models here.

class FavoritesManager(models.Manager):

    def addfavorite(self, postData):
        print 'Add QUOTE to Favorites: quote id------> ', postData

        new_fav = Favorites.objects.create(
        user_favoriting = User.objects.get(id=postData['user_id']),
        fav_quote = Quote.objects.get(id=postData['quote_id']),
        )

        print 'NEW FAV QUOTE------>>> ', new_fav
        return True, new_fav

class Favorites(models.Model):
    user_favoriting = models.ForeignKey(User, related_name='my_fav')
    fav_quote = models.ForeignKey(Quote, related_name='my_quotes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = FavoritesManager()
