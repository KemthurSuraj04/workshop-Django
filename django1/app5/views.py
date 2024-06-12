from django.shortcuts import render
from app5.forms import inputform
from .models import students
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'app5/index.html',{'form':form1,'param1':"Success"})
    else:
        form1=inputform() #if it is a GET Request present an empty form
    return render(request,'app5/index.html',{'form':form1})

def show(request):
    ls=students.objects.all().values()
    con={
        'students':ls
    }
    return render(request,'app5/details.html',con)
    
    
# Create your views here.
