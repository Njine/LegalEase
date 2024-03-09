
Law Firm Management System
Overview
The Law Firm Management System is a web-based application designed to streamline the operations of a law firm. It provides tools for managing clients, cases, documents, invoices, and user authentication.
Features
    • User Authentication: Secure login and authentication system for different user roles (partners, associates, clerks, secretary).
    • Client Management: Create, view, update, and delete client records with associated contact information and legal representation details.
    • Case Management: Record case details including title, description, court level, assigned lawyer, and scheduling information.
    • Document Management: Upload, view, and manage documents associated with specific cases.
    • Invoice Generation: Automatically generate invoices for billable services, with options for various billing methods and payment tracking.
Technologies Used
    • Python: Backend development using the Django framework.
    • HTML/CSS/JavaScript: Frontend interface design and interactivity.
    • Django Templates: Rendering dynamic content in HTML pages.
    • PostgreSQL: Database management system for storing application data.
Getting Started
    1. Clone the repository to your local machine.
    2. Install Python (if not already installed) and create a virtual environment.
       Copy code
       python -m venv venv
    3. Activate the virtual environment.
        ◦ On Windows:
          Copy code
          venv\Scripts\activate
        ◦ On macOS/Linux:
          bashCopy code
          source venv/bin/activate
    4. Install project dependencies.
       Copy code
       pip install -r requirements.txt
    5. Apply database migrations.
       Copy code
       python manage.py migrate
    6. Run the development server.
       Copy code
       python manage.py runserver
    7. Access the application at http://localhost:8000 in your web browser.
Contributing
Contributions are welcome! Feel free to submit pull requests or open issues for any bugs or feature requests.
License
This project is licensed under the MIT License - see the LICENSE file for details.
