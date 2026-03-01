from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def secure_view(request):
    if not request.user.is_superuser:
        return render(request, "403.html", status=403)
    return render(request, "login.html")


def custom_page_not_found(request, exception):
    return render(request, "404.html", status=404)
