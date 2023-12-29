from django.shortcuts import render
from factorial1.forms import inputform
def fact1(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input")
            result=1
            for i in range(1,n1+1,1):
                result=result*i
            return render(request,'factorial1/index.html',{'param1':result,'param2':n1,'form':form1})
    else:
        form1=inputform()
    return render(request,'factorial1/index.html',{'form':form1})

