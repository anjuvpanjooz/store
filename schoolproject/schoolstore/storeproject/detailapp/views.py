from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from  .models import ContactQuery

from detailapp.models import Course


# Create your views here.
def detail(request,id):

        try:
            detail = Course.objects.get( id=id)
        except Exception as e:
            raise e
        return render(request, 'detail.html', {'detail': detail})
def new(request):

    return render(request,"new.html")
def add(request):
    if request.method=='POST':
        name=request.POST['Name']
        dob=request.POST['DOB']
        age=request.POST['age']
        email_id=request.POST['email_id']
        if name != "":
            contact = ContactQuery()
            contact.Name = name
            contact.DOB = dob
            contact.age = age
            contact.email_id = email_id
            contact.save()
            messages.info(request, 'order confirmed')
        else:
            pass


    else:
        return render(request, "add.html")
