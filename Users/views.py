from django.shortcuts import render

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView

from django.urls import reverse, reverse_lazy

# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    
    return render(request, 'Users/profile.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)

        print("Hello Wrold!")
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('HashbookApp:index'))
        
        else:
            context = {"message":"Invalid Credentials"}
            return render(request, 'Users/login.html', context)
        
    return render(request, 'Users/login.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("Users:login")
    template_name = "Users/signup.html"


def logout_view(request):
    logout(request)
    
    context = {"message":'Logged Out Successfully!'}
    return render(request,'Users/login.html', context)