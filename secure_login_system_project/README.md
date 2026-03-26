# Secure Login System

A full-stack Django project that demonstrates a **secure user authentication and authorization system** using **Python, Django, HTML, CSS, Bootstrap, JavaScript, and SQLite/MySQL**.

## Features

- User registration
- User login and logout
- Secure authentication and authorization using Django
- Password hashing with Django's built-in user model
- Session management
- CSRF protection in all forms
- Input validation for username, email, and password
- Password strength validation
- Protected dashboard page after login
- Friendly success and error messages
- Responsive frontend using Bootstrap

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite (default), MySQL supported

## Folder Structure

```bash
secure_login_system_project/
│── accounts/
│   ├── templates/accounts/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│── secure_login_system/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│── static/
│   ├── css/style.css
│   └── js/script.js
│── templates/
│   └── base.html
│── .env.example
│── manage.py
│── README.md
│── requirements.txt
```

## Setup Instructions

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Start development server

```bash
python manage.py runserver
```

### 7. Open in browser

```bash
http://127.0.0.1:8000/
```

## MySQL Configuration

By default, the project uses SQLite.

To switch to MySQL:
1. Install MySQL server.
2. Create a MySQL database.
3. Update environment variables based on `.env.example`.
4. Set:

```bash
DB_ENGINE=mysql
```

Then run:

```bash
python manage.py migrate
```

## Security Implementations

- Passwords are securely hashed by Django.
- Session cookies are HTTPOnly.
- CSRF protection is enabled.
- Protected pages require login.
- Strong password validation is enabled.
- Form input is validated on both frontend and backend.

## Resume Project Description

Built a Secure Login System using Django with secure authentication and authorization, implementing password hashing, session management, CSRF protection, and input validation.

## Resume Feature Points

- Developed a secure authentication system using Python and Django.
- Implemented user registration, login, logout, and protected dashboard access.
- Applied password hashing, session management, CSRF protection, and validation.
- Built a responsive frontend using HTML, CSS, Bootstrap, and JavaScript.
- Configured SQLite by default with optional MySQL support.

## GitHub Description

A Django-based Secure Login System with authentication, authorization, password hashing, CSRF protection, session management, and responsive UI.
