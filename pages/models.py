from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    
    class Meta:
        ordering = ['-sent_at']

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Bootstrap icon class")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-is_featured', 'title']

class SocialMediaLink(models.Model):
    """Model for managing social media links"""
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('github', 'GitHub'),
        ('tiktok', 'TikTok'),
        ('pinterest', 'Pinterest'),
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('website', 'Website'),
    ]
    
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, unique=True)
    url = models.URLField(validators=[URLValidator()])
    icon_class = models.CharField(max_length=50, help_text="Bootstrap icon class (e.g., bi-facebook)")
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0, help_text="Order of display (0 = first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.get_platform_display()} - {self.url}"
    
    class Meta:
        ordering = ['display_order', 'platform']
        verbose_name = "Social Media Link"
        verbose_name_plural = "Social Media Links"

class CompanyInfo(models.Model):
    """Model for storing company information"""
    name = models.CharField(max_length=100, default="TechCorp Solutions")
    tagline = models.CharField(max_length=200, default="Delivering innovative technology solutions for modern businesses.")
    email = models.EmailField(default="info@techcorpsolutions.com")
    phone = models.CharField(max_length=20, default="(555) 123-4567")
    address = models.TextField(default="123 Tech Street\nSan Francisco, CA 94105")
    website = models.URLField(default="https://techcorpsolutions.com")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"