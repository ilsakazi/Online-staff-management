from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import leaveform
from .models import *
from django.contrib import messages
from django.template.loader import get_template

# Create your views here.
def leaves(request):
    if request.method== 'POST':
        l=leaveform(request.POST)
        if l.is_valid():
            print('form is valid')
            try:
                l.save()
                messages.info(request, 'Leave Send successfully')
                return redirect('/l/readleaves/')
                # return HttpResponse('form is submitted')
            except:
                pass
        else:
            pass
    else:
        l=leaveform()
    return render(request,'leaves.html',{'form':l})

def readleaves(request):
    if request.method=='POST':
        data=request.POST
        name=data.get('name')
        cno=data.get('cno')
        email=data.get('email')
        msg=data.get('msg')
        image=request.FILES.get('image')

        print(name,cno,email,msg,image)
        Leaves.objects.create(name=name, cno=cno, email=email, msg=msg, image=image)
        return redirect('/l/readleaves/')

    l=Leaves.objects.all().order_by('name')
    if request.GET.get('search'):
        a=request.GET.get('search')
        print(a)
        m=Q(Q(name_icontains=a) | Q(subject_icontains=a))
        l=Leaves.objects.filter(m)
    return render(request,'readleaves.html',{'l':l})

def deleteleaves(request,id):
    l=Leaves.objects.get(id=id)
    l.delete()
    messages.info(request, 'Deleted successfully')
    return redirect('/l/readleaves/')

def updateleaves(request,id):
    l=Leaves.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        name=data.get('name')
        email=data.get('email')
        cno=data.get('cno')
        msg=data.get('msg')
        image=request.FILES.get('image')
        l.name = name
        l.email = email
        l.cno = cno
        l.msg = msg
        if image:
            l.image = image
        l.save()
        messages.info(request, 'Updated successfully')
        return redirect('/l/readleaves/')
    return render(request,'updateleaves.html',{'l':l})

