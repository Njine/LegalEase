# LegalEase - Law Firm Management System

[![Django CI](https://github.com/Njine/LegalEase/workflows/Django%20CI/badge.svg)](https://github.com/Njine/LegalEase/actions)
![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)
![Django Version](https://img.shields.io/badge/django-5.1.14-green)

## Project Status

**Last Updated:** November 2025  
**Status:** 🚀 Active Development (Revived from hiatus)

After a period of inactivity since April 2024, this project has been modernized with:
- ✅ Updated to Django 5.1.14 (latest security patches)
- ✅ Python 3.12 support
- ✅ Security improvements (environment-based configuration)
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Modern dependency management

## Overview

LegalEase is a comprehensive web-based application designed to streamline the operations of a law firm. It provides tools for managing clients, cases, documents, invoices, and user authentication.

## Features

- **User Authentication:** Secure login and authentication system for different user roles (partners, associates, clerks, secretary).
- **Client Management:** Create, view, update, and delete client records with associated contact information and legal representation details.
- **Case Management:** Record case details including title, description, court level, assigned lawyer, and scheduling information.
- **Document Management:** Upload, view, and manage documents associated with specific cases.
- **Invoice Generation:** Automatically generate invoices for billable services, with options for various billing methods and payment tracking.
- **Calendar Integration:** Integration with a calendar system to schedule appointments, court dates, and deadlines.
- **Task Management:** Assign tasks to users, track task progress, and set reminders for important deadlines.
- **Reporting:** Generate reports on various metrics such as case workload, billing summaries, and client demographics.

## Technologies Used

- **Python 3.11/3.12:** Modern Python for backend development
- **Django 5.1.14:** Latest stable Django framework with security patches
- **PostgreSQL:** Robust database management system
- **HTML/CSS/JavaScript:** Frontend interface design and interactivity
- **Django Templates:** Server-side rendering
- **Gunicorn:** Production-ready WSGI server
- **WhiteNoise:** Static file serving

## Prerequisites

- Python 3.11 or 3.12
- PostgreSQL 12+ 
- pip (Python package manager)
- Virtual environment tool (venv or virtualenv)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Njine/LegalEase.git
cd LegalEase/LegalEase
```

### 2. Set up virtual environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example environment file and update with your settings:

```bash
cp .env.example .env
```

Edit `.env` and set your configuration:
- `SECRET_KEY`: Generate a secure secret key for Django
- `DEBUG`: Set to `False` in production
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`: Your PostgreSQL credentials

### 5. Set up the database

```bash
# Create PostgreSQL database
createdb legalease

# Run migrations
python manage.py migrate
```

### 6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Access the application at http://localhost:8000

## Development

### Running Tests

```bash
python manage.py test
```

### Linting

```bash
flake8 .
```

### Creating Migrations

```bash
python manage.py makemigrations
```

## Deployment

For production deployment:

1. Set `DEBUG=False` in your `.env` file
2. Configure `ALLOWED_HOSTS` with your domain
3. Use a production-ready database
4. Collect static files: `python manage.py collectstatic`
5. Use Gunicorn or similar WSGI server
6. Set up reverse proxy (Nginx/Apache)
7. Enable HTTPS

## Project Structure

```
LegalEase/
├── LegalEase/          # Main project settings
├── authentication_manager/
├── case_app/
├── client_app/
├── document_app/
├── invoice_app/
├── task_app/
├── calendar_app/
├── collaboration_app/
├── contact_app/
├── reporting_app/
├── security_app/
├── user_app/
├── error_logger/
├── database_manager/
└── manage.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security

- Never commit `.env` files or expose sensitive credentials
- Use environment variables for all sensitive configuration
- Keep dependencies updated regularly
- Follow Django security best practices

## Changelog

### November 2025 - Project Revival
- Updated Django from 5.0.2 to 5.1.14 (security patches)
- Updated Python support to 3.11/3.12
- Added environment-based configuration
- Implemented CI/CD with GitHub Actions
- Added comprehensive .gitignore
- Updated all dependencies to latest versions
- Improved security practices

### April 2024
- Initial development phase
- Core features implemented

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Brian Njine**
- [LinkedIn](https://www.linkedin.com/in/brian-njine-aa730684/)
- [GitHub](https://github.com/njine)
- [Twitter](https://twitter.com/BrainNjyn)

---

*Part of the Holberton School portfolio project*

