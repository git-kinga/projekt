from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def MonaApps(request):
    return HttpResponse("Hello world!")

def index(request):
    return render(request, 'index.html')

def form(request):
    return render(request, 'Monitoring_form.html')

def login(request):
     # Process login form submission
    if request.method == 'POST':
        # Authenticate user
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            # Log the user in and redirect to home page
            login(request, user)
            
            # Set any desired session variables
            # request.session['my_var'] = 'some_value'
            
            return redirect('home.html')
        else:
            return render('login.html')
            pass
    else:
        # Render login form
        pass
    return render(request, 'login.html')