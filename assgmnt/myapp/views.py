from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators  import api_view
from rest_framework.response import Response 
from . models import *
# Create your views here.
def myIndex(request):
    # print('working')
    # message = {'data':'welcome to baabtra'}
    return render(request,'fbc.html')


def fn_userLogin(request):
    print(request.POST)
    user_data = request.POST['username']
    psd_data = request.POST['password']
    try:
        usr = Login.objects.get(username=user_data)
        if usr.password == psd_data:
            request.session['user_id'] = usr.id
            return render(request,'successfullylogin.html')
        else:
            return render(request,'psss.html')
    except Exception as e:
        print(str(e))
        return render(request,'fb1.html')

def fn_reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        un = Login.objects.filter(username=username).exists()
        if un == False:
            fstname = request.POST['textt1']
            sndname = request.POST['textt2']
            dob     = request.POST['dob']
            gender  = request.POST['radio']
            password = request.POST['password']
    try:
        login =Login(username=username,password=password)
        login.save()

        if login.id > 0:
            userdetails_obj = registr(firstname=fstname,secondname=sndname,dob=dob,gender=gender,fk_login=login)
            userdetails_obj.save()
            if userdetails_obj.id>0:
                return render(request,'fbc.html')
                
    except Exception as e:
        print(str(e))
        return HttpResponse('invalid')

def fn_change_pass(request):
    if request.method == "POST":
        user_id = request.session['user_id']
        print('session id:',user_id)
        exist_password = request.POST['current']
        print('current password:'+exist_password)
        new_password = request.POST['change']
        print('new password:' +new_password)
        login = Login.objects.get(id=user_id)
        print(login.password)
        if exist_password == login.password:
            login.password = new_password
            login.save()
            return render(request,'successfullylogin.html',{'msg':'password updated'})
        else:
            return HttpResponse('invalid')
    
    return render(request,'changep.html')     

def fn_profile(request):
    my_id = request.session['user_id']
    try:
        rg = registr.objects.get(id=my_id)
    except Exception as e:
        print(str(e))
    
    return render(request,'profile.html',{'id':rg})
    print(rg)
    
# def get_user_profile(request, username):
#      un =registr.objects.filter(username=username).exists()
#     return render(request, '<app_name>/user_profile.html', {"user":user})

