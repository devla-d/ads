from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
from django.contrib import  messages
from django.contrib.auth  import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

# Create your views here.

def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect



class LoginView(View):
    def get(self, request):
        return render(self.request, 'users/auth/login.html')

    def post(self, request):
        destination = get_redirect_if_exists(self.request)
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(self.request, user)
            if user.is_advertiser:
                direct = '/advertiser/dashboard/'
            else:
                direct = '/taskers/dashboard/'
            data = {'successful':"authenticated","dest": direct}
            return JsonResponse(data)
        else:
            data = {'failed':"Invalid Credentials"}
            return JsonResponse(data)


def register(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            ip = request.META.get("REMOTE_ADDR")
            instance.ip_address = ip
            instance.save()
            messages.success(request, f'Account created !')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/auth/register.html',{"form":form})


def logout_view(request):
    logout(request)
    return redirect('login')