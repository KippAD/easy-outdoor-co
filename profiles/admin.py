from django.contrib import admin
from django.contrib import admin
from .models import UserProfile, ProductReview


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "default_phone_number",
        "default_country",
        "default_postcode",
        "default_town_or_city",
        "default_street_address1",
        "default_street_address2",
        "default_county",
    )


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "product",
        "rating",
        "comment",
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
