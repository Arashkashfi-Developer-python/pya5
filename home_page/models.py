from django.db import models
from datetime import datetime 
class data (models.Model) :
    topic  = models.CharField(max_length=10000)
    img = models.ImageField()
    data =  models.CharField(max_length=1000000000000000000000000000000000,null=True,blank=True,default="not load yet")
    come_out = models.DateTimeField()
    def __str__(self):
        return self.topic
class tikmodel (models.Model) :
    user = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True)
    tiket_id=id
    ticket_link = models.IntegerField(max_length=10000000000000,null=True,blank=True)
    name=models.CharField(max_length=10000000000000000000)
    email= models.EmailField(max_length=1000000000000000)
    topic = models.CharField(max_length=1000000000,null=True,blank=True)
    tik = models.CharField(max_length=11111111188888888888888888888888888888888888888888888888888888888888)
    answered= models.BooleanField(default=False)
    answers = models.CharField(max_length=10000000000000)
    timeuploaded =  models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return   self.topic 
class checktik (models.Model) :
    user = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=10000000000000000000) 
    timecheck = models.DateTimeField(auto_now_add=True)
class fileinput(models.Model):
    date = models.ForeignKey(data, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    name = models.CharField(max_length=10000000000000000000,null=True,blank=True) 
    data =  models.FileField(upload_to="files",null=True,blank=True)
    timeuploaded =  models.DateTimeField(auto_now_add=True,null=True,blank=True)
class imginput(models.Model): 
    date = models.ForeignKey(data, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    name = models.CharField (max_length=10000000000000000000,null=True,blank=True)
    img = models.ImageField(upload_to="img",null=True,blank=True)
    timeuploaded =  models.DateTimeField(auto_now_add=True,null=True,blank=True)


    def __str__(self):
        return self.name
