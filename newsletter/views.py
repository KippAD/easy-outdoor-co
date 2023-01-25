from django.shortcuts import render, redirect
from django.conf import settings
from .models import MailingList, NewsletterEmail
from django.contrib import messages
from .forms import NewsletterForm
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def newsletter_subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if MailingList.objects.filter(email=email).exists():
            messages.warning(request, 'You have already joined our newsletter!')
        else:
            e = MailingList(name=name, email=email)
            e.save()

            email_subject = 'Newsletter Subscription Confirmation'
            email_content = f"Hi {name}! This is a confirmation email for your recent \
                subscription to the Easy Outdoor Co. newsletter.\
                    Email: {email}"
            html_message = render_to_string('newsletter/email-template.html', {
                'subject': email_subject,
                'content': email_content
                })
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to = settings.EMAIL_TEST_USER
            mail.send_mail(email_subject, plain_message, from_email, [to], html_message=html_message)

            messages.success(request, 'You have joined our newsletter!')

    redirect_url = 'home'
    return redirect(redirect_url)


def newsletter_form(request):
    """
    Displays newsletter form
    """
    form = NewsletterForm()

    context = {
        'form': form,
    }

    return render(request, 'newsletter/newsletter-form.html', context)


def send_newsletter(request):
    """
    Takes newsletter content submitted
    by admin and sends it to all users on
    mailing list
    """
    if request.method == 'POST':
        email_subject = request.POST.get('subject')
        print(email_subject)
        email_content = request.POST.get('message')
        print(email_content)
        html_message = render_to_string('newsletter/email-template.html', {
            'subject': email_subject,
            'content': email_content
            })
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = settings.EMAIL_TEST_USER
        mail.send_mail(email_subject, plain_message, from_email, [to], html_message=html_message)

    messages.success(request, ('Newsletter sent!'))
    return redirect('manage-site')