from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import RegisterForm
from .models import Recruteur

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid():
			firstName = form.cleaned_data['firstName']
			lastName = form.cleaned_data['lastName']
			city = form.cleaned_data['city']
			country = form.cleaned_data['country']
			email = form.cleaned_data['email']
			aboutYou = form.cleaned_data['aboutYou']
			company = form.cleaned_data['company']
			password = form.cleaned_data['password']
			confirmPassword = form.cleaned_data['confirmPassword']
			if Recruteur.objects.filter(email=email).exists() == False:
				if password and password == confirmPassword:
					obj = Recruteur(nom=lastName, prenom=firstName, ville=city, pays=country, email=email, company=company, aboutMe=aboutYou, password=password)
					obj.save()
					envoi = True
					return HttpResponseRedirect('/')
				else:
					envoi = False
					messagePass = 'You must enter the same password'
					return render(request, 'register/register.html', locals())	
			else:
				envoi = False
				messagePass = 'An account are already exists with the same email'
				return render(request, 'register/register.html', locals())	

	else:
		form = RegisterForm()
		return render(request, 'register/register.html', {'form': form})