from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from accounts.forms import SignUpForm

# Create your views here.
def index(request):
    return render(request, 'base.html')

def goodbye(request):
    return render(request, 'goodbye.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
