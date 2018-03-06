from django.shortcuts import render
from django.http import HttpResponse
from maintainer.forms import details_form
from maintainer import pic
# Create your views here.
#pid = 0,pclass=0,ag = 0,sib=0,par=0,mal=0,fem=0,ec=0,eq=0,es=0
def index(request):
    mydict = {'var':"this has been successfully linked you can proceed further Thank You!"}
    return render(request,'index.html',context=mydict)
def form_fill(request):
    form = details_form()

    if request.method =="POST":
        form = details_form(request.POST)
        if form.is_valid():
            li = [passengerid,passengerclass,age,siblings,parents,fare,female,male,c,q,s]
            form.save(commit=True)
            return index(request)
        else:
            print("Form validation Failed")
    return render(request,"forms.html",{'form':form})

def predict(request):

    val = pic.prediction()
    dicti = {'fin':val}
    return render(request,'predictor.html',context=dicti)
