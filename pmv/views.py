# Shawn Jain
# 8/20/2013
# PriceMyVet

# imports
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from django.template import RequestContext
# import for email validation
from django import forms
from django.utils import simplejson

from pmv.models import *

def test(request):
	return HttpResponse("Test Page!!")

def home(request):
	return render(request, "home.html", {"name": "PMV homepage"})

def submit(request):
	return HttpResponse(request.POST)