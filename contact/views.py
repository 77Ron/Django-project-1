# contact/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'New Contact Form Submission'
            message = f"""
            From: {form.cleaned_data['name']} <{form.cleaned_data['email']}>
            
            Message:
            {form.cleaned_data['message']}
            """
            from_email = form.cleaned_data['email']
            recipient_list = [settings.EMAIL_HOST_USER]
            #fail_silently = False
            auth_password = [settings.EMAIL_HOST_PASSWORD]
            
            send_mail(subject, message, from_email, recipient_list, auth_password)
            
            messages.success(request, 'Thank you for contacting us!')
            
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, template_name='contact/contact.html', context={'form': form})
