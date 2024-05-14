from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View

from .models import Donation


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
            'institutions': len(institutions)


        }
        return render(request, 'index.html', context)

class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')

class Login(View):
    def get(self, request):
        return TemplateResponse(request, 'login.html')

class Register(View):
    def get(self, request):
        return render(request, 'register.html')
