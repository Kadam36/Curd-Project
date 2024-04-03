from django.shortcuts import render,redirect
from Crudassignment.models import Emp

# Create your views here.
def home(request):
    empdata = Emp.objects.all()
    return render(request,'home.html',{'empdata':empdata})

def Addemp(request):
    if(request.method=="GET"):
        return render(request,'Addemp.html')
    else:
        ename = request.POST["Name"]
        loc = request.POST["Location"]
        email = request.POST["Email"]

        try:
            user = Emp.objects.get(ename=ename)
        except:
            user = Emp(ename=ename,elocation=loc,email=email)
            user.save()
            return redirect(home)
        else:
            message = "Username already exist try another Username"
            return render(request,'Addemp.html',{'message':message})
    
def delete(request,id):
    emp = Emp.objects.get(id=id)
    emp.delete()
    return redirect(home)

def update(request,id):
    if request.method == "GET":
        emp = Emp.objects.get(id=id)
        return render(request,'update.html',{'emp':emp})
    else:
        ename = request.POST["Name"]
        loc = request.POST["Location"]
        email = request.POST["Email"]

        emp = Emp(
            id = id,
            ename = ename,
            elocation = loc,
            email = email,
        )
        emp.save()
        return redirect(home)