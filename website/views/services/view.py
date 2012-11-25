from django.views.generic import TemplateView
from django.template import Context, loader
from django.http import HttpResponse

class Services(TemplateView):
  template_name = "services/index.dhtml"
