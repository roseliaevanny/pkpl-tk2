from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponseForbidden

# Create your views here.

def show_main(request):
    context = {
        'nama_kelompok': 'ac3b',
        'user': request.user,
        'ALLOWED_EMAILS': settings.ALLOWED_EMAILS
    }
    
    return render(request, 'main.html', context)

# helper function
def is_authorized(user):
    return user.email in settings.ALLOWED_EMAILS

def customize(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/google/login')
    
    if not is_authorized(request.user):
        return HttpResponseForbidden("You don't have an access")
    
    return render(request, 'customize.html')