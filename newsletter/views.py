from django.shortcuts import render, redirect
from django.conf import settings
from .models import MailingList, NewsletterEmail
from django.contrib import messages


def newsletter_subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if MailingList.objects.filter(email=email).exists():
            messages.warning(request, 'You have already joined our newsletter!')
        else:
            e = MailingList(name=name, email=email)
            e.save()
            messages.success(request, 'You have joined our newsletter!')

    redirect_url = 'home'
    return redirect(redirect_url)
