# Django_Project_Management

This repository contains the Project Management built using Django and Django REST Framework. The API provides endpoints for user registration, authentication, and managing projects, tasks, and comments.

### Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/Faysal-MD/Django_Project_Management.git
   cd Project_Management
2. Create a virtual environment and activate it:

   ```sh
   python3 -m venv venv
   source venv/Scripts/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   pip install django djangorestframework

4. Apply the migrations:
   ```sh
   python manage.py migrate

5. Create a superuser:
   ```sh
   python manage.py createsuperuser

6. Run the development server:
   ```sh
   python manage.py runserver

