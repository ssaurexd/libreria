from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import View
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

from .forms import UserRegisterForm, VerificationForm
from .models import User
from .forms import LoginForm, UpdateUserPasswordForm
from .funtions import code_generator

# Create your views here.
class UserRegisterView(FormView):

	template_name = 'users/register.html'
	form_class = UserRegisterForm
	success_url = '/'

	def form_valid(self, form):
		
		#generamos codigo
		codigo = code_generator()
		usuario = User.objects.create_user(
			form.cleaned_data['username'],
			form.cleaned_data['email'],
			form.cleaned_data['password1'],
			nombre=form.cleaned_data['nombre'],
			apellidos=form.cleaned_data['apellidos'],
			genero=form.cleaned_data['genero'],
			codregistro=codigo
		)		

		#enviar email con el codigo
		asunto = 'Confirmacion de email'
		msj = 'Codigo de confirmacion: ' + codigo
		email_remitente = 'ssaurexd@gmail.com'

		send_mail(asunto, msj, email_remitente, [form.cleaned_data['email'], ])

		return HttpResponseRedirect(
			reverse('users_app:user-verification', kwargs={'pk':usuario.id})
		)

		return super(UserRegisterView, self).form_valid(form)
	
class LoginView(FormView):

	template_name = 'users/login.html'
	form_class = LoginForm
	success_url = reverse_lazy('home_app:panel')

	def form_valid(self, form):

		user = authenticate(
			username = form.cleaned_data['username'],
			password = form.cleaned_data['password']
		)

		login(self.request, user)

		return super(LoginView, self).form_valid(form)


class LogoutView(View):

	def get(self, request, *args, **kargs):
		
		logout(request)

		return HttpResponseRedirect(
			reverse('users_app:user-login')
		)


class UpdateUserPassword(LoginRequiredMixin, FormView):

	template_name = 'users/update.html'
	form_class = UpdateUserPasswordForm
	success_url = reverse_lazy('users_app:user-login')
	login_url = reverse_lazy('users_app:user-login')

	def form_valid(self, form):

		usuario  = self.request.user
		user = authenticate(
			username = usuario.username,
			password = form.cleaned_data['password1']
		)

		if user:
			new_password = form.cleaned_data['password2']
			usuario.set_password(new_password)
			usuario.save()

		
		logout(self.request)

		return super(UpdateUserPassword, self).form_valid(form)


class VerificationView(FormView):

	template_name = 'users/verification.html'
	form_class = VerificationForm
	success_url = reverse_lazy('home_app:panel')

	def form_valid(self, form):

		id_user = self.kwargs['pk']
		User.objects.filter(
			id=id_user
		).update(
			is_active=True
		)
		
		return super(VerificationView, self).form_valid(form)