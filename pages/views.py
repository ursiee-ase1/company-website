from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.cache import cache
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.utils import timezone
from .models import Service, Contact
from .forms import ContactForm
import time

def home(request):
    """Home page view"""
    featured_services = Service.objects.filter(is_featured=True)[:3]
    context = {
        'featured_services': featured_services,
        'page_title': 'Home'
    }
    return render(request, 'home.html', context)

def about(request):
    """About page view"""
    context = {
        'page_title': 'About Us'
    }
    return render(request, 'about.html', context)

def services(request):
    """Services page view"""
    all_services = Service.objects.all()
    context = {
        'services': all_services,
        'page_title': 'Our Services'
    }
    return render(request, 'services.html', context)

@csrf_protect
@never_cache
def contact(request):
    """Contact page view with form handling and rate limiting"""
    
    # Rate limiting: 5 submissions per IP per hour
    client_ip = request.META.get('REMOTE_ADDR', 'unknown')
    cache_key = f"contact_rate_limit_{client_ip}"
    submission_count = cache.get(cache_key, 0)
    
    if submission_count >= 5:
        messages.error(request, 'Too many submissions. Please try again later.')
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Additional security: Check for duplicate submissions
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Check if similar message was submitted recently
            recent_submissions = Contact.objects.filter(
                email=email,
                sent_at__gte=timezone.now() - timezone.timedelta(minutes=30)
            ).count()
            
            if recent_submissions > 0:
                messages.error(request, 'A similar message was recently submitted. Please wait before submitting again.')
            else:
                form.save()
                messages.success(request, 'Thank you! Your message has been sent successfully.')
                
                # Increment rate limit counter
                cache.set(cache_key, submission_count + 1, 3600)  # 1 hour
                
                return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'page_title': 'Contact Us'
    }
    return render(request, 'contact.html', context)