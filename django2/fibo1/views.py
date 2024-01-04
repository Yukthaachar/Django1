from django.shortcuts import render
from fibo1.forms import inputform 
def fibonacci(n1):
    if n1==1:
        return 0
    elif n1==2:
        return 1
    else:
        return fibonacci(n1-1)+fibonacci(n1-2)
    
def home(request):
    result = 0  
    n1 = 0
    if request.method=='POST':
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input")
            result=fibonacci(n1)
        return render(request,'fibo1/index.html',{'param1':result,'param2':n1,'form':form1})
    else:
        form1=inputform()
    return render(request,'fibo1/index.html',{'param1':result,'param2':n1,'form':form1})

# Create your views here.
