from django.shortcuts import render
from django.views.generic import TemplateView

# home view function
def home_page_view(request):
    return render(request, "home.html")

# class-based view for about page
class AboutPageView(TemplateView):
    template_name = "about.html"

def get_context_data(self, **kwargs): # added method to provide additional context
 context = super().get_context_data(**kwargs)
 context["contact_address"] = "123 Main Street"
 context["phone_number"] = "555-555-5555"
 return context