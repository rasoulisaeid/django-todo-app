# to-do-app
# Django Todo App

![Alt text](demo/demo.jpg)


This is a simple todo application built with Django.

## Table of Contents

- [1. Project Overview](#project-overview)
- [2. Features](#features)
- [3. Installation](#installation)
  - [3.1 Prerequisites](#prerequisites)
  - [3.2 Local Setup](#local-setup)
  - [3.3 Docker Setup (if applicable)](#docker-setup-if-applicable)
- [4. Usage](#usage)
  - [4.1 Running the Development Server](#running-the-development-server)
  - [4.2 Accessing the Application](#accessing-the-application)

## 1. Project Overview

This project is a simple Django-based todo application. It allows users to create, update, and delete tasks.

## 2. Features

- User authentication (registration and login)
- Create, read, update, and delete tasks (CRUD operations)
- Responsive design

## 3. Installation

### 3.1 Prerequisites

- Python (version >= 3.9)
- Django (version >= 3.2)

### 3.2 Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/rasoulisaeid/django-todo-app.git
   cd django-todo-app/

#### Create a virtual environment (optional but recommended)

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```


#### Install dependencies
```bash
pip install -r requirements.txt
```
#### Apply migrations
```bash
python manage.py migrate
```

### 3.3 Docker Setup (if applicable)
#### Build the Docker containers
```bash
docker-compose build
```

#### Run the containers
```bash
docker-compose up
```

## 4. Usage
### 4.1 Running the Development Server
#### Start the Django development server:
```bash
python manage.py runserver
```

### 4.2 Accessing the Application
#### Open a web browser and go to:
`http://localhost:8000/`