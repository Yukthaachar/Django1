from django.shortcuts import render
def fact1(request):
    n1=5
    result=1
    for i in range(1,n1+1,1):
        result=result*i
    return render(request,'factorial1/index.html',{'param1':result})

