from django.shortcuts import render
from django.shortcuts import HttpResponse

def about (request):
    #return HttpResponse ('hi there i am hello world...')
    return render(request,'about.html')
def home (request):
    #return HttpResponse ('iam fucking good')
    return render(request, 'home.html')