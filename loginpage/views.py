from django.shortcuts import render



def login(request):

    template='loginpage/login.html'
    return render(request, template, {})
