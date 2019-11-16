from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Post
from office.models import Mostwanted
from django.core.paginator import Paginator



def register(request):
    if request.method =='POST':
       first_name = request.POST["t1"]
       last_name = request.POST["t2"]
       username = request.POST["t3"]
       email = request.POST["t4"]
       password1 = request.POST["t5"]
       post = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
       post.save()
    return render(request, 'register.html')
            
def userlogin(request):
    if request.method=='POST':
        username = request.POST["t1"]
        password = request.POST["t2"]
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            request.session['username'] = username

            return render(request,"dashboard1.html")
            

        else:
            messages.info(request,'invalid credentials')
            return redirect("userlogin")
    else:
        return render(request,'userlogin.html')


def userdashboard(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard1.html')

    else:
        HttpResponse('login first')

def post(request):   
    if request.method =='POST':
        email = request.POST["t1"]
        name = request.POST["t2"]
        write_post = request.POST["t3"]
        address = request.POST["t4"]
        city = request.POST["t5"]
        state = request.POST["t6"]
        xp = request.POST["t7"]
        post = Post(email=email,name=name,write_post=write_post,address=address,city=city,state=state,zip=xp)
        if post == True:
          messages.info(request,'post has been saved!!!!')
          post.save()       
    return render(request,'post.html')

def about(request):
    username = request.session['username']
    data = User.objects.all().filter(username=username)
    return render(request,'profile.html',{'datas': data})


def showwanted(request):
    data = Mostwanted.objects.all()
    paginator = Paginator(data, 1)
    page = request.GET.get('page')
    datas = paginator.get_page(page)

    return render(request, 'showwanted.html', {'datas': datas})

def profile(request):
    username = request.session['username']
    data = User.objects.all().filter(username=username)
    return render(request, 'profile.html', {'datas': data})





