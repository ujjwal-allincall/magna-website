from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def services(request):
    return render(request, 'website/services.html')

def contact(request):
    return render(request, 'website/contact.html')

def terms(request):
    return render(request, 'website/terms.html')

def privacy(request):
    return render(request, 'website/privacy.html')
