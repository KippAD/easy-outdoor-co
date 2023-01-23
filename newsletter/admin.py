from django.contrib import admin
from .models import MailingList, NewsletterEmail


class MailingListAdmin(admin.ModelAdmin):
    model = MailingList

    list_display = ('name', 'email', 'date_subscribed')


class NewsletterEmailAdmin(admin.ModelAdmin):
    model = NewsletterEmail

    list_display = ('date', 'subject', 'message')


admin.site.register(NewsletterEmail, NewsletterEmailAdmin)
admin.site.register(MailingList, MailingListAdmin)