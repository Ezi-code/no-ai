from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import TemplateView
from django.views import View
from .forms import LoginForm, RegisterForm
from .models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class BaseView(TemplateView):
	template_name="index.html"

class LoginView(View):

	def get(self, request):
		form = LoginForm()
		return render(request, "login.html", {"form":form})

	def post(self, request):
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.data["email"], password=form.data["password"])
			if not user:
				return HttpResponseNotFound("User does not exist")
			login(request, user)
			return redirect("base:homepage")
		else:
			form = LoginForm()
		return render(request, "login.html", {"form":form})

class RegisterView(View):
	def get(self, request):
		form = RegisterForm()
		return render(request, "signup.html", {"form":form})

	def post(self, request):
		form = RegisterForm(request.POST)
		if form.is_valid():
			if not form.data["password"] == form.data["confirm_password"]:
				return redirect("accounts:signup")

			new_user = User(email=form.data["email"], username=form.data["username"])
			new_user.set_password(form.data["password"])
			new_user.save()
			return redirect("/")
		return render(request, "signup.html", {"form": RegisterForm()})
