"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from generator import views

urlpatterns = [
    # Step 1 start with path keyword
    # Step 2 first argument given is default URL (empty)
    # Step 3 third argument is views function from other project (has HTTP response)
    path('', views.home, name='home'),
    # Adding a slash at the end is a preference choice
    path('password/', views.password, name='password'),

    path('about/', views.about, name='about'),
]
