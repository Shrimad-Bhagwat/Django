from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
# Register
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:    
            if User.objects.filter(username=username).exists():
                print("Username already taken!")
                messages.info(request,'Username already taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("Email already in use")
                messages.info(request,'Email already in use!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                # print('Password Matched!')
                # messages.info(request,'Password Matched!')
                return redirect('login')
        else:
            print('Password Not Matched!')
            messages.info(request,'Password Not Matched!')
            return redirect('register')

    else:
        return render(request,'register.html')
    return redirect('/')


# Login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print("User Logged In")
            return redirect('/')
        else:
            print("Invalid Credentials")
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

# Logout
def logout(request):
    auth.logout(request)
    return redirect('/')