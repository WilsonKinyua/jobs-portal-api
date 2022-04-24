# Jobs Portal API

Jobs Portal API is a RESTful API that provides a way to create, update, delete and retrieve jobs. It also provides a way to create and retrieve users.

# Admin Login Credentials 🔑

```json
{
  "username": "john",
  "password": "password"
}
```

# Setup Requirements

    - Git (to clone the repository)
    - Python 3.8
    - Django 3.2
    - Django REST framework 3.13
    - PostgreSQL (to run the database)
    - Postman (to test the API)
    - Heroku cli (if you want to deploy to Heroku)

# Setup Installation

    - Clone the repository
    - Run the following commands in the repository:
        - cd <path_to_project> (if you cloned the repository)
        - virtualenv env (to create a virtual environment)
        - source env/bin/activate (to activate the virtual environment)
        - pip install -r requirements.txt
        - cp .env.example .env
        - python manage.py makemigrations
        - python manage.py migrate
        - python manage.py createsuperuser
        - python manage.py runserver
    - Open Postman to test the API endpoints or use the following link:
        - http://localhost:8000/<the_endpoint>
    - Run the following commands if you want to deploy to Heroku:
        - heroku login
        - heroku create
        - git push heroku master
        - heroku open

# Endpoints

- Root endpoint:
  - [https://jobs-platform.herokuapp.com](https://jobs-platform.herokuapp.com)

> POST

`/user/create/`

- Create a new user

```json
{
  "username": "string",
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "password": "string"
}
```

- Response:

```json
{
  "success": "User created successfully"
}
```

> POST

`/auth/`

- Create a new token

```json
{
  "username": "string",
  "password": "string"
}
```

- Response:

```json
{
  "token": "string"
}
```

`/user/details/`

- Get user details

```json
{
  "token": "string"
}
```

- Response:

```json
{
  "username": "string",
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "is_active": true
}
```

`/user/{id}/jobs`

- Get a list of jobs for a specific user

- Response:

```json
{
  [
  {
    "id": 1,
    "company_name": "Aguirre and Rodgers Plc",
    "company_email": "mail@mail.com",
    "company_phone": "+254717255460",
    "company_website": "https://www.hiqu.us",
    "company_linkedin": "https://www.xekela.mobi",
    "company_logo": "",
    "company_location": "Mombasa",
    "title": "Web developer",
    "slug": "web-developer",
    "category": 1,
    "salary_range": "120000 - 300000",
    "job_type": "Full Time",
    "job_description": "Job description",
    "location": "Mombasa",
    "application_deadline": "2022-04-28",
    "experience": 3,
    "qualification": "Bachelor",
    "link_to_job": "https://www.jusoxoh.in",
    "user": {id},
    "created_at": "2022-04-23T14:38:18.188864+03:00"
  },
  {
    "id": 2,
    "company_name": "Aguirre and Rodgers Plc",
    "company_email": "mail@mail.com",
    "company_phone": "+254717255460",
    "company_website": "https://www.hiqu.us",
    "company_linkedin": "https://www.xekela.mobi",
    "company_logo": "",
    "company_location": "Mombasa",
    "title": "Web developer",
    "slug": "web-developer",
    "category": 1,
    "salary_range": "120000 - 300000",
    "job_type": "Full Time",
    "job_description": "Job description",
    "location": "Mombasa",
    "application_deadline": "2022-04-28",
    "experience": 3,
    "qualification": "Bachelor",
    "link_to_job": "https://www.jusoxoh.in",
    "user": {id},
    "created_at": "2022-04-23T14:38:18.188864+03:00"
  }
]
}
```

`/jobs/`

- Create a new job

```json
{
    "company_name": "Aguirre and Rodgers Plc",
    "company_email": "mail@mail.com",
    "company_phone": "+254717255460",
    "company_website": "https://www.hiqu.us",
    "company_linkedin": "https://www.xekela.mobi",
    "company_logo": "",
    "company_location": "Mombasa",
    "title": "Web developer",
    "slug": "web-developer",
    "category": 1,
    "salary_range": "120000 - 300000",
    "job_type": "Full Time",
    "job_description": "Job description",
    "location": "Mombasa",
    "application_deadline": "2022-04-28",
    "experience": 3,
    "qualification": "Bachelor",
    "link_to_job": "https://www.jusoxoh.in",
    "user": {id},
  }
```

    - Response:

```json
{
  "success": "Job created successfully"
}
```

`/jobs/`

- Get a list of jobs

```json
{
    "id": 1,
    "company_name": "Aguirre and Rodgers Plc",
    "company_email": "mail@mail.com",
    "company_phone": "+254717255460",
    "company_website": "https://www.hiqu.us",
    "company_linkedin": "https://www.xekela.mobi",
    "company_logo": "",
    "company_location": "Mombasa",
    "title": "Web developer",
    "slug": "web-developer",
    "category": 1,
    "salary_range": "120000 - 300000",
    "job_type": "Full Time",
    "job_description": "Job description",
    "location": "Mombasa",
    "application_deadline": "2022-04-28",
    "experience": 3,
    "qualification": "Bachelor",
    "link_to_job": "https://www.jusoxoh.in",
    "user": {id},
    "created_at": "2022-04-23T14:38:18.188864+03:00"
  },
  {
    "id": 2,
    "company_name": "Aguirre and Rodgers Plc",
    "company_email": "mail@mail.com",
    "company_phone": "+254717255460",
    "company_website": "https://www.hiqu.us",
    "company_linkedin": "https://www.xekela.mobi",
    "company_logo": "",
    "company_location": "Mombasa",
    "title": "Web developer",
    "slug": "web-developer",
    "category": 1,
    "salary_range": "120000 - 300000",
    "job_type": "Full Time",
    "job_description": "Job description",
    "location": "Mombasa",
    "application_deadline": "2022-04-28",
    "experience": 3,
    "qualification": "Bachelor",
    "link_to_job": "https://www.jusoxoh.in",
    "user": {id},
    "created_at": "2022-04-23T14:38:18.188864+03:00"
  }
```

`/job/{id}/`

- Get job details

```json
{
    "id": {id},
    "company_name": "Aguirre and Rodgers Plc",
    "company_email": "mail@mail.com",
    "company_phone": "+254717255460",
    "company_website": "https://www.hiqu.us",
    "company_linkedin": "https://www.xekela.mobi",
    "company_logo": "",
    "company_location": "Mombasa",
    "title": "Web developer",
    "slug": "web-developer",
    "category": 1,
    "salary_range": "120000 - 300000",
    "job_type": "Full Time",
    "job_description": "Job description",
    "location": "Mombasa",
    "application_deadline": "2022-04-28",
    "experience": 3,
    "qualification": "Bachelor",
    "link_to_job": "https://www.jusoxoh.in",
    "user": 1,
    "created_at": "2022-04-23T14:38:18.188864+03:00"
  }
```

`/job/{id}/`

- Update job details

```json
{
  "company_name": "Aguirre and Rodgers Plc",
  "company_email": "mail@mail.com",
  "company_phone": "+254717255460",
  "company_website": "https://www.hiqu.us",
  "company_linkedin": "https://www.xekela.mobi",
  "company_logo": "",
  "company_location": "Mombasa",
  "title": "Web developer",
  "slug": "web-developer",
  "category": 1,
  "salary_range": "120000 - 300000",
  "job_type": "Full Time",
  "job_description": "Job description",
  "location": "Mombasa",
  "application_deadline": "2022-04-28",
  "experience": 3,
  "qualification": "Bachelor",
  "link_to_job": "https://www.jusoxoh.in",
  "user": 1
}
```

- Response:

```json
{
  "company_name": "Aguirre and Rodgers Plc",
  "company_email": "mail@mail.com",
  "company_phone": "+254717255460",
  "company_website": "https://www.hiqu.us",
  "company_linkedin": "https://www.xekela.mobi",
  "company_logo": "",
  "company_location": "Mombasa",
  "title": "Web developer",
  "slug": "web-developer",
  "category": 1,
  "salary_range": "120000 - 300000",
  "job_type": "Full Time",
  "job_description": "Job description",
  "location": "Mombasa",
  "application_deadline": "2022-04-28",
  "experience": 3,
  "qualification": "Bachelor",
  "link_to_job": "https://www.jusoxoh.in",
  "user": 1
}
```

`/job/{id}/`

    - Delete job details

- Response:

```json
{
  "success": "Job deleted successfully"
}
```

`/category/list/`

- Get a list of categories

```json
[
  {
    "id": 1,
    "name": "Technology",
    "icon": "fa fa-briefcase",
    "description": "Technology helps..."
  },
  {
    "id": 1,
    "name": "Technology",
    "icon": "fa fa-briefcase",
    "description": "Technology helps..."
  }
]
```

`/category/{id}/jobs`

- Get a list of jobs in a category

```json
[
  {
    "id": 1,
    "company_name": "Aguirre and Rodgers Plc",
    "company_email": "mail@mail.com",
    "company_phone": "+254717255460",
    "company_website": "https://www.hiqu.us",
    "company_linkedin": "https://www.xekela.mobi",
    "company_logo": "",
    "company_location": "Mombasa",
    "title": "Web developer",
    "slug": "web-developer",
    "category": 1,
    "salary_range": "120000 - 300000",
    "job_type": "Full Time",
    "job_description": "Job description",
    "location": "Mombasa",
    "application_deadline": "2022-04-28",
    "experience": 3,
    "qualification": "Bachelor",
    "link_to_job": "https://www.jusoxoh.in",
    "user": 2,
    "created_at": "2022-04-23T14:38:18.188864+03:00"
  }
]
```

# Known Bugs

So far so good there are no bugs related to this project 😎

# Support and contact details 😃

To make a contribution to the code used or any suggestions you can click on the contact link and email me your suggestions.

- Email: wilsonkinyuam@gmail.com
- Phone: +254717255460

# License

Copyright (c) 2022 Wilson Kinyua

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files , to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
