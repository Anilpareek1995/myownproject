from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Mostwanted


def office(request):
    if request.method == 'POST':
        username = request.POST["t1"]
        password = request.POST["t2"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'station.html')

        else:
            messages.info(request, 'invalid credentials')
            return render(request,"policelogin.html")
    else:
        return render(request, 'policelogin.html')

    return render(request, 'policelogin.html')


def mostwanted(request):
    if request.method =='POST':
       name = request.POST["t1"]
       height = request.POST["t2"]
       color = request.POST["t3"]
       crime_type = request.POST["t4"]
       crime_area = request.POST["t5"]
       victim = request.POST["t6"]
       crime_spot = request.POST["t7"]
       image = request.FILES["t8"]
       mst = Mostwanted(name=name, height=height, color=color, crime_type=crime_type, crime_area=crime_area, victim=victim, crime_spot=crime_spot, photo=image)
       mst.save()
    return render(request,'mostwanted.html')



