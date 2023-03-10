from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as loginUser, logout
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMultiAlternatives
from auth_system.forms import Employee_form,leave_form
from datetime import date
from auth_system.models import holiday
from datetime import datetime

# Create your views here.

def HomePage(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {"form": form1}
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context = {"form": form}
            return render(request, 'login.html', context=context)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists..! Try another ..')
                return redirect('signup')

            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()

                messages.info(request,"User Successfully Created")
                return redirect('forms1')
        else:
            messages.info(request,"Password is not matching")
            return redirect('login')
    else:
        return render(request,'signup.html')

def signout(request):
    logout(request)
    return redirect('/')

def forms1(Request):
    form = Employee_form()
    if Request.method == "POST":
        form = Employee_form(Request.POST)
        form.save(commit=True)
        if form.is_valid():
            form.save(commit=True)
            return redirect('login')
        else:
            print("Error form invalid")
    return render(Request,"forms1.html",{'form':form})

def forms2(Request):
    form = leave_form()
    if Request.method == "POST":
        form = leave_form(Request.POST)
        Start_date = Request.POST['Start_date']
        End_date = Request.POST['End_date']


        print(Start_date)
        print(type(Start_date))
        if End_date >= Start_date:
            form.save(commit=True)
            import datetime
            # Startdate 2023-03-11
            yyyy = int(Start_date[0:4])
            mm = int(Start_date[5:7])
            dd = int(Start_date[-2:])
            # enddate
            yyyy_e = int(End_date[0:4])
            mm_e = int(End_date[5:7])
            dd_e = int(End_date[-2:])
            start = datetime.date(yyyy, mm, dd)
            end = datetime.date(yyyy_e, mm_e, dd_e)
            daydiff = end.weekday() - start.weekday()
            days = ((end - start).days - daydiff) / 7 * 5 + min(daydiff, 5) - (max(end.weekday() - 4, 0) % 5)
            print(start, '***', days, '***', end)
            if form.is_valid():
                    form.save(commit=True)
                    return HttpResponse("<h1>You have successfully applied  %d days of leaves</h1>"%days)
            else:
                print("Error form invalid")
        else:
            messages.info(Request, "Please enter the correct date")
            return redirect('forms2')
    return render(Request,"forms2.html",{'form':form})




