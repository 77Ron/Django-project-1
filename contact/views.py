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
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"Message from {name} ({email}):\m\n{message}"

            send_mail(
                subject = subject,
                message = full_message,
                from_email = settings.EMAIL_HOST_USER, 
                #from_email = settings.DEFAULT_FROM_EMAIL,
                recipient_list = [email],
                fail_silently=False,
                )

            messages.success(request, 'Thank you for contacting us!')

            form = ContactForm()
            

        """if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                f"Message from {cd['name']} ({cd['email']}):\n\n{cd['message']}",
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, "Thank you for contacting us!")
            return redirect('contact')"""
        
    else:
        form = ContactForm()

    return render(request, template_name='contact/contact.html', context={'form': form})

    #return render(request, 'contact/contact.html', {'form': form})
