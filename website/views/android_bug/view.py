from django.views.generic import TemplateView
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import redirect
from website.models import AndroidBug
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage

  #Store a bug
@csrf_exempt
def bug(request):
    #Store my bug data
  obj = AndroidBug()
  obj.package_name = request.POST['package_name']
  obj.package_version = request.POST['package_version']
  obj.stacktrace = request.POST['stacktrace']
  obj.save()

    #Send an email
  email = EmailMessage("Android bug detected: "+ obj.package_name, 
                       obj.package_name +"\n"+
                       obj.package_version +"\n"+
                       obj.stacktrace, 
                       to=['info@fsdllc.us'])
  email.send()

  return redirect('/')
