from django.shortcuts import render, redirect
from .models import Favorites, FavoritesManager

def addquote(request, id):
    print 'adding quote to favorite quotes, quote id-->',id
    NeededIDs = {
    'quote_id': id,
    'user_id': request.session['id'],
    }
    Favorites.objects.addfavorite(NeededIDs)

    return redirect('quotableapp:quotes')

def removequote(request, id):
    print 'REMOVINGGGGGG!! quote FROM favorites'

    Favorites.objects.filter(id=id).delete()
    return redirect('quotableapp:quotes')
