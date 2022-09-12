from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User 

def homeScreen(request):
    islogin=False
    signup=False
    params={'signup':signup,'login':islogin}
    return render(request,'homeScreen.html',params)

def checkPoint(request,check):
    if(check == 'login'):
        islogin=True
        params={'login':islogin}
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"login successfully")
            else:
                messages.error(request,"invalid Credentials")
                return redirect('/')
            return redirect('/digiapp/')
        return render(request,'homeScreen.html',params)
    else:
        signup=True
        params={'signup':signup}
        if request.method=='POST':
            username=request.POST['username']
            email=request.POST['email']
            firstname=request.POST['fName']
            lastname=request.POST['lName']
            password=request.POST['password1']
            password1=request.POST['password2']
           
            #checks
            if(username.isalpha()):
                messages.error(request,'please insert your mobile number.')
                return redirect('/')
            if (len(username)!=10 or not(username.isdigit())):
                messages.error(request,'please check the number again')
                return redirect('/')
            if (len(firstname)<3 or not(firstname.isalpha()) or firstname.isdigit()):
                messages.error(request,'First Name must be alphabet')
                return redirect('/')
            if (len(lastname)<3 or not(lastname.isalpha()) or lastname.isdigit()):
                messages.error(request, 'last Name must be alphabet')
                return redirect('/')
            if(password != password1):
                messages.error(request,'Password did not matched')
                return redirect('/')
            user=User.objects.create_user(username,email,password)
            user.first_name=firstname
            user.last_name=lastname
            user.save()
            
            messages.success(request,'Thanks for Register in DigiPocket.Please login into your account')
            return redirect('/')
        return render(request,'homeScreen.html',params)


    