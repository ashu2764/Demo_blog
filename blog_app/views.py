from django.shortcuts import render,redirect
from blog_app.models import blog
from .form import blog_ok,contect_ok
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def blogs(request):
    
    if request.method =='GET':
        result = blog_ok()
        
        # data=blog.objects.all()
        return render (request,'blogs.html',{'result':result})
    
    else:
        result = blog_ok(request.POST ,request.FILES)
        result.save()
        
        
        return render(request,'blogs.html')
    
def show(request):
    return render (request,"show.html")
    

def home(request):
    data=blog.objects.all()
    return render (request,'index.html',{'data':data})


def about(request):
    return render (request,'about.html')

def contect(request):
    if request.method =='GET':
        result = contect_ok()
        
        # data=blog.objects.all()
        return render (request,'contect.html',{'result':result})
    
    else:
        result = contect_ok(request.POST ,request.FILES)
        result.save()
        
        p="thanks for submitting yours details"
        return render(request,'contect.html',{'p':p})


    # return render(request,'contect.html')

def ourproducts(request):
    return render (request,'ourproducts.html')

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USER ALLREADY EXISTS")
                return redirect("register")
            else:

                User.objects.create_user(username=username,password=password)
                return render (request,'login.html')
        else:
            messages.info(request,"PASSWORD DOES NOT MATCH")
            return redirect("register")
           
    else:
        return render (request,'login.html')
    

def login(request):
      if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user :
            auth.login(request,user)
            return redirect("home")
        else:
            messages.info(request,"Username/Password does not match ")

            return redirect("login")


      return render (request,'login1.html')
   
        
def logout(request):
    auth.logout(request)
    return redirect("login")


