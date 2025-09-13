from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from .models import Contact
import re

class ContactForm(forms.ModelForm):
    # Add honeypot field for spam protection
    website = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
        label=''
    )
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'maxlength': '100',
                'autocomplete': 'name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'maxlength': '254',
                'autocomplete': 'email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Your Message',
                'maxlength': '2000',
                'autocomplete': 'off'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.required:
                field.required = True
    
    def clean_name(self):
        """Validate and sanitize name field"""
        name = self.cleaned_data.get('name', '').strip()
        
        # Check for minimum length
        if len(name) < 2:
            raise ValidationError('Name must be at least 2 characters long.')
        
        # Check for maximum length
        if len(name) > 100:
            raise ValidationError('Name must be less than 100 characters.')
        
        # Remove HTML tags
        name = strip_tags(name)
        
        # Check for valid characters only
        if not re.match(r'^[a-zA-Z\s\-\'\.]+$', name):
            raise ValidationError('Name contains invalid characters.')
        
        return name
    
    def clean_email(self):
        """Validate email field"""
        email = self.cleaned_data.get('email', '').strip().lower()
        
        # Basic email validation (Django's EmailField already does this)
        if len(email) > 254:
            raise ValidationError('Email address is too long.')
        
        return email
    
    def clean_message(self):
        """Validate and sanitize message field"""
        message = self.cleaned_data.get('message', '').strip()
        
        # Check for minimum length
        if len(message) < 10:
            raise ValidationError('Message must be at least 10 characters long.')
        
        # Check for maximum length
        if len(message) > 2000:
            raise ValidationError('Message must be less than 2000 characters.')
        
        # Remove HTML tags
        message = strip_tags(message)
        
        # Check for spam patterns
        spam_patterns = [
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            r'www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            r'\b(?:viagra|cialis|casino|poker|lottery|winner|congratulations)\b',
        ]
        
        for pattern in spam_patterns:
            if re.search(pattern, message, re.IGNORECASE):
                raise ValidationError('Message contains prohibited content.')
        
        return message
    
    def clean_website(self):
        """Honeypot field - should always be empty"""
        website = self.cleaned_data.get('website')
        if website:
            raise ValidationError('Spam detected.')
        return website
    
    def clean(self):
        """Cross-field validation"""
        cleaned_data = super().clean()
        
        # Additional spam detection
        name = cleaned_data.get('name', '')
        message = cleaned_data.get('message', '')
        
        # Check for repeated characters (spam indicator)
        if len(set(name)) < 3 and len(name) > 5:
            raise ValidationError('Invalid name format.')
        
        # Check for excessive repetition in message
        words = message.split()
        if len(words) > 10:
            word_counts = {}
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1
            max_repetition = max(word_counts.values())
            if max_repetition > len(words) * 0.3:  # More than 30% repetition
                raise ValidationError('Message appears to be spam.')
        
        return cleaned_data