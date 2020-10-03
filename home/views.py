from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')
def sample(request):
    return render(request,'sample.html')