The Expense Tracker is a full-stack application built using Django (backend) and optionally React (frontend). It allows users to manage expenses, categorize spending, and visualize financial data with modern features such as dark mode, custom login system, and Django admin panel.

This project is designed to be scalable and extendable, with planned integration of AI-powered financial advice, OCR bill scanning, and investment tracking.

Features

Completed
User authentication (login, logout, signup)
Expense CRUD operations
Categories for transactions
Django Admin Panel
REST API endpoints for expenses
Custom frontend with login and dark mode
SQLite database

In Progress / Future
AI-powered budget advisor
OCR bill/invoice scanning (auto expense logging)
Investment tracking (via yFinance API)
Email/SMS parsing for transactions
Task reminders (EMI/bill due dates)
Shared budgets for families

Tech Stack
Backend: Django, Django REST Framework
Frontend: React (or Django templates)
Database: SQLite (default), PostgreSQL (production-ready)
Auth: Django auth system + custom login page
Other planned integrations: OCR, AI, APIs

Project Structure
expense_tracker/
│── backend/
│   ├── expense_tracker/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── core/ (apps will be here)
│   ├── manage.py
│   ├── db.sqlite3
│
│── frontend/ (if using React)
│   ├── package.json
│   ├── src/
│   └── public/
│
│── venv/ (virtual environment)
│── .env
│── requirements.txt


Installation & Setup
1. Clone Repository
git clone <repo-link>
cd expense_tracker

2. Setup Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file inside backend/:

DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///db.sqlite3
OPENAI_API_KEY=your_api_key_here

5. Run Database Migrations
python manage.py migrate

6. Create Superuser (only if needed)
python manage.py createsuperuser

Running the Application
Backend (Django)
python manage.py runserver
Access at: http://127.0.0.1:8000/

Frontend (React)
cd frontend
npm install
npm start
Access at: http://localhost:3000/

Access Points

Django Admin Panel
http://127.0.0.1:8000/admin/
Custom Frontend (Login + Dark Mode)
If React: http://localhost:3000/
If Django templates: http://127.0.0.1:8000/

Django Superuser Credentials
Username: Vanshika
Password: vAnshikA#19
Use these to log in at http://127.0.0.1:8000/admin/


Quick Demo Guide

Start backend:
python manage.py runserver
Open http://127.0.0.1:8000/

Start frontend (if React):
cd frontend
npm start
Open http://localhost:3000/

Login Options:
Django Admin → http://127.0.0.1:8000/admin/ (with credentials above)

Deployment Guide

Localhost (Development)
Run Django backend on port 8000
Run React frontend on port 3000

Production
Use Gunicorn/Uvicorn for Django
Use Nginx as reverse proxy
Use Docker for containerization
Host on Heroku / Render / AWS / DigitalOcean

Future Enhancements
AI-powered financial advisor
OCR for bill scanning
PDF report generation
Multi-user shared budgets
Mobile version (React Native / Flutter)
