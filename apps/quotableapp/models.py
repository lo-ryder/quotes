from __future__ import unicode_literals

from django.db import models
from ..logregapp .models import User

# Create your models here.

class QuoteManager(models.Manager):

    def ContributeQuote(self, postData):
        print 'Contribute Quote: POST DATA------> ', postData

        errors = []

        if len(postData['quoted_by']) < 3:
            errors.append('Quoted By: Must be more than 3 characters entered!')
        if len(postData['message']) < 3:
            errors.append('Message: Must be more than 10 characters entered!')
        if errors:
            print errors
            return False, errors
        else:
            print 'ADDING QUOTE------>>> ',postData['message'], 'posted by -> user_id=',postData['user_id']

            new_quote = Quote.objects.create(
            quoted_by = postData['quoted_by'],
            message = postData['message'],
            posted_by = User.objects.get(id=postData['user_id']),
            )


            print 'NEW ITEM------>>> ', new_quote
            return True, new_quote

class Quote(models.Model):
    quoted_by = models.CharField(max_length=50)
    message = models.CharField(max_length=400)
    posted_by = models.ForeignKey(User, related_name='quote_added')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuoteManager()
