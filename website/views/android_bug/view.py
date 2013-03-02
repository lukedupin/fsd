from django.views.generic import TemplateView
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import redirect
from website.models import AndroidBugs

def bug(request):
  AndroidBugs(request.POST).save()
  return redirect('/')
