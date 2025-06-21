<h1 align="center">🛡️ Django Login & Blog App</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Django-Login%20%26%20Blog-green?style=for-the-badge&logo=django" />
  <img src="https://img.shields.io/badge/Docker-Deploy-blue?style=for-the-badge&logo=docker" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-purple?style=for-the-badge&logo=githubactions" />
</p>

> A powerful Django-based application with modular apps for user login (`login`), blog post management (`myapp`), and extended modules (`myapp1`). Fully containerized with Docker and integrated CI/CD via GitHub Actions.

---
---

## 🗂️ Project Structure

```bash
.
├── Dockerfile                  # Docker configuration
├── manage.py                  # Django entry point
├── cb.sqlite3                 # SQLite DB
├── requirements.txt           # Dependencies
├── user_data.xlsx             # Uploaded Excel file
│
├── templates/                 # UI HTML templates
│   ├── base.html
│   ├── index.html
│   ├── form.html
│   ├── blog.html
│   ├── Thankyou.html
│   └── myapp/pdf_list.html
│
├── media/                     # Uploaded files
│   └── blog_image/
│   └── user_data.xlsx
│
├── log/
│   └── admin_access.log       # Admin access logs
│
├── login/                     # Auth app
│   ├── settings.py
│   ├── views.py
│   ├── urls.py
│   └── wsgi.py, asgi.py
│
├── myapp/                     # Blog logic
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── myapp1/                    # Extended feature module
│   ├── models.py
│   ├── views.py
│   └── urls.py
🌟 Features
🔐 User Authentication (Login/Register)

📝 Blog Creation & Listing

📁 Media Uploads (images & excel files)

📊 Excel File Handling

📜 Log File for Admin Access

🐳 Dockerized Setup

🔄 CI/CD with GitHub Actions

🐳 Docker Deployment
Step 1: Build Docker Image
bash
Copy
Edit
docker build -t yourdockerhubusername/myapp .
Step 2: Run Container
bash
Copy
Edit
docker run -d -p 8000:8000 yourdockerhubusername/myapp
Visit http://localhost:8000

🔁 CI/CD with GitHub Actions
Deployment happens automatically on commit via:

bash
Copy
Edit
.github/workflows/deploy.yml
✅ Build image
✅ Login to Docker Hub
✅ Push image to DockerHub

📦 Dependencies
Install with:

bash
Copy
Edit
pip install -r requirements.txt
📂 Data Handling
Images: /media/blog_image/

Logs: log/admin_access.log

Excel Files: user_data.xlsx

🙋‍♂️ Author
Sudhanshu Kumar
🛠️ DevSecOps Enthusiast | 💻 Python & Django Developer

📫 LinkedIn | 🌐 Portfolio

📜 License
Licensed under the MIT License.



