# CodeAlpha Job Board Platform

A backend Job Board Platform built with Django and Django REST Framework as part of the CodeAlpha Backend Development Internship.

## Overview

This project provides a RESTful backend for a job board platform where employers can post and manage jobs, candidates can search and apply for jobs, resumes can be uploaded, and application statuses can be tracked.

The platform also includes a notification system for application events and a Django Admin panel for managing platform data.

## Features

- Employer and candidate profiles
- Job posting and management
- Job search and filtering
- Job type filtering
- Resume upload
- Job applications
- Application tracking
- Application status updates
- Candidate notifications when application status changes
- Employer notifications when candidates apply
- Django REST Framework API
- Django Admin panel
- SQLite database
- Media file handling for uploaded resumes

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Django REST Framework Browsable API
- Git & GitHub

## Project Structure

```text
CodeAlpha_JobBoard/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── migrations/
│
├── jobs/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── applications/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── notifications/
│   ├── models.py
│   ├── admin.py
│   └── migrations/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md
└── LICENSE
```

## API Endpoints

### Jobs

| Method | Endpoint          | Description            |
| ------ | ----------------- | ---------------------- |
| GET    | `/api/jobs/`      | List all jobs          |
| POST   | `/api/jobs/`      | Create a job           |
| GET    | `/api/jobs/<id>/` | Retrieve a job         |
| PUT    | `/api/jobs/<id>/` | Update a job           |
| PATCH  | `/api/jobs/<id>/` | Partially update a job |
| DELETE | `/api/jobs/<id>/` | Delete a job           |

### Job Search and Filtering

Jobs can be filtered using query parameters:

```text
/api/jobs/?location=Remote
/api/jobs/?job_type=internship
/api/jobs/?location=Remote&job_type=internship
```

### Applications

| Method | Endpoint                  | Description               |
| ------ | ------------------------- | ------------------------- |
| GET    | `/api/applications/`      | List applications         |
| POST   | `/api/applications/`      | Submit an application     |
| GET    | `/api/applications/<id>/` | Retrieve an application   |
| PUT    | `/api/applications/<id>/` | Update an application     |
| PATCH  | `/api/applications/<id>/` | Update application status |
| DELETE | `/api/applications/<id>/` | Delete an application     |

Application filtering is also supported:

```text
/api/applications/?candidate=1
/api/applications/?job=1
/api/applications/?status=shortlisted
```

## Application Workflow

```text
Candidate
    |
    v
Search Jobs
    |
    v
Select Job
    |
    v
Upload Resume
    |
    v
Submit Application
    |
    v
Application Status: Applied
    |
    v
Employer Reviews Application
    |
    +----> Reviewing
    |
    +----> Shortlisted
    |
    +----> Rejected
    |
    +----> Accepted
```

## Notifications

The notification system handles application-related events.

### Employer Notification

When a candidate applies for a job, the employer receives a notification:

```text
New application received for '<job title>'.
```

### Candidate Notification

When an application's status changes, the candidate receives a notification:

```text
Your application for '<job title>' has been updated to '<status>'.
```

## Resume Uploads

Candidates can upload resumes while submitting applications.

Uploaded resumes are stored under:

```text
media/resumes/
```

Media files are excluded from version control.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/rameenali03/CodeAlpha_JobBoard.git
cd CodeAlpha_JobBoard
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Apply migrations

```powershell
python manage.py migrate
```

### 6. Run the development server

```powershell
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## Admin Panel

Create a superuser:

```powershell
python manage.py createsuperuser
```

Then open:

```text
http://127.0.0.1:8000/admin/
```

The admin panel can be used to manage:

* Users
* Candidate profiles
* Employer profiles
* Jobs
* Applications
* Notifications

## Testing

Django system checks can be run using:

```powershell
python manage.py check
```

The project has been manually tested for:

* Job creation and retrieval
* Job filtering
* Application submission
* Resume upload
* Application status updates
* Employer notifications
* Candidate notifications

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

Rameen Ali

Developed as part of the CodeAlpha Backend Development Internship.

