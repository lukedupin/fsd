from django.views.generic import TemplateView
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.shortcuts import render
from django.core.mail import EmailMessage

  #My object
class ContactForm(forms.Form):
  email_address = forms.EmailField(required=False)
  phone_number = forms.CharField(max_length=100,required=False)
  subject = forms.CharField(max_length=100,required=False)
  message = forms.CharField(widget=forms.Textarea,required=False)

class Contact(TemplateView):
  template_get = "contact/index.dhtml"
  template_post = "contact/result.dhtml"

    #Handle get events
  def get(self, request, *args, **kwargs):
    form = ContactForm() # An unbound form
    return render(request, self.template_get, { 'form': form, })

  
    #Handle post events
  def post(self, request, *args, **kwargs):
    form = ContactForm(request.POST)

      #If the info isn't valid, go back
    if not form.is_valid():
      return render(request, self.template_get, { 'form': form, })

      #Send an email to me
    email = EmailMessage(form.data['subject'], 
                         "Phone: "+ form.data['phone_number'] +
                          "\r\nEmail: "+ form.data['email_address'] +
                          "\r\n"+ form.data['message'], 
                         to=['info@fsdllc.us'])
    #email.send()

      #Render a thank you
    return render(request, self.template_post, { 'form': form, })
