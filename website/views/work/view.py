from django.views.generic import TemplateView
from django.template import Context, loader
from django.http import HttpResponse

class Work(TemplateView):
  template_name = "work/index.dhtml"
