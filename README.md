# Trainer Portal

## Overview

Trainer Portal is a Django-based web application that helps trainers manage student records efficiently. The system provides secure user authentication and allows trainers to perform Create, Read, Update, and Delete (CRUD) operations on student data through a simple and user-friendly interface.

---

## Features

- User Registration and Login
- Secure Authentication System
- Trainer-Specific Dashboard
- Add New Students
- View Student Records
- Update Student Information
- Delete Student Records
- Form Validation
- SQLite Database Integration

---

## Tech Stack

- Python
- Django
- HTML
- CSS
- SQLite

---

## Project Modules

### Authentication Module
- User Signup
- User Signin
- User Signout

### Student Management Module
- Create Student
- Display Students
- Update Student
- Delete Student

---

## Student Information Stored

The application stores the following student details:

- Full Name
- Roll Number
- Email Address
- Contact Number
- Course
- Address
- Assigned Trainer

---

## Project Structure

```text
trainer_portal/
│
├── user_auth_system/
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│
├── students/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   ├── base.html
│   ├── form.html
│
├── manage.py
├── db.sqlite3
└── requirements.txt
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Kiran-sai-99/trainer-portal.git
cd trainer-portal
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install django
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## Screenshots

Add screenshots of:
- Login Page
- Registration Page
- Student Dashboard
- Create Student Form
- Student List Page

---

## Future Enhancements

- Student Search Functionality
- Attendance Tracking System
- Student Performance Analytics
- Course Management Module
- Email Notifications
- Dashboard Reports
- Export Student Data to Excel/PDF

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Django Framework
- Authentication & Authorization
- ModelForms
- CRUD Operations
- URL Routing
- Template Rendering
- Database Management
- MVC/MVT Architecture

---

## Author

**Kiran Sai**

GitHub: https://github.com/Kiran-sai-99

---

## License

This project is developed for learning and educational purposes.

⭐ If you found this project useful, please consider giving it a star.
