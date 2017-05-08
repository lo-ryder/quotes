from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Quote, QuoteManager
from ..favoritesapp .models import Favorites
from ..logregapp .models import User

def quotes(request):
    context = {
    'currentUser': User.objects.get(id=request.session['id']),
    'quotableQuotes': Quote.objects.all().exclude(my_quotes__user_favoriting=request.session['id']),
    'favoriteQuotes': Favorites.objects.filter(user_favoriting=request.session['id']),

    }


    return render(request, 'quotableapp/quotes.html', context)

def contribute(request):
    if request.method == 'POST':
        valid, response = Quote.objects.ContributeQuote(request.POST)
        if valid:
            print 'NOW adding QUOTE to QUOTABLE QUOTES, response->', response

            return redirect('quotableapp:quotes')
        else:
            print "else error.....",response

            for error in response:
                print '......',error
            messages.error(request, response)
            return redirect('quotableapp:quotes')

    return redirect(reverse('quotableapp:quotes'))


def posts(request, id):
    context = {
    'postsUser': User.objects.get(id=id),
    'quotableQuotes': Quote.objects.filter(posted_by=id),
    }

    return render(request, 'quotableapp/users.html', context)
