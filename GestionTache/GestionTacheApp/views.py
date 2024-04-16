from django.shortcuts import render

def home(request):
    return render(request, 'hello_world.html', {})

# Create your views here.
