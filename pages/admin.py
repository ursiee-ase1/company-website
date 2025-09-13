from django.contrib import admin
from .models import Contact, Service, SocialMediaLink, CompanyInfo

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'sent_at']
    list_filter = ['sent_at']
    search_fields = ['name', 'email']
    readonly_fields = ['sent_at']
    ordering = ['-sent_at']
    
    def has_add_permission(self, request):
        return False  # Disable adding contacts through admin

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'created_at']
    list_filter = ['is_featured', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_featured']
    ordering = ['-is_featured', 'title']

@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'is_active', 'display_order']
    list_filter = ['is_active', 'platform']
    list_editable = ['is_active', 'display_order']
    search_fields = ['platform', 'url']
    ordering = ['display_order', 'platform']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('platform', 'url', 'icon_class')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'display_order')
        }),
    )

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'updated_at']
    search_fields = ['name', 'email']
    
    def has_add_permission(self, request):
        # Only allow one company info record
        return not CompanyInfo.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of company info
        return False