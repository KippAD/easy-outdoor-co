from django.db import models


class MailingList(models.Model):
    """ List of emails that recieve promotional emails from site """
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class NewsletterEmail(models.Model):
    """Stores and sends out newsletters composed by the admin"""
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.subject
