from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View

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
    def get(self, request):
        return TemplateResponse(request, 'login.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # if not request.user.is_authenticated:

        pass