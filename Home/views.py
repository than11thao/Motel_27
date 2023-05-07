from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.http import HttpRequest, JsonResponse,HttpResponse
from Room.models import Room
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import *
from User.models import *
from Bill.models import Bill
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
class LoginSite(TemplateView):
    def get(self, request):
        return render(request, 'home/login.html')
    
    def post(self, request):
        if request.is_ajax():
            try:
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                
                if user is None:
                    return JsonResponse({"valid":False, "message":"Tài khoản hoặc mật khẩu không đúng"})
                else:
                    if user.is_owner or hasattr(user, 'renter'):
                        login(request, user)
                        return JsonResponse({"valid":True, 'is_owner':user.is_owner})
                    else:
                        return JsonResponse({"valid":False, "message":"Tài khoản chưa được cấp phép"})
                    
            except:
                return JsonResponse({"valid":False})
        
        return JsonResponse({"valid":"oke"})  

def LogOut(request):
    logout(request)
    return redirect("home:login")


class DashBoardSite(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    login_url= "home:login"

    def test_func(self):
        return self.request.user.is_owner
    
    def get(self, request):
        all_room = Room.objects.all()
        room_rented = Room.objects.filter(status = True).count()
        room_not_rent = Room.objects.filter(status= False).count()
        infor_room = [room_rented,room_not_rent]
        unpaid_bills = Bill.objects.filter(pay_status = False)
        return render(request, 'home/index.html',{'all_room':all_room, 'unpaid_bills':unpaid_bills, 'infor_room':infor_room})
    

def SignupPage(request):
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        # fullname = request.POST.get('fullname')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your passowrd and confrom password are not Same!!!")
        else:
            my_user  = MyUserManager.objects.create_user(username, email,pass1)           
            my_user.save(commit=False)       
                 
            # chuyển đến trang login
            return redirect('home:login')
        # print(uname, email, pass1, pass2)    
    return render(request , 'home/signup.html')

class RenterDashBoardSite(LoginRequiredMixin, TemplateView):
    def get(self, request):
        return render(request, "renter_dashboard/partial/index.html")