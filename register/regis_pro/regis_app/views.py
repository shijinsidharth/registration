# from register.regis_pro.regis_app.models import Registration
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from django.urls.resolvers import CheckURLMixin
from .models import *
def Testfn(request):
    return HttpResponse('hloo')
def html1(request):
    if request.method=="POST":
        try:
            firstname=request.POST['first_name']
            lastname=request.POST['last_name']
            username=request.POST['user_name']
            email=request.POST['email']
            password=request.POST['pass']
            propic=request.FILES['pic']
            login=Login(username=username,password=password)
            login.save()
            person=Registration(firstname=firstname,lastname=lastname,email=email,login=login,propic=propic)
            person.save()
            return render(request,'reg.html',{'msg':'registered'})
        except Exception as error:
            return render(request,'reg.html',{'msg':error})
            
        # return HttpResponse('registered succesfully')
    else:
        return render(request,'reg.html')

def reg1(request):
    firstname=request.POST['first_name']
    lastname=request.POST['last_name']
    username=request.POST['user_name']
    email=request.POST['email']
    password=request.POST['pass']
    propic=request.FILES['pic']
    login=Login(username=username,password=password)
    login.save()
    person=Registration(firstname=firstname,lastname=lastname,email=email,login=login,propic=propic)
    person.save()
    return HttpResponse('registered succesfully')
def views1(request):
    users=Registration.objects.all()
    print(users)
    return render(request,'html2.html',{'users':users})

def login(request):
    if request.method=='POST':
        try:
            user_name=request.POST['username']
            password=request.POST['password']
            log_obj=Login.objects.get(username=user_name,password=password)
            print(log_obj.id)
            request.session['log_id']=log_obj.id
            return redirect('/new/home')
        except:
            return render(request,'login.html',{'error':'please enter a valid username and password'})
    return render(request,'login.html')

def home(request):
    user_id=request.session['log_id']
    print('user_id',user_id)
    user_name=Registration.objects.get(login=user_id)
    print(user_name.firstname)
    return render(request,'home.html',{'name':user_name.firstname})

def profile(request):
    if request.method=="POST":
        print('------------------------------POST')
        try:
            new_fname=request.POST['fname']
            new_lname=request.POST['lname']
            new_email=request.POST['nemail']
            return HttpResponse('new_fname,new_lname,new_email')
        except Exception as error:
            return HttpResponse('error')
    else:
        user_id=request.session['log_id']
        user=Registration.objects.get(login=user_id)
        return render(request,'profile.html',{'user':user})

def update(request):

    if request.method=="POST":
        new_fname=request.POST['fname']
        new_lname=request.POST['lname']
        new_email=request.POST['nemail']
        user_id=request.session['log_id']
        user=Registration.objects.get(login=user_id)
        print(user.firstname)
        user.firstname=new_fname
        user.lastname=new_lname
        user.email=new_email
        user.save()
        print(user.firstname)
        print('updated----------')
        return HttpResponse('updated')
    user_id=request.session['log_id']
    user=Registration.objects.get(login=user_id)
    return render(request,'update.html',{'user'})

def insert(request):
    if request.method=="POST":
        title=request.POST['title']
        description=request.POST['description']
        image=request.FILES['photo']
        print(image)
        district=Card(title=title,description=description,photo=image)
        district.save()
        return HttpResponse('inserted',image)
    return render(request,'add_destination.html')

def show(request):
    dis=Card.objects.all()
    return render(request,'dynamic.html',{'sample':dis})
def logout(request):
    del request.session['log_id']
    return render(request,'home.html')
def json(request):
    return JsonResponse(
        {"name":"John", "age":30, "city":"New York","hobby":['reading','singing','dancing']}
    )
    # datas=Card.objects.values()
    # data=list(datas)
    # return JsonResponse({
    #     'data1':data
    # })



# def checkusername(request):
#     username=request.GET['username']
#     print(username)
#     check=Login.objects.filter(username=username).exist()
#     print(check)
#     return JsonResponse({
#         'exist':check
#     })
# Create your views here.
