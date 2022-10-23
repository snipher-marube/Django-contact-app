from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages

def contact(request):
    if request.method == 'POST':

        template = render_to_string('email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['sniphermarube@gmail.com']
        )

        email.fail_silently = False
        email.send()
        messages.success(request, "Thanks for reaching out!", 'alert alert-success alert-dismissible')
    return render(request, 'contact.html')
