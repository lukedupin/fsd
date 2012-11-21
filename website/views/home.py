from django.views.generic import TemplateView
from django.template import Context, loader
from django.http import HttpResponse

class Home(TemplateView):
  template_name = "home/index.dhtml"
