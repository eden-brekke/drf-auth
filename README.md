# Lab 33

## Django Authentication

### Author

- Eden Brekke
- Followed the class demo and altered to what I wanted

### Collaborator

Worked with Benjamin Carter

### How to Run this Application

- python -m venv .venv
- .\.venv\Scripts\activate
- pip install django
- pip install djangorestframework
- pip install djangorestframework-simplejwt
- pip install psycopg2-binary
- pip install gunicorn
- pip install whitenoise
- django-admin startproject projectname
- python manage.py migrate
- python manage.py runserver
- python manage.py startapp app
- Make TUV and add to settings
- python manage.py makemigrations app
- python manage.py createsuperuser
- python manage.py runserver

- docker compose up --build
- docker compose run web bash
- Redo python manage stuff in docker terminal!

### ThunderClient:

So! You want to use ThunderClient?  
Can do!  

I've created a superuser with username admin and password admin  

- Great a new request
- POST to http://localhost:8000/api/token  
- In the body of the post, as JSON data input:

```JSON
    {
        "username":"admin","password":"admin"
    }
```

- This will generate a refresh and access token for you.
  - Mine looks like:

```JSON
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDIwNzEyNiwiaWF0IjoxNjU0MTIwNzI2LCJqdGkiOiJhNjJiYmI0MmE5ZWM0MjFmOGI0YTcxNTU0ODY2M2YzNyIsInVzZXJfaWQiOjF9.baq_m8zssZ_wzFXkw56PirJlQScEg49lvTicizf2j9c",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0MTIxMDI2LCJpYXQiOjE2NTQxMjA3MjYsImp0aSI6ImNiYTEwODY5MTM4YzQ5MmM4NDliZTk4ZTkxZGQ0MGEzIiwidXNlcl9pZCI6MX0.okhZyChC0M2Mezjg53JQGNypCiK0AQeGNl0xRw8mEig"
}
```

- Make a new request!
- GET from http://localhost:8000/api/v1/pet_pics
  - Under Auth --> Bearer
  - Paste the Access token that was generated from the POST request.
- This should allow you to see the contents of the page
  - For me that looks like:

```JSON
[
  {
    "id": 1,
    "name": "Jackingtons the Third",
    "type_of_pet": "Cat",
    "description": "He's a silly boy and I love him many",
    "img": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.15752-9/280963822_3121528261449014_4912931217840871039_n.jpg?stp=dst-jpg_p1080x2048&_nc_cat=104&ccb=1-7&_nc_sid=ae9488&_nc_ohc=Roj9u7HqefcAX_-Q9Ux&_nc_ht=scontent-sea1-1.xx&oh=03_AVKcvo_rNLpnK5MhXy1Ex2s6EsIcYZ0LTGsWH0Du2fR2PQ&oe=6298BE4B",
    "added_by": 1
  },
  {
    "id": 2,
    "name": "Pumpkin",
    "type_of_pet": "Cat",
    "description": "Pumpkin is a model kitty",
    "img": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.15752-9/278596827_268614505479231_2907753800458125029_n.jpg?stp=dst-jpg_p1080x2048&_nc_cat=111&ccb=1-7&_nc_sid=ae9488&_nc_ohc=3kRlVJCjtB8AX8v4Ap9&tn=H3qSDr1DGr70j70e&_nc_ht=scontent-sea1-1.xx&oh=03_AVJbe21JNYy3AcUFF0eLrPQCErfwy5WYs6fO_XJ7_G4GHg&oe=62BEE37D",
    "added_by": 1
  },
  {
    "id": 3,
    "name": "Jack2.0",
    "type_of_pet": "Cat",
    "description": "Jack is always helping me",
    "img": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.15752-9/279059667_365426115617412_5086589871209871886_n.jpg?stp=dst-jpg_s2048x2048&_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_ohc=qA8V-IgBnt4AX9oIpAY&_nc_ht=scontent-sea1-1.xx&oh=03_AVIYCKmOfmcan9tUSy5qFZXwvpB0Gn9ZfDta8v3zaPFrBw&oe=62BE76E7",
    "added_by": 2
  },
  {
    "id": 4,
    "name": "Jack2.0",
    "type_of_pet": "Cat",
    "description": "Jack is always helping me",
    "img": "https://scontent-sea1-1.xx.fbcdn.net/v/t1.15752-9/279059667_365426115617412_5086589871209871886_n.jpg?stp=dst-jpg_s2048x2048&_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_ohc=qA8V-IgBnt4AX9oIpAY&_nc_ht=scontent-sea1-1.xx&oh=03_AVIYCKmOfmcan9tUSy5qFZXwvpB0Gn9ZfDta8v3zaPFrBw&oe=62BE76E7",
    "added_by": 2
  }
]
```

### Tests

- to run tests import the class PetPic
- import django.test import APITestCase
- python manage.py test to run tests

- I referenced the tests provided in today's demo