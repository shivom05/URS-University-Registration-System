from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.


def loginuser(request):
    if request.method== "POST" : 
        username = request.POST['username']  
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
             auth.login(request,user)
             messages.success(request,"You are logged in ")
             return redirect("front/index")
        else:
             messages.error(request,"Invalid credentails")  
             return redirect('/')
    else: 
     return render(request,"login.html")
 
def registermain(request):
    if request.method== "POST" :

     first_name = request.POST['first_name'] 
     last_name = request.POST['last_name']   
     username = request.POST['username']  
     email =request.POST['email'] 
     password1 = request.POST['password1']
     password2 = request.POST['password2']
     
     if password1 == password2:
        if len(password1) < 8:
           messages.error(request,"Password too short")
        if User.objects.filter(username=username).exists():
             messages.error(request,"Username Taken")
             return redirect('registermain')
        elif User.objects.filter(email=email).exists():
             messages.error(request,"Email Already exists")
             return redirect('registermain')
        else:
             user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)          
             user.save()
             return redirect('/')
     else:
        messages.error(request,"Password does not match")
        return redirect('registermain')
    else:
     return render(request,'registermain.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

    