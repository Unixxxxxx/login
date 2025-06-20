import logging
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

# ✅ Define logger
logger = logging.getLogger(__name__)

class BlockAdminForNonSuperusers:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            if not request.user.is_authenticated:
                logger.warning(f"[ADMIN BLOCK] Anonymous user tried to access /admin/ from IP {request.META.get('REMOTE_ADDR')}")
                return redirect('/login/')  # or your custom login route

            if not request.user.is_superuser:
                logger.warning(f"[ADMIN BLOCK] User '{request.user.username}' (ID: {request.user.id}) attempted admin access. IP: {request.META.get('REMOTE_ADDR')}")
                return HttpResponseForbidden("❌ Access Denied: Not a superuser.")

        return self.get_response(request)
