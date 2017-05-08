from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User, UserManager
# Create your views here.
def index(request):
    return redirect('logregapp:main')

def main(request):
    return render(request, 'logregapp/index.html')

def register(request):
    print "Success TYPE.....>", request.POST
    print request.method

    if request.method == "POST":
        print "in reg successful post"

        valid, response = User.objects.register(request.POST)

        if valid:
            print "valid REGISTRATION >< ><", response

            context = {
            'users': response, #new user from new_obj
            'type': 'registered',
            }
            print '\n\n in users context obj', context['users']

            print '+++++++valid login +++++++++', response
            for item in response.values():
                print 'Valid ID', item['id']
                request.session['id']= item['id']
                print 'session ID.......', request.session['id']
            context = {
            'users': response, #user found from email if password matched
            'type': 'logged in',
            }
            return redirect('quotableapp:quotes')
        else:
            print "REGISTER>>>>> else error.....",response

            for error in response:
                print '......',error
            messages.error(request, response)
            return redirect(reverse('logregapp:main'))
    if request.method == "GET":
        return reverse('logregapp:main')

def login(request):
    print "Success TYPE.....>", request.POST
    print request.method

    if request.method == "POST":
        print "in login successful post"

        valid, response = User.objects.login(request.POST)

        if valid:
            print '+++++++valid login +++++++++', response
            for item in response.values():
                print 'Valid ID', item['id']
                request.session['id']= item['id']
                print 'session ID.......', request.session['id']
            context = {
            'users': response, #user found from email if password matched
            'type': 'logged in',
            }
            return redirect('quotableapp:quotes')
        else:
            print "LOGIN>>>>> else error.....",response

            for error in response:
                print '......',error
            messages.error(request, response)
            return redirect(reverse('logregapp:main'))

    if request.method == "GET":
        return reverse('logregapp:main')
