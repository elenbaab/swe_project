from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
# from .forms import SignupForm, LoginForm, NewUserForm
from .forms import SignupForm, LoginForm

from .models import Form

# Create your views here.

def index(request):
    return render(request, 'index.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input_view')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return render(request, 'userlanding.html')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def user_landing(request):
    return render(request, 'userlanding.html')

def user_plan(request):
    return render(request, 'userplan.html')

def user_major(request):
    return render(request, 'usermajor.html')

def input_view(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        startyear = request.POST['lastname']
        gradyear = request.POST['lastname']
        major1 = request.POST['major1']
        major2 = request.POST['major2']
        minor1 = request.POST['minor1']
        minor2 = request.POST['minor2']
        
        new_user = Form(firstname=firstname, lastname=lastname, startyear=startyear, gradyear=gradyear, major1=major1, major2=major2, minor1=minor1, minor2=minor2)
        
        new_user.save()

        return redirect('userlanding')

    return render(request, "input.html", {})