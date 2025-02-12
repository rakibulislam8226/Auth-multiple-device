# Project Name

```markdown
A full-stack web application built using **Django Rest Framework (DRF) for the backend** and **Vue.js for the frontend**, hosted on a single server.
```

## Features
```markdown
- User authentication (JWT-based)
- RESTful API with Django Rest Framework
- Vue.js frontend served by Django
- Single-server deployment
```

---

## Setup Instructions

### 1️⃣ Clone the Repository
```sh
git clone git@github.com:rakibulislam8226/Auth-multiple-device.git
cd your-repo
```

### 2️⃣ Setup Backend (Django)

#### Create a virtual environment and install dependencies:
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

#### Apply migrations and create a superuser:
```sh
python manage.py migrate
python manage.py createsuperuser
```

#### Run the Django server:
```sh
python manage.py runserver
```

### 3️⃣ Setup Frontend (Vue.js)

#### Install dependencies:
```sh
npm install
```

#### Build Vue frontend and serve with Django:
```sh
npm run build
cp -r dist/* ../static/
cd ..
python manage.py collectstatic --noinput
```

### 4️⃣ Access the Application
```markdown
- **Backend API**: `http://127.0.0.1:8000/api/`
- **Frontend**: `http://127.0.0.1:8000/`
```

---

## API Documentation
```sh
http://127.0.0.1:8000/api/docs/
```



