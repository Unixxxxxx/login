<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a3a2a,100:2ea043&height=180&section=header&text=Django%20Login%20%26%20Blog%20App&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=Full-Stack%20Web%20App%20%7C%20Docker%20%7C%20CI%2FCD%20via%20GitHub%20Actions&descAlignY=58&descSize=16&animation=fadeIn" />

<br/>

[![Django](https://img.shields.io/badge/Django-Login_%26_Blog-2ea043?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-6e40c9?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-f0a500?style=for-the-badge)](LICENSE)

<br/>

> A powerful Django-based web application featuring modular apps for **user authentication**, **blog post management**, and **extended utilities** — fully containerised with Docker and automated with GitHub Actions CI/CD.

<br/>

[✨ Features](#-features) &nbsp;·&nbsp; [📁 Structure](#️-project-structure) &nbsp;·&nbsp; [🚀 Quick Start](#-quick-start) &nbsp;·&nbsp; [🐳 Docker](#-docker-deployment) &nbsp;·&nbsp; [🔁 CI/CD](#-cicd-pipeline) &nbsp;·&nbsp; [📦 Dependencies](#-dependencies)

</div>

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 🔐 | **User Authentication** | Secure login and registration system |
| 📝 | **Blog Management** | Create, list, and manage blog posts |
| 📁 | **Media Uploads** | Handle images and Excel file uploads |
| 📊 | **Excel Processing** | Read and store data from `.xlsx` files |
| 📜 | **Admin Access Logs** | Track admin activity via log files |
| 🐳 | **Dockerized Setup** | One-command container build & run |
| 🔄 | **CI/CD Pipeline** | Auto-build, push, and deploy on commit |

---

## 🗂️ Project Structure

```bash
django-login-blog/
│
├── 📄 Dockerfile                   # Docker image configuration
├── 📄 manage.py                    # Django entry point
├── 📄 requirements.txt             # Python dependencies
├── 📄 cb.sqlite3                   # SQLite database
├── 📄 user_data.xlsx               # Sample Excel data file
│
├── 📂 templates/                   # HTML UI templates
│   ├── base.html                   # Base layout template
│   ├── index.html                  # Home page
│   ├── form.html                   # Form page
│   ├── blog.html                   # Blog listing page
│   ├── Thankyou.html               # Success / thank-you page
│   └── myapp/
│       └── pdf_list.html           # PDF listing template
│
├── 📂 media/                       # User-uploaded files
│   ├── blog_image/                 # Blog post images
│   └── user_data.xlsx              # Uploaded Excel data
│
├── 📂 log/
│   └── admin_access.log            # Admin activity log
│
├── 📂 login/                       # 🔐 Authentication app
│   ├── settings.py                 # Project settings
│   ├── views.py                    # Login/register views
│   ├── urls.py                     # URL routing
│   ├── wsgi.py                     # WSGI entry point
│   └── asgi.py                     # ASGI entry point
│
├── 📂 myapp/                       # 📝 Blog logic app
│   ├── models.py                   # Blog data models
│   ├── forms.py                    # Blog forms
│   ├── views.py                    # Blog views
│   ├── urls.py                     # Blog URL routing
│   └── migrations/                 # Database migrations
│
├── 📂 myapp1/                      # 🔧 Extended feature module
│   ├── models.py                   # Extended models
│   ├── views.py                    # Extended views
│   └── urls.py                     # Extended URL routing
│
└── 📂 .github/
    └── workflows/
        └── deploy.yml              # 🔄 GitHub Actions CI/CD workflow
```

---

## 🚀 Quick Start

### Prerequisites

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-2ea043?style=flat-square&logo=django&logoColor=white)](https://djangoproject.com)
[![Docker](https://img.shields.io/badge/Docker-Optional-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)

### 1️⃣ &nbsp; Clone the Repository

```bash
git clone https://github.com/Unixxxxxx/django-login-blog.git
cd django-login-blog
```

### 2️⃣ &nbsp; Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ &nbsp; Apply Migrations

```bash
python manage.py migrate
```

### 4️⃣ &nbsp; Run Development Server

```bash
python manage.py runserver
```

> ✅ Visit **`http://localhost:8000`** in your browser.

---

## 🐳 Docker Deployment

### Step 1 — Build the Image

```bash
docker build -t mynewapp .
```

### Step 2 — Run the Container

```bash
docker run -d -p 8000:8000 mynewapp
```

> ✅ Visit **`http://localhost:8000`** — your app is live inside Docker.

### Useful Docker Commands

```bash
# View running containers
docker ps

# Stop the container
docker stop <container_id>

# View logs
docker logs <container_id>
```

---

## 🔁 CI/CD Pipeline

Deployment is fully automated via **GitHub Actions** on every push to `main`.

```
📦 Push to main
    │
    ├── ✅  Build Docker image
    ├── ✅  Login to Docker Hub
    └── ✅  Push image to Docker Hub
```

**Workflow file location:**

```bash
.github/workflows/deploy.yml
```

**Workflow overview:**

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main]

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build Docker image
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/mynewapp .
      - name: Login to Docker Hub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin
      - name: Push to Docker Hub
        run: docker push ${{ secrets.DOCKER_USERNAME }}/mynewapp
```

---

## 📦 Dependencies

Install all dependencies with a single command:

```bash
pip install -r requirements.txt
```

**Core packages:**

| Package | Purpose |
|---------|---------|
| `django` | Web framework |
| `pillow` | Image upload handling |
| `openpyxl` | Excel file processing |
| `gunicorn` | Production WSGI server |

---

## 📂 Data & Media Handling

```
📁 Media Files    →   media/blog_image/        (blog post images)
📊 Excel Files    →   media/user_data.xlsx     (uploaded data)
📜 Admin Logs     →   log/admin_access.log     (access tracking)
🗃️  Database       →   cb.sqlite3               (SQLite — dev only)
```

> ⚠️ **Production Note:** Replace `cb.sqlite3` with PostgreSQL or MySQL for production deployments.

---

## 🙋‍♂️ Author

<div align="center">

<br/>

**Sudhanshu Kumar**

🛠️ DevSecOps Enthusiast &nbsp;|&nbsp; 💻 Python & Django Developer

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/sudhanshu-kumar)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-00d9ff?style=for-the-badge&logo=vercel&logoColor=black)](https://github.com/Unixxxxxx)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sudhanshu@example.com)

<br/>

</div>

---

## 📜 License

```
MIT License — free to use, modify, and distribute.
See the LICENSE file for full terms.
```

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:2ea043,50:1a3a2a,100:0d1117&height=100&section=footer&animation=fadeIn" />

![Built with Django](https://img.shields.io/badge/Built_with-Django_%26_Docker-2ea043?style=flat-square&logo=django&logoColor=white)
&nbsp;
![Made by Sudhanshu](https://img.shields.io/badge/Made_by-Sudhanshu_Kumar-3776AB?style=flat-square&logo=python&logoColor=white)
&nbsp;
![License MIT](https://img.shields.io/badge/License-MIT-f0a500?style=flat-square)

</div>
