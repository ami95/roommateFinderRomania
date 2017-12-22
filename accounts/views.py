from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')

def goodbye(request):
    return render(request, 'goodbye.html')
