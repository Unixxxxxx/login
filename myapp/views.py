import pandas as pd
import os
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from.models import UserData

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'myapp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'myapp/login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def user(request):
    if request.method == 'POST':
        name = request.POST.get('fname')  # Ensure the name matches the form field
        lname = request.POST.get('lname')
        age = request.POST.get('age')

        # Save data in the database
        # Save data to database using the correct model
        UserData.objects.create(name=name, lname=lname, age=age)

        # Define the file path in the media directory
        file_path = os.path.join(settings.MEDIA_ROOT, "user_data.xlsx")

        # Ensure the media directory exists
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

        # Check if the file exists
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
        else:
            df = pd.DataFrame(columns=["First Name", "Last Name", "Age"])

        # Add new data
        new_data = pd.DataFrame([[name, lname, age]], columns=df.columns)
        df = pd.concat([df, new_data], ignore_index=True)

        # Save to Excel
        df.to_excel(file_path, index=False)


        return redirect('thankyou')  # Ensure the correct URL name is used

    return render(request, 'form.html')

def thankyou(request):
    return render(request, "Thankyou.html")
