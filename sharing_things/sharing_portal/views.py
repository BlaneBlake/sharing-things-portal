from audioop import reverse

from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import RedirectView

from .models import Donation, Institution, Category


# Create your views here.

class Test(View):
    def get(self, request):
        return HttpResponse('test działania')


class LandingPage(View):
    def get(self, request):

        donations = Donation.objects.all()
        quantity = 0
        institutions = []

        for donation in donations:
            quantity += donation.quantity
            if donation.institution not in institutions:
                institutions.append(donation.institution)

        context = {
            'quantity': quantity,
            'number_of_institutions': len(institutions),
            'foundations': Institution.objects.filter(type=1),
            'organizations': Institution.objects.filter(type=2),
            'locals': Institution.objects.filter(type=3),

        }
        return render(request, 'index.html', context)


class AddDonation(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
# przekierowanie się nie uruchamia poprawnie po logowaniu

    def get(self, request):

        context = {
            'categories': Category.objects.all(),
            'institutions': Institution.objects.all()
        }
        return render(request, 'form.html', context)


class Login(View):
    template_name = 'login.html'
    success_url = reverse_lazy('landing')

    def get(self, request):
        return TemplateResponse(request, self.template_name)

    def post(self, request):
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            return redirect('landing')
        else:
            return redirect('register')
            # return render(self.request, reverse('register'), {'error_message': 'błąd logowania! brak uzytkownika. '})


class LogoutView(RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class Register(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        username = email = request.POST['email']
        name = request.POST['name']
        surname = request.POST['surname']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            user = User.objects.create_user(username, email, password, first_name=name, last_name=surname)
        else:
            return HttpResponse('password mismatch')

        return redirect('login')


class UserView(View):
    def get(self, request):
        context = {

            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,


        }
        return render(request, 'user-view.html', context)
