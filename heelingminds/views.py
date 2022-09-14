from django.shortcuts import render

from home.models import enquiry,therapies

# Create your views here.
def index(request):
    if request.method=="POST":
       
       
        name = request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        issue=request.POST.get('issue')
       
        
        
        ins=enquiry(name=name, email=email,phone=phone,message=message,issue=issue )
        
        ins.save()
    return render(request, 'index.html')
def navigation(request):
    return render(request, 'navigation.html')
def checkout(request):
    return render(request, 'checkout.html')
def payment(request):
    return render(request, 'payment.html')
def therapy(request):
    if request.method=="POST":
        
        name = request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        phone=request.POST['phone']
       
        issue=request.POST.get('issue')
        gender=request.POST.get('gender')
        a=therapies(name=name, email=email,phone=phone,issue=issue,age=age,gender=gender)
        a.save()
    return render(request, 'therapy.html')