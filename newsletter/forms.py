from django import forms
from .models import NewsletterEmail, MailingList


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterEmail
        fields = ['subject', 'message']