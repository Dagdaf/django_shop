from django.shortcuts import render, redirect, get_object_or_404


def Home(request):
    return render(request, 'shop/home.html')
# Create your views here.
