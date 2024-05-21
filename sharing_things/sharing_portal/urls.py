"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import (Test, AddDonation, Login, Register, LandingPage, LogoutView, UserView)

urlpatterns = [
    path('test/', Test.as_view(), name='test'),
    path('', LandingPage.as_view(), name='landing'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('add-donation/', AddDonation.as_view(), name='add-donation'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserView.as_view(), name='profile')
    ]
