from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
##from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            user = form.save()
            login(request, user)
            print("Signup successful, redirecting to dashboard")
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request): 
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)  
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
                print("Login failed, invalid username or password.")
    else:
        print("Get request, rendering login form")
    return render(request, 'login.html', {'form': form})

def logout_view(request): 
    logout(request)
    print("Logout successful, redirecting to login")
    return redirect('login')

##@login_required
def dashboard(request):
    print(f"Rendering dashboard for user:{request.user.username}")
    return render(request, 'dashboard.html', {'user' : request.user})
