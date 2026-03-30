from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponseForbidden
from .models import Theme

# Create your views here.

def show_main(request):
    theme = None

    if request.user.is_authenticated:
        theme = Theme.objects.filter(user=request.user).first()

    context = {
        'nama_kelompok': 'ac3b',
        'user': request.user,
        'ALLOWED_EMAILS': settings.ALLOWED_EMAILS,
        'theme': theme,
    }
    
    return render(request, 'main.html', context)

# helper function
def is_authorized(user):
    return user.email in settings.ALLOWED_EMAILS

def customize(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/google/login/')
    
    if not is_authorized(request.user):
        return HttpResponseForbidden("You don't have access")

    theme, created = Theme.objects.get_or_create(user=request.user)

    if request.method == "POST":
        color = request.POST.get("color")
        font = request.POST.get("font")

        ALLOWED_FONTS = ["Arial", "Times New Roman", "Courier New", "verdana"]

        if color:
            theme.color = color

        if font in ALLOWED_FONTS:
            theme.font = font

        theme.save()
        return redirect("/")
    
    return render(request, "customize.html", {'theme': theme})