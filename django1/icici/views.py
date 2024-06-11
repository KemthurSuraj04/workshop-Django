from django.shortcuts import render
from icici.forms import inputform
from .models import Accounts
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            form1.save()
            try:
                last_account = Accounts.objects.latest('id')
                new_customer_id = last_account.customer_id
            except Accounts.DoesNotExist:
                new_customer_id = 8001
            return render(request,'icici/index.html',{'form':form1,'cus_id':new_customer_id})
    else:
        form1=inputform() #if it is a GET Request present an empty form
    return render(request,'icici/index.html',{'form':form1})


# Create your views here.
