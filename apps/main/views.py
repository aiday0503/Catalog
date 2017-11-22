from __future__ import unicode_literals
from .models import User
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import datetime

def index(request):
    try:
        request.session['user_id']
    except:
        request.session['user_id'] = []
    if request.session['user_id']:
        return redirect('/success')
    return render(request, "main/index.html")

def create(request):
    if request.method =='POST':
        result = User.objects.validation(request.POST)
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect('/')        
    request.session['user_id'] = result.id
    messages.success(request, "Successfully Registered")
    return redirect('/success')

def login(request):
    result = User.objects.validation_2(request.POST)
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect('/')
    
    request.session['user_id'] = result.id
    messages.success(request, "Thanks for logging in!")
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except:
        return redirect('/')
    
    userIds = {}
    allUsers = User.objects.all()
    for user in allUsers:
        userIds[user.id] = user
    print allUsers[2].fName

    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "items" : Item.objects.all(),
        "userIds": userIds
    }
    print context["userIds"]
    

    return render(request, "main/success.html", context)

def show(request, id):
    return render(request, 'main/show.html', {"item" : Item.objects.filter(id=id)})

def removeitem(request,id):
    user = User.objects.get(id=request.session['user_id'])
    #user.items.remove(Item.objects.get(id=id))
    return redirect('/success')   


def additem(request, id):
    user = User.objects.get(id=request.session['user_id'])
    print "123123"
    print Item.objects.get(id=id).id
    user.items.add(Item.objects.get(id=id).id)
    print Item.objects.all()
    return redirect('/success') 


def createitem(request):       
    return redirect('/success')
   

def logout(request):
    request.session.clear()
    return render(request, "main/index.html")