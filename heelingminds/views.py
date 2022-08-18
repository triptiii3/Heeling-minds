from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def navigation(request):
    return render(request, 'navigation.html')
def therapy(request):
    return render(request, 'therapy.html')