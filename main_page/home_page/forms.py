from django import forms
from . import  * 
from .models import  *
class tikform (forms.ModelForm) :
    name = forms.CharField(label="name", widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'your name'}))
    email = forms.EmailField(label="email",widget=forms.TextInput(attrs={"class":'form-control', "placeholder":"your email"}))
    tik = forms.CharField(label="ask", widget=forms.Textarea(attrs={"class":"form-control",'placeholder':'ask thing you want '}))
    topic = forms.CharField(label="topic", widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'topic'}))


    class Meta () :
        model = tikmodel     
        fields = ['name','email',"tik","topic"]
class chtikforms (forms.ModelForm) :
    name =  forms.CharField(label="name", widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'your name'}))
    class Meta () :
        model =checktik
        fields = ['name']
class tiklinkform (forms.ModelForm) :
    name = forms.CharField(label="name", widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'your name'}))
    email = forms.EmailField(label="email",widget=forms.TextInput(attrs={"class":'form-control', "placeholder":"your email"}))
    tik = forms.CharField(label="ask", widget=forms.Textarea(attrs={"class":"form-control",'placeholder':'ask thing you want '}))
    topic = forms.CharField(label="topic", widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'topic'}))

    ticket_id = forms.IntegerField(label="tiket id", widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'tiket id'}))
    class Meta () :
        model = tikmodel
        fields = ['ticket_id','name','email',"tik",'topic']