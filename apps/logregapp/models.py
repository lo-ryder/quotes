from __future__ import unicode_literals
import re
import bcrypt
from django.db import models


#Our new manager!
#No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class UserManager(models.Manager):
    print "+++++++In User Manager+++++++"

    def register(self, postData):
        errors = []
        emailck = postData['email']
        print emailck
        EMAIL_REGEX = re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', emailck)
        print EMAIL_REGEX

        if len(postData['name'])<2:
            errors.append('Name: No fewer than 3 characters; letters only.')

        if len(postData['alias'])<2:
            errors.append('Alias: No fewer than 3 characters; letters only.')

        if EMAIL_REGEX is None:
            errors.append('Email: Required. Valid format.')

        if len(postData['password'])<7 and postData['password'] == postData['con_password']:
            errors.append('Password: Required; No fewer than 8 characters in length; matches Password Confirmation')

        print errors

        if errors:
            return False, errors

        else:
            key = postData['password'].encode()
            hashed_key = bcrypt.hashpw(
                key,
                bcrypt.gensalt()
            )

            print "\n\n>>>>>>>>><<<<>>>><<<<>>><>**\n\nhash->", hashed_key,'\n\n'

            new_obj = User.objects.create(
                name = postData['name'],
                alias = postData['alias'],
                email = postData['email'],
                password = hashed_key,
                dob = postData['dob'],
            )

            find_user = User.objects.filter(email=postData['email']).values()
            print 'in models register.... find_user=', find_user, '\n\n'
            return True, find_user

    def login(self, postData):
            errors = []

            if User.objects.filter(email=postData['email']):
                print "In login........."
                print "email search......", postData['email']

                print User.objects.all()
                print postData['password']
                print 'in if string????!'

                find_user = User.objects.filter(email=postData['email'])


                print "F I N D  U S E R PW. . . . SAVED AS ->", find_user
                for item in find_user.values():
                    print item
                    user_password = item['password']
                    print 'user password found      ', user_password, '     creating hashkey for input pw'


                    key = postData['password'].encode()
                    hashed_key = bcrypt.hashpw(
                        key,
                        item['password'].encode()
                    )
                    print hashed_key
                    if user_password == hashed_key:
                        print "password MATCH <<<<<<<<<<<"
                        return True, find_user
                    else:
                        print "wrong username or password"
                        errors.append('Login: username or password inccorrect')
                        return False, errors
            else:
                print "wrong username or password"
                errors.append('Login: username or password inccorrect')
                return False, errors



    def validate_activity(self, postData):
        print "in models", postData

        errors = []

        if len(postData['name'])<1:
            errors.append('No fewer than 2 characters; letters only.')

        # Location.objects.get(id=postData['location'])
class User(models.Model):
        name = models.CharField(max_length=45)
        alias = models.CharField(max_length=45)
        email = models.CharField(max_length=45)
        password = models.CharField(max_length=100)
        dob = models.DateField(null=True)
        created_at = models.DateTimeField(auto_now_add = True)
        updated_at = models.DateTimeField(auto_now = True)

        objects = UserManager()
