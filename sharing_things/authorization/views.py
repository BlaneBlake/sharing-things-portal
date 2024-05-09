from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


# Create your views here.

class Test(View):
    pass


# HomePage with Login required mixin (zezwala na dostęp tylko zalogowanego użytkownika)
class HomePageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home_page.html')