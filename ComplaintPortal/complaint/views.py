from django.shortcuts import redirect, render
from complaint.models import Student,AdminLogin,Complaint
from django.http.response import HttpResponse, HttpResponseRedirect
from complaint.models import Complaint
# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    if(request.method == 'POST'):
        roll_number = request.POST["name"]
        password = request.POST["password"]
        try:
            objects = Student.objects.get(roll_number = roll_number,password=password)
        except:
            error = "Please Check the Credentials you have typed"
            return render(request,'login.html',{'error':error})
        return HttpResponseRedirect('form/'+str(objects.id))
    return render(request,'login.html',{'forgot': 'Student Log In'})

def admin(request):
    pass

def form(request,id1):
    return render(request,'form.html',{'id1':id1})

def complaint(request):
    return render(request,'complaint_register.html')
    
def submit(request,id1):
    if request.method == 'POST':
        date_incident = request.POST['date']
        time_incident = request.POST['time']
        place_incident = request.POST['place']
        description = request.POST['desc']
        student = Student.objects.get(id=id1)
        done = "<h3>Successfully Registered Your Complaint</h3>"
        complaint = Complaint.objects.create(student = student,place=place_incident,date_time = date_incident+' '+time_incident, desc = description)
        return render(request,'form.html',{'done':done,'id1':id1})
    else:
        return render(request,'form.html',{'id1':id1})

def submitted(request,id1):
    list1=[]
    objects = Complaint.objects.all()

    return render(request,'complaints.html',{'objects':objects,'id1':id1})



def admin_login(request):
    if(request.method == 'POST'):
        print("hello world")
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            objects = AdminLogin.objects.get(emailid = email,password=password)
        except:
            error = "Please Check the Credentials you have typed"
            return render(request,'admin_login.html',{'error':error})
        
        return HttpResponseRedirect('adminpage/'+str(objects.id))
    return render(request,'admin_login.html')

def forgot_password(request):
    if request.method == "POST":
        email = request.POST["email"]
        try:
            objects = Student.objects.get(mail=email)
            password = request.POST["password"]
            objects.password = password
            objects.save()
        except:
            try:
                objects = AdminLogin.objects.get(emailid=email)
                password = request.POST["password"]
                objects.password = password
                objects.save()
            except:
               return render(request,'forgot.html',{'error':'Please Check the Credentials you have typed'})
            return render(request,'admin_login.html',{'error':'Successfully Changed your password'})
    return render(request,'login.html',{'error':'Successfully Changed your password'})

def myaccount(request,id1):
    
    objects = Student.objects.get(id=id1)
    return render(request,'myaccount.html',{'objects': objects,'id1':id1})

def change_password(request,id1):
    objects = Student.objects.get(id=id1)
    if request.method == "POST":
        objects = Student.objects.get(id=id1)
        email = objects.mail
        roll_number = objects.roll_number
        password=request.POST['password']
        objects = Student.objects.get(mail=email,roll_number =roll_number)
        objects.password = password
        objects.save()
        return render(request,'myaccount.html',{'id1':id1,'objects':objects})
    return render(request,'changepassword.html',{'id1':id1,'objects':objects})