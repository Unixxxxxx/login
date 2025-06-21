from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseForbidden

def index(request):
    return render(request,'index.html')


def secure_view(request):
    if not request.user.is_superuser:
        return render(request, '403.html', status=403)
    return render(request, 'login.html')