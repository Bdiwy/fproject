from django.shortcuts import render,redirect 
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import feature
from .models import other,Contact
# Create your views here.


f = feature.objects.all()
o = other.objects.all()

def index(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        contact = Contact.objects.create(name=name, email=email , comment=comment)
        return redirect('index')
    return render(request,'index.html',{"feat":f})


def about(request):
    return render(request,'about.html',{"feat":f})

def register(request):
    if request.method == 'POST' :
        username = request.POST['username']
        name = request.POST['name'] + request.POST['name2']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword :
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already have an account')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already have an account')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password , email=email  )
                user.save()
                return redirect('about')
        else:
                messages.info(request,'passwd not the same')
                return redirect('register')
                
    return render(request,'register.html')


def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user =auth.authenticate(username=username , password=password )
        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'passwd or email not the right')
            return redirect('login')
    else:
        return render(request,"login.html")
    

def logout(request):
    auth.logout(request)
    return redirect('/')
    
def counter(request):
    txt=request.POST['txt']
    amount= len(txt.split())
    return render(request,"counter.html",{'amount':amount})


def post(request,pk):
    return render(request,'post.html',{'pk':pk})

def center(request):
    post=[1,2,3,4,5,6,7,8]
    return render(request,'center.html',{'post':post})