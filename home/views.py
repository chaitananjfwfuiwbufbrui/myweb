from django.shortcuts import render,HttpResponse
from home.models import Home
from  django.contrib import messages
# Create your views here.
def home(request):
    if request.method =="POST":
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            ins = Home(name=name,email=email, subject1=subject, message1=message)
            ins.save()
            messages.success(request,'YOUR response has been recived')
            print("done for the data")
    return render(request,'index.html')
def sample(request):
    return render(request,'sample.html')