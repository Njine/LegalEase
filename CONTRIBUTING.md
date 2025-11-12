# Contributing to LegalEase

Thank you for your interest in contributing to LegalEase! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/LegalEase.git
   cd LegalEase
   ```
3. **Set up your development environment** as described in the README.md
4. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Guidelines

### Code Style

- Follow PEP 8 style guidelines for Python code
- Use meaningful variable and function names
- Write docstrings for all functions, classes, and modules
- Keep lines to a maximum of 127 characters
- Use 4 spaces for indentation (no tabs)

### Django Best Practices

- Use Django's built-in features whenever possible
- Follow Django's naming conventions
- Keep views thin and models fat
- Use Django forms for data validation
- Write tests for new features
- Use Django's template system properly

### Commit Messages

Write clear and descriptive commit messages:

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- First line should be 50 characters or less
- Reference issues and pull requests after the first line

Example:
```
Add user authentication middleware

- Implement JWT token validation
- Add permission checks for admin routes
- Update tests for new middleware

Fixes #123
```

## Making Changes

### Before Starting

1. Check existing issues and pull requests to avoid duplicates
2. For major changes, open an issue first to discuss your proposal
3. Make sure all tests pass before starting your work

### Development Process

1. **Write tests first** (TDD approach recommended)
2. **Implement your changes** following the coding guidelines
3. **Run tests** to ensure nothing is broken:
   ```bash
   python manage.py test
   ```
4. **Check code style** with flake8:
   ```bash
   flake8 .
   ```
5. **Update documentation** if needed
6. **Commit your changes** with clear messages

### Testing

- Write unit tests for all new functionality
- Write integration tests for complex features
- Ensure test coverage doesn't decrease
- Test both success and failure cases
- Mock external dependencies

Example test structure:
```python
from django.test import TestCase

class YourFeatureTestCase(TestCase):
    def setUp(self):
        # Set up test data
        pass
    
    def test_your_feature(self):
        # Test your feature
        self.assertEqual(expected, actual)
```

## Submitting Changes

### Pull Request Process

1. **Update your branch** with the latest changes from main:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Push your changes** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request** on GitHub with:
   - Clear title describing the change
   - Detailed description of what and why
   - Reference to related issues
   - Screenshots for UI changes
   - Test results

4. **Respond to feedback** from reviewers promptly

5. **Update your PR** as requested

### Pull Request Checklist

Before submitting, ensure:

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] No merge conflicts with main branch
- [ ] Commit messages are clear and descriptive
- [ ] Changes are focused and minimal
- [ ] No unnecessary files included (build artifacts, IDE configs, etc.)

## Types of Contributions

### Bug Reports

When reporting bugs, include:
- Clear, descriptive title
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots if applicable
- Environment details (OS, Python version, Django version)

### Feature Requests

When requesting features:
- Explain the problem you're trying to solve
- Describe your proposed solution
- Consider alternative solutions
- Explain why this benefits the project

### Documentation

- Fix typos and clarify existing documentation
- Add missing documentation
- Improve examples
- Translate documentation

### Code Contributions

- Bug fixes
- New features
- Performance improvements
- Code refactoring
- Test improvements

## Development Setup

### Prerequisites

- Python 3.11 or 3.12
- PostgreSQL 12+
- Git
- Virtual environment tool

### Environment Variables

Copy `.env.example` to `.env` and configure:
```bash
cp LegalEase/.env.example LegalEase/.env
```

### Database Setup

```bash
# Create database
createdb legalease

# Run migrations
cd LegalEase
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test case_app

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## Questions?

If you have questions:
- Check existing documentation
- Search closed issues and PRs
- Open a new issue with the "question" label
- Contact the maintainers

## Recognition

Contributors will be recognized in:
- Project README
- Release notes
- GitHub contributors page

Thank you for contributing to LegalEase! 🎉
