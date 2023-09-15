from django.shortcuts import render  
#importing loading from django template  
from django.template import loader    
# Create your views here.  
from django.http import HttpResponse  
from captura.form import EmpForm  
  
def hola(request):  
    return HttpResponse("<h2>Hello, probando to Django!</h2>")   

def index(request):  
    stu = EmpForm()  
    return render(request,"index.html",{'form':EmpForm})  