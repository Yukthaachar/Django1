from django.shortcuts import render
from fact1.forms import inputform
def home(request):
    result=1
    n1=0
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input")
            for i in range(1,n1+1,1):
                result=result*i
        return render(request,'fact1/index.html',{'param1':result,'param2':n1,'form':form1})
    else:
        form1=inputform()
    return render(request,'fact1/index.html',{'param1':result,'param2':n1,'form':form1})
# Create your views here.
