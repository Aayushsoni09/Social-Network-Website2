from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
def index(request):
    return render(request,'main/base.html');

 
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        x=auth.authenticate(username=username,password=password)
        if x is None:
            return render(request, 'main/login.html')

        else:
            request.session['username'] = username
            return redirect('main')
    else:
        return render(request,'main/login.html')

def signup(request):
    if request.method=='POST':
        username = request.POST['ausername']
        firstname = request.POST['afirstname']
        lastname = request.POST['alastname']
        email = request.POST['amail']
        password = request.POST['apassword1']
        x = User.objects.create_user(username=username,is_superuser=True,first_name=firstname,last_name=lastname,email=email,password=password)
        x.save()
        return redirect('login')
    else:
        return render(request, 'adminpanel/adminsignup.html')
  
