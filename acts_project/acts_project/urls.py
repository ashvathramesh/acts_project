"""
URL configuration for acts_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from acts_app.views import home
from acts_app.views import peoples
from acts_app.views import places
from acts_app.views import time
from acts_app.views import events
from acts_app.views import miscellaneous
from acts_app.views import jokes
from acts_app.views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name="home"),
    path('people/people groups', peoples, name="people_page"),
    path('places', places, name="places_page"),
    path('time periods', time, name="time_page"),
    path('miscellaneous', miscellaneous, name="miscellaneous_page"),
    path('events', events, name="events_page"),
    path('jokes', jokes, name="jokes_page"),
    path('about', about, name="about_page"),
]
