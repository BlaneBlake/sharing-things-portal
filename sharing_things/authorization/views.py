from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.


class Test(View):
    def get(self, request):
        return HttpResponse('test działania')

class LoginView(View):
    def get(self, request):
        return HttpResponse('logowanie')

# HomePage with Login required mixin (zezwala na dostęp tylko zalogowanego użytkownika)
class HomePageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home_page.html')