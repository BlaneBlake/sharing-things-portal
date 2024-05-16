from audioop import reverse

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import View

# from .forms import RegisterForm
from .models import Donation, Institution


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


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')


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
            return render(self.request, self.template_name, {'error_message': 'błąd logowania!'})



class Register(View):
    template_name = 'register.html'

    def get(self, request):
        # form = RegisterForm()
        return render(request, self.template_name) #, {'form': form})

    def post(self, request):
        # form = RegisterForm(request.POST
        # if form.is_valid():
        #     user = User.objects.create_user(form.cleaned_data['e-mail'], form.cleaned_data['e-mail'], form.cleaned_data['password'])
        #     # procesowanie danych
        #     return HttpResponse('User already exist!!@!')
        # else:
        #     return HttpResponse('Form is invalid!!!')

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