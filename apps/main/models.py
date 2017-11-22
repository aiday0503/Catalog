from __future__ import unicode_literals
import re
from django.db import models
import bcrypt
from datetime import datetime, timedelta

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validation(self, postdata):
        errors = []
       
        if len(postdata['fName'])<1 and len(postdata['username'])<1 and len (postdata['email'])<1 and len(postdata['date'])<1:
            errors.append("Please fill outs the form to register")
        if len(postdata['email']) < 0:
            errors.append("Sorry you need an email to register.")
        if not re.match(EMAIL_REGEX, postdata['email']):
            errors.append("Hmm this doesn't look like a valid email")
        else:
            if len(self.filter(email=postdata['email']))>0:
                errors.append("Email already in use.")
        
        if postdata['date'] !='':
            date = datetime.strptime(postdata['date'], "%Y-%m-%d")
            now = datetime.now()
            if date > now:
                errors.append("Invalid Birthday Field")
        else:
            errors.append("Please provide the Birthdate")
                        
        if len(postdata['password1']) < 8:
            errors.append("Password cannot be less than 8 characters!")

        if postdata['password1'] != postdata['password2']:
            errors.append("Password and password confirmation must match!")

        if len(errors) == 0:
            hash_pw = bcrypt.hashpw(postdata['password1'].encode(), bcrypt.gensalt())
            new_user = self.create(
                fName = postdata["fName"],
                Username = postdata["username"],
                email = postdata["email"],
                birthday = postdata["date"],
                password = hash_pw  
            )   
            return new_user
        return errors

    def validation_2(self, postdata):
        errors = []        
        if len(self.filter(email=postdata['email'])) > 0:           
            user = self.filter(email=postdata['email'])[0]
            if not bcrypt.checkpw(postdata['password'].encode(), user.password.encode()):
                errors.append('Hmm email or password incorrect, try again!')
        else:
            errors.append(' Email and password cannot be empty, please try again!')

        if errors:
            return errors
        return user

def show(request, id):
    context = {}
    if 'user_id' in request.session:
        context['logged'] = True
        context['user'] = User.objects.get(id=request.session['user_id'])
    try:
        theuser = User.objects.get(id=id)
        context['show'] = the
        return render(request, 'main/show.html', context)
    except:
        messages.warning(request, "We cannot show any details about this user who doesn't exist in our database.")
        return redirect('/')

       
class User(models.Model):
    fName = models.CharField(max_length = 255)
    Username = models.CharField(max_length= 255)
    email = models.CharField(max_length= 255)
    password = models.CharField(max_length= 20, default="none")
    birthday = models.DateTimeField(auto_now_add=False)
    items = models.ManyToManyField('self')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Item(models.Model):
    name = models.CharField(max_length = 255)
    added_by = models.ForeignKey(User, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



   

    


