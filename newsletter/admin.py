from django.contrib import admin
from .models import MailingList, NewsletterEmail
from django_summernote.admin import SummernoteModelAdmin


class MailingListAdmin(admin.ModelAdmin):
    model = MailingList

    list_display = ("name", "email", "date_subscribed")


class NewsletterEmailAdmin(SummernoteModelAdmin):
    model = NewsletterEmail
    summernote_fields = ("message")
    list_display = ("date", "subject", "message")


admin.site.register(NewsletterEmail, NewsletterEmailAdmin)
admin.site.register(MailingList, MailingListAdmin)
