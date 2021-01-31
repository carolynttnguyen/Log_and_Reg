from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    # validate user data
    # grab method from models and store in a var
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        #if no errors:... redirect
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect('/')
        user_pw = request.POST['password']
        hash_pw = bcrypt.hashpw(user_pw.encode(), bcrypt.gensalt()).decode()
        print(hash_pw)

        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hash_pw,
        )
        print(new_user)
        request.session['user_id']= new_user.id
        request.session['user_name']= f"{new_user.first_name} {new_user.last_name}"
        return redirect('/success')
    return redirect('/')
    
def login(request):
    if request.method == 'POST':
        logged_user = User.objects.filter(email= request.POST['email'])
        if logged_user:
            logged_user = logged_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id']= logged_user.id
                request.session['user_name']= f"{logged_user.first_name} {logged_user.last_name}"
                return redirect('/success')
    return redirect('/')  

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request,'success.html')

def logout(request):
    request.session.clear()
    return redirect('/')