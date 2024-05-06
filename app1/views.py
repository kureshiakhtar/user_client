from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Client
# Create your views here.


# def Signup(request):
#     if request.method == 'POST':
#         uname = request.POST.get('name')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('password1')
#         pass2 = request.POST.get('password2')
#         print(uname, email, pass1, pass2)
#     return render(request, 'signup.html')


# def Signup(request):
#     if request.method == 'POST':
#         uname = request.POST.get('name')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('password1')
#         pass2 = request.POST.get('password2')
#         return HttpResponse("usr created successfully")
#     return render(request, 'signup.html')


# def Signup(request):
#     if request.method == 'POST':
#         uname = request.POST.get('name')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('password1')
#         pass2 = request.POST.get('password2')
#         my_user = User.objects.create_user(uname, email, pass1)
#         my_user.save()
#         return redirect('login')
#     return render(request, 'signup.html')


def Signup(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("you have entered Incorrect password")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        print(username, pass1)
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('next')
        else:
            return HttpResponse("username & password is incorrect")
    return render(request, 'login.html')


# def logoutpage(request):
#     if request.method == "POST":
#         logout(request)
#         return redirect('login')
#     return render(request, 'logout.html')

def logoutpage(request):
    logout(request)
    return redirect('login')


def Next(request):
    return render(request, 'next.html')


def create_client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        creator = request.POST.get('creator')
        client = Client(name=name, creator=creator)
        client.save()
        return redirect('next')
    return render(request, 'client.html')


def fetch(request):
    emps = Client.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'fetch_client.html', context)


# def remove(request):
#     emps = Client.objects.all()
#     context = {
#         'emps': emps
#     }
#     return render(request, 'remove_client.html', context)


def remove(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Client.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Client removed sucessfully")
        except:
            return HttpResponse("please enter a valid EMP id")
    emps = Client.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_client.html', context)
