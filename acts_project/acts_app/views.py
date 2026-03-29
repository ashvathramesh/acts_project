from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.template import loader


def home(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def peoples(request):
    template = loader.get_template("people.html")
    return HttpResponse(template.render())

def places(request):
    template = loader.get_template("places.html")
    return HttpResponse(template.render())

def time(request):
    template = loader.get_template("time.html")
    return HttpResponse(template.render())

def events(request):
    template = loader.get_template("events.html")
    return HttpResponse(template.render())

def miscellaneous(request):
    template = loader.get_template("miscellaneous.html")
    return HttpResponse(template.render())

def jokes(request):
    template = loader.get_template("jokes.html")
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())



