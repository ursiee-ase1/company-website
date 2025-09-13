# TechCorp Solutions - Django Website

A modern, responsive company website built with Django 5.2.4 featuring dynamic content management, social media integration, and enhanced security features.

## 🚀 Features

### Core Functionality
- **Responsive Design**: Mobile-first Bootstrap 5.3.0 design
- **Dynamic Content**: Database-driven pages and content management
- **Admin Interface**: Full Django admin for easy content management
- **Contact Form**: Enhanced form with validation and spam protection
- **Social Media Integration**: Dynamic social media links and sharing

### Security Features
- **CSRF Protection**: Built-in Django CSRF middleware
- **Input Validation**: Comprehensive form validation and sanitization
- **Rate Limiting**: IP-based rate limiting for contact form
- **Spam Protection**: Honeypot fields and pattern detection
- **XSS Prevention**: HTML tag stripping and proper escaping

### Pages
- **Home**: Hero section with featured services
- **About**: Company information with team profiles
- **Services**: Dynamic service listings
- **Contact**: Interactive contact form with company details

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4
- **Frontend**: Bootstrap 5.3.0, HTML5, CSS3, JavaScript
- **Database**: SQLite3 (development), PostgreSQL (production ready)
- **Icons**: Bootstrap Icons
- **Python**: 3.13.2

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip (Python package installer)
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/techcorp-solutions.git
   cd techcorp-solutions
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Set up default data**
   ```bash
   python manage.py setup_social_media
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the website**
   - Website: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 🔧 Configuration

### Environment Variables (Production)
Create a `.env` file with the following variables:

```env
DJANGO_SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Database Configuration
- **Development**: SQLite3 (default)
- **Production**: PostgreSQL (recommended)

## 📁 Project Structure

```
techcorp-solutions/
├── company_project/          # Django project settings
│   ├── __init__.py
│   ├── settings.py          # Development settings
│   ├── settings_production.py # Production settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py
├── pages/                   # Main Django app
│   ├── management/
│   │   └── commands/
│   │       └── setup_social_media.py
│   ├── migrations/          # Database migrations
│   ├── static/css/         # CSS files
│   ├── admin.py            # Admin configuration
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py            # Form definitions
│   ├── models.py           # Database models
│   ├── security.py         # Security middleware
│   ├── urls.py             # App URL configuration
│   └── views.py            # View functions
├── templates/              # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── services.html
│   ├── contact.html
│   ├── navbar.html
│   ├── footer.html
│   └── social_share.html
├── static/                 # Static files
├── media/                  # User uploaded files
├── .gitignore
├── README.md
├── requirements.txt
├── requirements_production.txt
└── manage.py
```

## 🎨 Customization

### Adding New Social Media Platforms
1. Go to Django Admin → Social Media Links
2. Add new platform with URL and icon class
3. Icons use Bootstrap Icons (e.g., `bi-github`, `bi-tiktok`)

### Updating Company Information
1. Go to Django Admin → Company Information
2. Update company details, contact information
3. Changes reflect across all pages automatically

### Adding New Services
1. Go to Django Admin → Services
2. Add service with title, description, and icon
3. Mark as "Featured" to show on home page

## 🔒 Security Features

### Form Security
- **CSRF Protection**: All forms protected against CSRF attacks
- **Input Validation**: Server-side validation for all inputs
- **Spam Protection**: Honeypot fields and pattern detection
- **Rate Limiting**: 5 submissions per IP per hour

### Template Security
- **XSS Prevention**: Auto-escaping enabled
- **HTML Sanitization**: User input stripped of HTML tags
- **Safe URLs**: External links use `rel="noopener noreferrer"`

### Production Security
- **Environment Variables**: Sensitive data in environment variables
- **HTTPS Enforcement**: SSL/TLS configuration for production
- **Security Headers**: Comprehensive security headers
- **Database Security**: Parameterized queries prevent SQL injection

## 🚀 Deployment

### Production Checklist
1. Set `DEBUG = False` in settings
2. Configure `ALLOWED_HOSTS`
3. Set up PostgreSQL database
4. Configure email backend
5. Set up static file serving
6. Configure HTTPS/SSL
7. Set up monitoring and logging

### Recommended Hosting
- **Heroku**: Easy deployment with PostgreSQL
- **DigitalOcean**: VPS with full control
- **AWS**: Scalable cloud hosting
- **PythonAnywhere**: Django-optimized hosting

## 📝 Management Commands

### Setup Social Media
```bash
python manage.py setup_social_media
```
Sets up default social media links and company information.

### Database Operations
```bash
python manage.py makemigrations    # Create migrations
python manage.py migrate          # Apply migrations
python manage.py collectstatic    # Collect static files
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support, email info@techcorpsolutions.com or create an issue in this repository.

## 🙏 Acknowledgments

- Django Framework
- Bootstrap for UI components
- Bootstrap Icons for icons
- All contributors and testers

---

**TechCorp Solutions** - Delivering innovative technology solutions for modern businesses.
