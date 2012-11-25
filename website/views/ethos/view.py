from django.views.generic import TemplateView
from django.template import Context, loader
from django.http import HttpResponse

class Ethos(TemplateView):
  template_name = "ethos/index.dhtml"
