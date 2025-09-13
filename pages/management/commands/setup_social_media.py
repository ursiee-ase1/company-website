"""
Management command to set up default social media links
"""

from django.core.management.base import BaseCommand
from pages.models import SocialMediaLink, CompanyInfo

class Command(BaseCommand):
    help = 'Set up default social media links and company information'

    def handle(self, *args, **options):
        # Create default company info if it doesn't exist
        company_info, created = CompanyInfo.objects.get_or_create(
            defaults={
                'name': 'TechCorp Solutions',
                'tagline': 'Delivering innovative technology solutions for modern businesses.',
                'email': 'info@techcorpsolutions.com',
                'phone': '(555) 123-4567',
                'address': '123 Tech Street\nSan Francisco, CA 94105',
                'website': 'https://techcorpsolutions.com',
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS('Created default company information')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Company information already exists')
            )

        # Default social media links
        default_links = [
            {
                'platform': 'facebook',
                'url': 'https://facebook.com/techcorpsolutions',
                'icon_class': 'bi-facebook',
                'display_order': 1
            },
            {
                'platform': 'twitter',
                'url': 'https://twitter.com/techcorpsol',
                'icon_class': 'bi-twitter',
                'display_order': 2
            },
            {
                'platform': 'linkedin',
                'url': 'https://linkedin.com/company/techcorp-solutions',
                'icon_class': 'bi-linkedin',
                'display_order': 3
            },
            {
                'platform': 'instagram',
                'url': 'https://instagram.com/techcorpsolutions',
                'icon_class': 'bi-instagram',
                'display_order': 4
            },
            {
                'platform': 'youtube',
                'url': 'https://youtube.com/@techcorpsolutions',
                'icon_class': 'bi-youtube',
                'display_order': 5
            },
            {
                'platform': 'email',
                'url': 'mailto:info@techcorpsolutions.com',
                'icon_class': 'bi-envelope',
                'display_order': 6
            },
        ]

        created_count = 0
        for link_data in default_links:
            link, created = SocialMediaLink.objects.get_or_create(
                platform=link_data['platform'],
                defaults=link_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created {link_data["platform"]} link')
                )

        if created_count == 0:
            self.stdout.write(
                self.style.WARNING('All social media links already exist')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f'Created {created_count} social media links')
            )

        self.stdout.write(
            self.style.SUCCESS('Social media setup completed successfully!')
        )
