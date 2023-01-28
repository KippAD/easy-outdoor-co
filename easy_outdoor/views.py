from django.shortcuts import render


# https://levelup.gitconnected.com/django-customize-404-error-page-72c6b6277317
def page_not_found_view(request, exception):
    return render(request, "404.html", status=404)


def page_forbidden_found_view(request, exception):
    return render(request, "403.html", status=403)


def server_error_view(request, *args, **argv):
    return render(request, "500.html", status=500)
