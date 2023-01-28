from django import forms
from .models import NewsletterEmail, MailingList
from django_summernote.widgets import SummernoteWidget


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterEmail
        fields = ["subject", "message"]

        widgets = {
                "subject": forms.TextInput(
                    attrs={"placeholder": "Newsletter Subject *"}),
                "message": SummernoteWidget(
                    attrs={"placeholder": "Newsletter message *"}),
            }
