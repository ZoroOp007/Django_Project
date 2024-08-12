from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, AddUpdateForm, AddRecordForm

from django.contrib.auth import authenticate

from django.contrib import auth

from django.contrib.auth.decorators import login_required

from .models import Record

from django.contrib import messages

# Create your views here.

# -- HomePage
def home(request):
    return render(request, 'webapp/index.html')


# -- Register a User

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully !")

            return redirect('mylogin')
        else:

            messages.error(request, "Account creation failed !")
            context = {
                #'msg1' : "Seems like Invalid Data is filled during registeration ",
                #'msg2' : "Please follow the guidelines of input field",
                'form' : form,
            }
            return render(request, 'webapp/register.html',context)
        

    return render(request,'webapp/register.html' ,{'form' : form})

# Login a User ()

def mylogin(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data= request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request,user)

                messages.success(request,"Logged In Successfully !")

                return redirect('dashboard')

            

    return render(request, 'webapp/my-login.html',{'form' : form})


# dashboard 
@login_required(login_url = 'mylogin')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records' : my_records}

    return render(request,'webapp/dashboard.html',context=context)


# -- Create a record 

@login_required(login_url = 'mylogin')
def createrecord(request):
    form = AddRecordForm()

    if request.method == 'POST':

        form = AddRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request,"New Record Created Successfully !")

            return redirect("dashboard")
        
        
    context = {'form' : form }

    return render(request,'webapp/create-record.html',context=context)




# -- Update a record

@login_required(login_url = 'mylogin')
def updaterecord(request ,pk):
    
    record = Record.objects.get( id = pk)

    form = AddUpdateForm(instance=record)

    if request.method == "POST":
        form = AddUpdateForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request,"Record Updated Successfully !")

            return redirect("dashboard")
    
    context = {'form' : form}

    return render(request, 'webapp/update-record.html', context=context)


# Read / View a Singular Record
@login_required(login_url='mylogin')
def readrecord(request, pk):

    all_record = Record.objects.get( id = pk)

    context = {'record' : all_record}
    return render(request, 'webapp/view-record.html',context =context)


# -- Delete a record
@login_required(login_url='mylogin')
def deleterecord(request, pk):

    record = Record.objects.get(id = pk)

    record.delete()

    messages.success(request,"One Record Deleted !")

    return redirect('dashboard')




# User Logout 
def userlogout(request):
    
    auth.logout(request)

    messages.success(request,"You have been Logged Out !")

    return redirect('mylogin')







