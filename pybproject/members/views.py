from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
# Create your views here.



# def index(request):
#     return render(request, 'index.html', { 'email' : request.session.get('user')})

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    # success_url = '/'

    success_url = reverse_lazy('basedbboard') 
    def form_valid(self, form):
        # email = form.cleaned_data.get("email")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        # self.request.session['user'] = form.user_id

        if user is None:
            return redirect(reverse("customlogin"))
        login(self.request, user)
        return super().form_valid(form)



def log_out(request):
    logout(request)
    return redirect(reverse("home"))









