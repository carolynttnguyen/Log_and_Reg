from django.db import models
import re
import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}

        email_check= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        # First Name - required; at least 2 characters; letters only
        if len(postData['first_name']) < 2:
            errors['first_name']='First name is required to be at least 2 characters, and letters only'
        # Last Name - required; at least 2 characters; letters only
        if len(postData['last_name']) < 2:
            errors['last_name']='Last name is required to be at least 2 characters, and letters only'
        
        # Email - required; valid format
        if not email_check.match(postData['email']):
            errors['email']= 'Your email format is invalid.'

        # # check to see if user email is not already in use
        # email_check = self.filter(email=postData['email'])
        # if email_check:
        #     errors['email']='Email is already in use'

        # Password - required; at least 8 characters; matches password confirmation
        if len(postData['password']) < 8:
            errors['password'] = 'A password is required'

        if postData['password'] != postData['confirm_password']:
            errors['password']= 'Your password does not match with the confirmed password.'

        return errors

    def register(self, postData):
        pass

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()