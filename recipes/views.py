from django.shortcuts import render

# Create your views here.

# HTTP REQUEST <- RESPONSE


def home(request):
    return render(request, 'recipes/home.html')
    # return HTTP Response
