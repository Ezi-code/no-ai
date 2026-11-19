from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from .forms import LoginForm

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
			return render(request, "index.html")
		else:
			form = LoginForm()
		return render(request, "login.html", {"form":form})
