from django.shortcuts import render,redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import HOTEL,fam,ruk

# @login_required(login_url='login')
def home(request):
    hotels =HOTEL.objects.all()
    fams = fam.objects.all()
    return render(request, 'app/home.html',
                  {'hotels': hotels,
                   "fams":fams})

   
def taa(request):
    famr = ruk.objects.all()
    return render(request,'app/taa.html',{'famr':famr})



# def sign_up(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('username')
#         password = request.POST.get('password')

        
#         if User.objects.filter(username=user_name).exists():
#             messages.error(request, "User already exists")
#             return redirect('signup')   

#         user = User.objects.create_user(username=user_name, password=password)
#         user.save()

#         messages.success(request, "Account created successfully")
#         login(request, user)

#         # return redirect('home')
#         return redirect('home')

#     return render(request, "app/signup.html")

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')  # change to your homepage
#         else:
#             messages.error(request, "Invalid username or password")
#             return redirect('login')

#     return render(request, 'app/login.html')

def front(request):
        
    
        return render(request,"app/front.html")

def taa (request):
    return render(request,"app/taa.html")

      








