from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
# from .forms import SignupForm, LoginForm, NewUserForm
from .forms import SignupForm, LoginForm

from .models import Form

# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input_view')
            # input_view(request)
            #return render(request, 'input.html')
            # new_user_form = NewUserForm()
            # return input_view(request)
            # return render(request, 'newuserinfo.html', {'new_user_form': new_user_form})
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
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
        major = request.POST['major']
        grad = request.POST['grad']

        new_user = Form(major=major, grad=grad)
        new_user.save()

        return redirect('userlanding')

    return render(request, "input.html", {})