# Personal Document Management API

The Personal Document Management API is a RESTful web service that allows users to upload, manage, and share their personal documents in various formats. Built using Django and Django Rest Framework, this API provides a secure and convenient way to handle document-related tasks.

## Features

- User Registration and Authentication
- Role-Based Access Control
- Document Upload and Conversion (docx to pdf)
- Document Download and Sharing
- Document Management (Update and Delete)
- Document Search
- API Documentation using Swagger UI

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python (3.7 or higher)
- Pipenv (recommended for virtual environment management)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/al-jaber-nishad/document_management.git
   cd document_management
   ```

2. Install project dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Run database migrations:

   ```
   python manage.py migrate
   ```

6. Create a superuser for admin access:

   ```
   python manage.py createsuperuser
   ```
   or use
   ```
    username: nishad
    password: password
   ```

8. Start the development server:

   ```
   python manage.py runserver
   ```

### Usage

- Access the API at: `http://localhost:8000/`
- Admin Panel: `http://localhost:8000/admin/`
- API Documentation (Swagger): `http://127.0.0.1:8000/schema/swagger-ui/`

### Authentication

- Token-based authentication is used. Include the token in the request headers as: `Authorization: Token <your_token>`
