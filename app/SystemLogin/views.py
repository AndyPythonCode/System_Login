from django.shortcuts import render
from django.views import generic
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms
from .decorators import unathenticated_user

@method_decorator(login_required, name='dispatch')
class Home(generic.TemplateView):
    template_name = 'home.html'

@method_decorator(unathenticated_user, name='dispatch')
class LoginView(auth_views.LoginView):
    template_name = 'login.html'

@method_decorator(login_required, name='dispatch')
class LogoutView(auth_views.LogoutView):
    template_name = 'logout.html'

@method_decorator(unathenticated_user, name='dispatch')
class RegisterView(generic.FormView):
    template_name = 'register.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        data = form.data
        form.sign_in(data['email'],data['first_name'],data['last_name'],data['gender'],data['birth_date'],data['password1'])
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'password_change.html'

@method_decorator(login_required, name='dispatch')
class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'password_change_done.html'

class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'password_reset.html'

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'