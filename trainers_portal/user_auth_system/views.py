from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('display')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('display')
    else:
        form = RegisterForm()

    context = {
        'form' : form,
        'title' : 'Register Here',
        'operation' : 'Register'
    }

    return render(request, 'signup.html', context)
    


def signin(request): 
    if request.user.is_authenticated:
        return redirect('display')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('display')
            else:
                form.add_error(None, 'Invalid Credentials!!')
    else:
        form = LoginForm()

    context = {
        'form' : form,
        'title' : 'Login Here',
        'operation' : 'Submit'
    }

    return render(request, 'signin.html', context)



def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('signin')

  
