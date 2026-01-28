import datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from .form import facform
from .models import *
from django.shortcuts import render,redirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template import loader

# Create your views here.
@login_required(login_url='/login/')
def addfaculty(request):
    if request.method == 'POST':
        return HttpResponse("Method Not Allowed")
        f=facform(request.POST)
        if f.is_valid():
            print('form is valid')
            try:
                f.save()
                messages.info(request, 'Successfully Added Staff')
                return HttpResponseRedirect(reverse("read"))
                return redirect('/read/')
                #return HttpResponse('form is submitted')
            except:
                pass
        else:
            pass
    else:
        f=facform()
    return render(request,'addfaculty.html',{'form':f})

def read(request):
    u = request.user.id
    print(u)

    print("----------------")

    now = datetime.datetime.now()
    print(now)
    year = now.year
    month = now.month
    day = now.day

    if len(str(day)) == 1 :
        day = "0" + str(day)

    if len(str(month)) == 1 :
        day = "0" + str(month)

    print(year,month,day)

    print("----------------")

    if request.method=='POST':
        data=request.POST
        name=data.get('name')
        image=request.FILES.get('image')
        roomno = data.get('roomno')
        div = data.get('div')
        sem = data.get('sem')
        subject = data.get('subject')

        print(name,image,roomno,div,sem,subject)
        Faculty.objects.create(name=name, image=image, roomno=roomno, div=div, sem=sem, subject=subject, user_id=u)
        return redirect('/read/')

    f=Faculty.objects.all().order_by('name')
    if request.GET.get('search'):
        a=request.GET.get('search')
        print(a)
        m=Q(Q(name__icontains=a) | Q(subject__icontains=a))
        f=Faculty.objects.filter(m)
    return render(request,'read.html',{'f':f})

def delete(request,id):
    f=Faculty.objects.get(id=id)
    f.delete()
    messages.info(request, 'Successfully Deleted')
    return redirect('/read/')

def update(request,slug):
    f = Faculty.objects.get(slug=slug)
    if request.method=='POST':
        data = request.POST
        name = data.get('name')
        image = request.FILES.get('image')
        roomno = data.get('roomno')
        div = data.get('div')
        sem = data.get('sem')
        subject = data.get('subject')
        f.name=name
        if image:
            f.image=image
        f.roomno = roomno
        f.div = div
        f.sem = sem
        f.subject = subject
        f.save()
        messages.info(request,'Updated Successfully')
        return redirect('/read/')
    return render(request,'update.html',{'f':f})

def register(request):
    if request.method=="POST":
        data=request.POST
        print(data)
        uname=data.get('username')
        fname=data.get('first_name')
        lname=data.get('last_name')
        image=request.FILES.get('image')
        email=data.get('email')
        address=data.get('address')
        password=data.get('password')

        print(uname,fname,lname,image,email,password,address)
        u=User.objects.filter(username=uname)
        if u.exists():
            messages.info(request,'username is already exists')
        user=User.objects.create_user(username=uname,
                                      first_name=fname,
                                      last_name=lname,
                                      email=email,

                                      )
        user.set_password(password)
        u1=Register.objects.create(address=address,user=user,image=image)
        user.save()
        messages.info(request,'user registed successfully')
        return redirect('/base/')
        #return HttpResponse('user registed successfully')
    return render(request,'register.html')

def Login(request):
    if request.method=="POST":
        data=request.POST
        print(data)
        uname=data.get('username')
        password=data.get('password')
        print(uname,password)
        if not User.objects.filter(username=uname).exists():
            messages.error(request,'user is invalid')
            return redirect('/Login/')
        else:
            u=authenticate(username=uname, password=password)
            if u is None:
                messages.error(request,'password is invalid')
                return redirect('/Login/')
            else:
                login(request,u)
                return redirect('/base/')

    return render(request,'login.html')


def base(request):
    return render(request,'base.html')

def Logout(request):
    logout(request)
    return redirect('/Login/')

def emailsend(request):
    subject = "Django"
    message = "Project"
    fromemail = settings.EMAIL_HOST_USER
    list = ['sujanseikh444@gmail.com']
    send_mail(subject, message, fromemail, list)
    messages.info(request,'Your mail is send successfully')
    return redirect('/read/')
def pdfcreate(request):
    f=Faculty.objects.all()
    template_path = 'read1.html'
    context = {'f':f}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the templates and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, )
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def read1(request):
    u = request.user.id
    print(u)
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        image = request.FILES.get('image')
        roomno = data.get('roomno')
        div = data.get('div')
        sem = data.get('sem')
        subject = data.get('subject')

        print(name, image, roomno, div, sem, subject)
        Faculty.objects.create(name=name, image=image, roomno=roomno, div=div, sem=sem, subject=subject, user_id=u)
        return redirect('/read1/')

    f = Faculty.objects.all()#.order_by('name')
    return render(request, 'read1.html', {'f': f})

def todolist(request):
    return render(request,'todolist.html')

def profile(request):
    return render(request,'profile.html')

def p1(request):
    return render(request,'p1.html')

def p2(request):
    return render(request,'p2.html')

def p3(request):
    return render(request,'p3.html')

def dash(request):
    return render(request,'dash.html')