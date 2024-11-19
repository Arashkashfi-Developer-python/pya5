from django.contrib import admin
from .models import * 
class file (admin.TabularInline):
    model = fileinput
    extra = 1
class img (admin.TabularInline):
    model = imginput
    extra =  1 # Number of empty inline forms you want
class tiketmodeladmin(admin.TabularInline):
    model = tikmodel
    extra =  1 # Number of empty inline forms you want

class tikadmin(admin.ModelAdmin):
    inlines = [tiketmodeladmin]
class fileimg(admin.ModelAdmin):
    inlines = [file,img]
    
admin.site.register(data,fileimg)
admin.site.register(tikmodel,tikadmin)
admin.site.register(checktik)

# Register your models here.
