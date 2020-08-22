from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


def logoutPage(request):
	logout(request)
	return HttpResponseRedirect('/')