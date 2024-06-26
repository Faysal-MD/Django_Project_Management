# Django_Project_Management

This repository contains the Project Management built using Django and Django REST Framework. The API provides endpoints for user registration, authentication, and managing projects, tasks, and comments.



### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/user_name/Django_Project_Management.git
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

7. Go to the browser and click:
   ```sh
   http://127.0.0.1:8000/admin/

### Postman Collection
To facilitate API testing, a Postman collection and environment are provided in the Postman_API folder.

#### Setting Up Postman
   1. Import the Postman collection and environment:
      - Go to Postman and click on Import.
      - Select the ProjectManagementCollections.postman_collection.json file from the Postman_API_Report folder.
      - Import the ProjectManagementEnv.postman_environment.json file from the same folder.
   
   2. Set the environment:
       - In Postman, select the ProjectManagementEnv environment..
   
   3. Run the requests:
      - Use the provided requests in the collection to interact with the API.
        
#### Running Tests with Newman
   Newman is a command-line tool to run Postman collections.

##### Installation
1. Install Newman:
   ```sh
   npm install -g newman
##### Running Tests
1. Run the collection using Newman:
   ```sh
   newman run Postman_API_Report/ProjectManagementCollections.postman_collection.json -e Postman_API_Report/ProjectManagementEnv.postman_environment.json -r cli,html --reporter-html-export=Postman_API_Report/report.html

This command will execute the collection and generate a report in the Postman_API_Report folder.
   
##### Viewing Reports
1. Open the report:
   - Navigate to the Postman_API_Report folder and open the .html file in a web browser to view the test results.

### Folder Structure
```sh
Django_Project_Management/
├── Project_Management/
│ ├── manage.py
│ ├── Project_app/
│ └── ... (other Django project files)
├── Postman_API/
│ ├── ProjectManagementCollections.postman_collection.json
│ ├── ProjectManagementEnv.postman_environment.json
│ └── report.html
└── README.md

