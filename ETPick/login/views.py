from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm
from register.models import Recruteur


def login(request):
	form = LoginForm(request.POST or None)
	context = {
		'form': form
	}
	if form.is_valid():
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		recruteur = Recruteur.objects.filter(email=email,password=password)
		if recruteur is not None:
			recruteur = Recruteur.objects.get(email=email,password=password)
			request.session['connecte'] = True
			request.session['nom'] = recruteur.nom
			request.session['prenom'] = recruteur.prenom
			request.session['ville'] = recruteur.ville
			request.session['pays'] = recruteur.pays
			request.session['company'] = recruteur.company
			request.session['aboutMe'] = recruteur.aboutMe
			request.session['emailRec'] = email
			request.session['password'] = password
			return HttpResponseRedirect('/recherche', locals())
		else:
			envoi = False
			messagePass = 'Wrong email or password'
	return render(request, "login/login.html", context=context)