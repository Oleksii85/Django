from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def registration(request):
    return render(request, "registration.html")


def details(request):
    return render(request, "details.html")


def create(request):
    return render(request, "create.html")
