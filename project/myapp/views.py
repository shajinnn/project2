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

def fn_upload_img(request) :
    context={}
    my_id = request.session['user_id']
    lg = Login.objects.get(id=my_id)
    if request.method == "POST" and request.FILES['uploadd']:
        
     
        myfile = request.FILES['uploadd']
        obj_upload = upload(image=myfile,fk_login=lg)
        
        obj_upload.save()
        context['img']=obj_upload.image
    return render(request,'profile.html',{'id':rg})    
    
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


    
def fn_editprofile(request):
    my_id = request.session['user_id']
    rg = registr.objects.get(id=my_id)
    context={}
    if request.method == 'POST' and request.FILES['image_upload']:
        
    
        print(rg)
        edit_fname = request.POST['firstname']

        print(edit_fname)
        edit_lastname = request.POST['lastname']
        print(edit_lastname)
        myfile = request.FILES['image_upload']
        obj = upload.objects.get(id=my_id)
        obj.image = myfile
        obj.save()
        print(myfile)
        context['img']=obj.image
        rg.firstname = edit_fname
        rg.secondname = edit_lastname
        rg.save()
    return render(request,'profile.html',{'id':rg})

def fn_addpro(request):
    print('i')




    



# def get_user_profile(request, username):
#      un =registr.objects.filter(username=username).exists()
#     return render(request, '<app_name>/user_profile.html', {"user":user})

