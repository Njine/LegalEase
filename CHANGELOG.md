# Changelog

All notable changes to the LegalEase project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub Actions CI/CD pipeline for automated testing and linting
- Comprehensive `.gitignore` file for Python/Django projects
- Environment-based configuration using `python-dotenv`
- `.env.example` file for easy setup
- Pre-commit hooks configuration
- Development requirements file (`requirements-dev.txt`)
- Contributing guidelines (CONTRIBUTING.md)
- This CHANGELOG file

### Changed
- **BREAKING**: Updated Django from 5.0.2 to 5.1.14 (includes security patches)
- Updated Python support from 3.10 to 3.11/3.12
- Updated all dependencies to latest versions:
  - gunicorn: 21.2.0 → 23.0.0
  - whitenoise: 6.0.0 → 6.8.2
  - psycopg2 → psycopg2-binary 2.9.10
  - sqlparse: 0.4.4 → 0.5.3
  - typing-extensions: 4.10.0 → 4.12.2
  - packaging: 24.0 → 24.2
  - dj-database-url: 2.1.0 → 2.2.0
- Fixed `requirements.txt` format from Pipfile syntax to standard pip format
- Updated Pipfile to use Python 3.12
- Moved hardcoded secrets to environment variables in settings.py
- Comprehensive README update with modern setup instructions
- Updated copyright year to 2024-2025

### Fixed
- Removed non-existent `report_builder` app from INSTALLED_APPS
- Security: SECRET_KEY now loaded from environment variables
- Security: Database credentials now loaded from environment variables
- Security: Updated Django to patch multiple SQL injection vulnerabilities

### Security
- **CRITICAL**: Fixed SQL injection vulnerabilities by updating Django to 5.1.14
- **HIGH**: Moved SECRET_KEY to environment variables (was hardcoded)
- **MEDIUM**: Moved database credentials to environment variables
- Added security scanning to CI/CD pipeline

## [1.0.0] - 2024-04-17

### Added
- Initial implementation of law firm management system
- User authentication system with role-based access
- Client management module
- Case management module
- Document management system
- Invoice generation functionality
- Calendar integration
- Task management system
- Reporting capabilities
- Collaboration features
- Security features
- Contact management
- Error logging system
- Database management utilities

### Technical Stack
- Django 5.0.2
- Python 3.10
- PostgreSQL database
- Bootstrap for frontend
- jQuery for client-side interactivity

---

## Project Status

**November 2025**: Project revived and modernized after 1.5 years of inactivity  
**April 2024**: Initial development and last commit before hiatus  

## Version History Legend

- `Added` for new features
- `Changed` for changes in existing functionality
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` for vulnerability fixes

[Unreleased]: https://github.com/Njine/LegalEase/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/Njine/LegalEase/releases/tag/v1.0.0
