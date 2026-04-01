# 🚀 Dockerized Portfolio

A modern **developer portfolio** built using **FastAPI, MongoDB Atlas, HTML/CSS/JS**, designed with a **Docker-based microservices architecture**.

This project demonstrates practical skills in:

* 🐳 Docker containerization
* 🧩 Microservices architecture
* ⚙️ CI/CD pipeline using GitHub Actions
* 🔗 API communication between services
* ☁️ Cloud-ready backend (MongoDB Atlas)
* 📦 GitHub project structuring
* ⚡ FastAPI backend development

The application dynamically loads projects from the database and allows visitors to send messages via a contact form stored in MongoDB Atlas.

---

# 🏗️ Architecture Overview

The project follows a **2-service architecture**:

Browser -> Frontend Service (FastAPI + Jinja2) -> REST API -> Backend Service (FastAPI) -> MongoDB Atlas (Cloud Database)

Each service runs in its own Docker container.

---

# 🐳 Docker Microservices

The application is split into two independent services:

### 1️⃣ Frontend Service

* Serves UI using Jinja2 templates
* Handles user interaction
* Communicates with backend via REST API
* Runs on port **3000**

### 2️⃣ Backend Service

* Handles business logic
* Provides API endpoints
* Connects to MongoDB Atlas
* Runs on port **7000**

---

# ⚙️ CI/CD Pipeline (GitHub Actions)

This project includes a CI pipeline using GitHub Actions to automatically build and test the application whenever code is pushed to the repository.

The workflow ensures that the application builds correctly and that the backend API is reachable.

## 🚀 CI Workflow Steps

When code is pushed to the repository, the pipeline performs the following steps:

### 1️⃣ Checkout the repository code

### 2️⃣ Build the Docker images for both services

Frontend container
Backend container

### 3️⃣ Start the services using Docker Compose

### 4️⃣ Wait for containers to initialize

### 5️⃣ Test the backend API using a curl request

Example test step:
```
- name: Test Backend API
  run: curl http://localhost:7000
```
If the API responds successfully, the workflow passes.

If the API fails to start, the pipeline fails.

---
# 🛠️ Tech Stack

### Backend

* FastAPI
* MongoDB Atlas
* Pydantic

### Frontend

* HTML
* CSS
* JavaScript
* Jinja2 Templates

### DevOps / Tools

* Docker
* Docker Compose
* Git & GitHub
* Environment variables (.env)

---

# 📁 Project Structure

```
project/
│
├── backend/
│   ├── app/
│   │   ├── config/
│   │   │   └── mongo_db_connection.py
│   │   ├── models/
│   │   │   └── contact.py
│   │   ├── routes/
│   │   │   └── my_routes.py
│   │   └── main.py
│   │
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── app/
│   │   ├── static/
│   │   │   ├── style.css
│   │   │   └── script.js
│   │   ├── templates/
│   │   │   └── index.html
│   │   └── main.py
│   │
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── requirements.txt
│   └── .env
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

# ⚙️ Setup Instructions (Docker)

## 1️⃣ Clone repository

```
git clone https://github.com/praveenmehta010/Dockerized_Portfolio
cd Dockerized_Portfolio
```

---

## 2️⃣ Configure environment variables

### backend/.env

```
MONGO_URI=mongodb+srv://username:password@database.mongodb.net/
```

---

### frontend/.env

```
BACKEND_URL=http://backend

PROFILE_IMAGE_URL=YOUR_PROFILE_IMAGE_URL
```

---

## 3️⃣ Build and run containers

```
docker compose up --build
```

Run in background:

```
docker compose up -d --build
```

---

## 4️⃣ Access application

Frontend:

```
http://localhost:3000
```

Backend API docs:

```
http://localhost:7000/docs
```

---

# 🔗 API Endpoints


| Method | Endpoint      | Description               |
| ------ | ------------- | ------------------------- |
| GET    | /get-projects | Fetch portfolio projects  |
| POST   | /contact      | Save contact form message |

---

# 🧠 Key Concepts Demonstrated

### Containerization

Each service runs in an isolated Docker container.

### Service Communication

Frontend communicates with backend using internal Docker network:

```
http://backend:7000
```

### Environment Configuration

Sensitive data stored securely using `.env` files.

### Cloud Database Integration

MongoDB Atlas used for persistent storage.

### GitHub Project Structure

Clean and maintainable folder structure for scalability.

---

# 🚀 Future Improvements

* CI/CD pipeline using GitHub Actions
* Deployment on AWS / Render
* Admin dashboard
* Authentication system
* Kubernetes deployment
* Automated testing

---

# 📬 Contact

Feel free to reach out using the contact form available in the project.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
