from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout



class UserRegisterView(View):
    def get(self,request):
        form=UserRegistrationForm()
        return render(request,'accounts/Register.html',{'form':form})

    def post(self,request):
        form=UserRegistrationForm()
        if form.is_valid():
            cd= form.cleaned_data
            user.objects.createuser(cd['full_name'],cd['phone_number'],cd['password'])
            messages.success(request,'Register done','success')
            return redirect('home:home')

class UserLoginView(View):
    form_class=UserLoginForm
    template_name='accounts/login.html'
    def get(self,request):
        form= self.form_class
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,full_name=cd['full_name'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success('you logged in','success')
                return redirect('home:home')
            messages.error(request,'user name or password is wrong','warning')
        return render(request,self.template_name,{'form':form})

class UserLogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,'you logged out','success')
        return redirect('home:home')