from django.urls import path

from .views import home, about, services, contact

urlpatterns = [
    path("", home, name="home"),  # Home page URL
    path("about/", about, name="about"),  # About page URL
    path("services/", services, name="services"),  # Services page URL
    path("contact/", contact, name="contact"),  # Contact page URL
]