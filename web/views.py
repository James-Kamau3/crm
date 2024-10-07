from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()
    return render(request, 'web/home.html', {'records': records})
    
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials!")
            return redirect('login')
            
    else:
        return render(request, 'web/login.html', {})  
    
    
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'web/register.html', {'form':form})

	return render(request, 'web/register.html', {'form':form})
    
def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful!")
    return redirect('login')

def customer_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request, 'web/record.html', {'record': record})
    else:
        messages.info(request, "You need to be logged in to view")
        return redirect('login')
        

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_rec = Record.objects.get(id=pk)
        delete_rec.delete()
        messages.success(request, "Successfully Deleted")
        return redirect('home')
    else:
        messages.info("You need to be logged in to perfome a delete")
        return redirect('login')


def add_record(request):
    return render(request, 'web/add_record.html', {})