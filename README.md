<h1 align="center">🛡️ Django Login & Blog App</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Django-Login%20%26%20Blog-green?style=for-the-badge&logo=django" />
  <img src="https://img.shields.io/badge/Docker-Deploy-blue?style=for-the-badge&logo=docker" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-purple?style=for-the-badge&logo=githubactions" />
</p>

> A powerful Django-based application with modular apps for user login (`login`), blog post management (`myapp`), and extended modules (`myapp1`). Fully containerized with Docker and integrated CI/CD via GitHub Actions.

---

## 🗂️ Project Structure

![image](https://github.com/user-attachments/assets/e78ec4b3-41e5-48a4-950f-284fbda25a7a)


---

## 🚀 Features

🔐 User Login & Signup  
📝 Create & View Blog Posts  
📁 Upload and Process Excel Files  
🖼️ Upload Blog Images  
🧾 Logging for Admin Access  
🐳 Dockerized Setup  
🔁 CI/CD with GitHub Actions

---

## 🐳 Docker Setup

> **Build Docker Image**

```bash
docker build -t yourdockerhubusername/myapp .
Run Docker Container

bash
Copy
Edit
docker run -d -p 8000:8000 yourdockerhubusername/myapp
🔗 Visit: http://localhost:8000

⚙️ GitHub Actions CI/CD
This repo includes a GitHub Actions workflow that:

🏗️ Builds Docker image

🔐 Authenticates with Docker Hub

🚀 Pushes on commit

📁 File location:

bash
Copy
Edit
.github/workflows/deploy.yml
⚙️ GitHub Actions CI/CD
This repo includes a GitHub Actions workflow that:

🏗️ Builds Docker image

🔐 Authenticates with Docker Hub

🚀 Pushes on commit

📁 File location:

bash
Copy
Edit
.github/workflows/deploy.yml
📦 Requirements
Install dependencies locally:

bash
Copy
Edit
pip install -r requirements.txt
📁 Media & Logs
📸 Uploaded Images → /media/blog_image/

🧾 Logs → /log/admin_access.log

📊 Excel Uploads → user_data.xlsx

🔐 GitHub Secrets (Required for CI/CD)
Go to: GitHub → Settings → Secrets → Actions
Add the following secrets:

Name	Description
DOCKER_USERNAME	Your Docker Hub username
DOCKER_PASSWORD	Your Docker Hub token or pwd

🙋 Author
Sudhanshu Kumar
💻 Developer | ☁️ Cloud Enthusiast | 🐧 Linux Lover

📜 License
This project is licensed under the MIT License.





