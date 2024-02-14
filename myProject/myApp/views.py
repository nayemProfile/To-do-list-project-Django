from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import *
from django.contrib import messages
from datetime import date

# forget password import section start
import random
from myProject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# forget password import section end



'''note: change the url path 
and add "token.py" file in the App 
and setup the "settings.py" file  
and install six packeg
and some update the singup function
'''
#email varification code start
from django.contrib.auth import get_user_model
from myApp.tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

def activate(request,uid64,token):
    User=get_user_model()
    try:
        uid= force_str(urlsafe_base64_decode(uid64))
        user=User.objects.get(pk=uid)

    except:
        user =None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active=True
        user.save()
        return redirect('singIn')
    return redirect('singIn')


def activateEmail(request,user,to_mail):
    mail_sub='Active your user Account'
    message=render_to_string("template_activate.html",{
        'user': user.username,
        'domain':get_current_site(request).domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
        'protocol':'https' if request.is_secure() else 'http'
    })
    email= EmailMessage(mail_sub, message, to=[to_mail])
    if email.send():
        messages.success(request,f'Dear')
    else:
        message.error(request,f'not')
    #email varification code end 
    
  
  

# forget  password code start 
def forget_pass(request):
    if request.method == "POST":
        my_email = request.POST.get("email")
        user = Custom_User.objects.get(email = my_email)
        otp = random.randint(111111,999999)
        user.otp_token = otp
        user.save()
          
        sub = f""" Your Otp : {otp}"""
        msg = f""" Your OTP is {otp}, keep is secret"""
        from_mail = EMAIL_HOST_USER
        receipent = [my_email]
        
        send_mail(
            subject = sub,
            recipient_list = receipent,
            from_email = from_mail,
            message = msg,
        )
        return redirect('update_pass')
    return render(request, "forgetpassword.html")


def update_pass(request):
    if request.method == "POST":
        mail = request.POST.get('email')
        otp = request.POST.get('otp')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        
        user = Custom_User.objects.get(email = mail)
        
        if user.otp_token != otp:
            return redirect("forget_pass")
        
        elif password != c_password:
            return redirect("forget_pass")
        
        else:
            user.set_password(password)
            user.otp_token = None
            user.save()
            return redirect("singIn")
    return render(request, 'updatepassword.html')

  # forget  password code end 

    






def signUp(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect("singIn")
    else:
        form = UserCreateForm()
    return render(request, 'singup.html', {'form':form})


def singIn(request):
    if request.method == "POST":
        form = UserSigninForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username, password)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("homePage")
    else:
        form = UserSigninForm()
    return render(request, 'singin.html', {'form': form})


def signOut(request):
    logout(request)
    return redirect('singIn')




def homePage(request):
    return render(request, 'home.html')


def addTaskCatagoriz(request):
    catagorize = Task_Catagorze.objects.all()
    if request.method == "POST":
        form = TaskCatagorizForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect("addTaskCatagoriz")   
    else:
        form = TaskCatagorizForm()   
    context = {
        'catagorize': catagorize,
        'form': form
    }
    return render(request, 'catagorize.html', context)


def editCatagoriz(request,id):
    Categorize = Task_Catagorze.objects.get(id=id)
    form = TaskCatagorizForm( instance = Categorize)
    if request.method== "POST":
        form = TaskCatagorizForm(request.POST, instance = Categorize)
        if form.is_valid():
            form.save()
            return redirect("addTaskCatagoriz")
    return render(request, 'editcatagoriz.html', {'form':form})


def deleteCatagoriz(request, id):
    Categorize = Task_Catagorze.objects.get(id = id)
    Categorize.delete()
    return redirect("addTaskCatagoriz")





def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewTask")
    else:
        form = TaskForm()
    return render(request, 'addtask.html', {'form': form})


def search(request):
    try:
        search = request.GET.get('search')
        if search:
            result = Task_Model.objects.filter(task_title__icontains = search)
        else:
            result=[]
        context={
            'search': search,
            'result': result,
        }
        return render(request, 'search.html', context)
    except Exception as e:

        return HttpResponse("Exciption Error", {{e}})



def viewTask(request):
    form = TaskPryrotyForm(request.POST or None)
    tasks = Task_Model.objects.all()

    if request.method == "POST":
        if form.is_valid():
            task_priroty = form.cleaned_data.get('task_priroty')
            task_categorize = form.cleaned_data.get('task_categorize')

            if task_priroty and task_categorize:
                tasks = Task_Model.objects.filter(task_priroty=task_priroty, task_categorize=task_categorize)
            elif task_priroty:
                tasks = Task_Model.objects.filter(task_priroty=task_priroty)
            elif task_categorize:
                tasks = Task_Model.objects.filter(task_categorize=task_categorize) 

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'viewtask.html', context)


def todayTask(request):
    # Get today's date
    today_date = date.today()

    # Filter tasks where the task_date is today's date
    today_tasks = Task_Model.objects.filter(task_date__date=today_date)

    return render(request, 'todaytask.html', {'today_tasks': today_tasks})




def editTask(request,id):
    task = Task_Model.objects.get(id=id)
    form = TaskForm( instance = task)
    if request.method== "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect("viewTask")
    return render(request, 'edittask.html', {'form':form})


# def taskStatus(request,id):
#     task_S = Task_Model.objects.get(id = id)
#     if request.method.get == "POST":
#         task_S.task_status = True
#         return redirect("viewTask")



def taskStatus(request, id):
    task = get_object_or_404(Task_Model, pk=id)
    
    task.task_status = True
    
    task.save()
    
    return redirect('viewTask')




def deleteTask(request, id):
    task = Task_Model.objects.get(id = id)
    task.delete()
    return redirect("viewTask")





