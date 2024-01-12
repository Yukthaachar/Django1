from django.shortcuts import render
from holiday1.forms import inputform
from holiday1.holidays import holiday 

def home(request):
    result=[]
    n1=[]
    if request.method=='POST':
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input")
            result=holiday(n1)
            
        return render(request,'holiday1/index.html',{'param1':result,'param2':" is holiday for ",'param3':n1,'form':form1})
    else:
        form1=inputform()
    return render(request,'holiday1/index.html',{'param1':result,'param2':" is holiday for ",'param3':n1,'form':form1})

