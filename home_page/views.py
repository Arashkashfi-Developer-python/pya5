from django.shortcuts import render ,redirect
from .models import data
from .forms import * 
from . import forms 
i = False
tnt = False
def seetik (request,pk) :
    tik = tikmodel.objects.get(id=pk)
    print(tik)
    print(pk)
    return render(request,"seetik.html",{"data":tik})
def anwsertik (request) : 
    global tnt 
    if  request.method == 'POST' or tnt :
        forms = chtikforms(request.POST)
        if forms.is_valid() :
            if not tnt : 
                n=forms.save(commit=False)
                name = n.name 
            forms.save()
            tnt = True 
            from . import models 
            mydata = models.tikmodel.objects.filter(name=name).values()
            if mydata is None : 
                print("no data") 
                mydata = models.tikmodel.filter(name=name)
                print(mydata)
            print(mydata)
            tnt = False
            return render (request,"anwsers.html",{"data":mydata})
        else : 
            print("not valid")
            pass 
    else : 
        print('not post')
        form = chtikforms() 
        return render (request,"your_name.html",{"forms":form})
def tik (request) :
    global i 
    if request.method=="POST"  and i==True :
        forms = tikform(request.POST)
        if forms.is_valid() : 
            forms.save()
            print("valid")
            return redirect("anwsertik")
        else : 
            print("not valid")
            print(forms.errors)
            i =True
            text = data.objects.all()
            forms = tikform()
            return render(request,"tik.html",{"data":text,'forms':forms}) 
    # we use i for that we can understand that if the code run this part
    else:
        i =True
        text = data.objects.all()
        forms = tikform(request)
        return render(request,"tik.html",{"data":text,'forms':forms}) 
def main_page (request) :
    text = data.objects.all()
    return render(request,"main_page.html",{"data":text})
def link_tik (request) :
    if request.method=="POST" :
        forms = tiklinkform(request.POST)
        if forms.is_valid() : 
            forms.save()
            print("valid")
            return redirect("anwsertik")
        else : 
            print("not valid")
            print(forms.errors)
            i =True
            text = data.objects.all()
            forms = tiklinkform()
            return render(request,"tik_link.html",{"data":text,'forms':forms}) 
    # we use i for that we can understand that if the code run this part
    else:
        forms = tiklinkform(request)
        return render(request,"tik_link.html",{'forms':forms}) 