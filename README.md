# 🛡️ Django Login & Blog Application with Docker Deployment

A robust Django-based application with modular apps for user authentication (`login`), blog posting (`myapp`), and additional features (`myapp1`). Designed to be containerized and deployed using Docker & GitHub Actions.

---

## 🗂️ Project Structure


├── Dockerfile # Docker configuration
├── manage.py # Django entry point
├── cb.sqlite3 # SQLite database
├── requirements.txt # Python dependencies
├── user_data.xlsx # Uploaded user data (Excel)
│
├── templates/ # HTML templates
│ ├── base.html
│ ├── index.html
│ ├── form.html
│ ├── blog.html
│ ├── Thankyou.html
│ └── myapp/pdf_list.html
│
├── media/ # Media uploads
│ └── blog_image/
│ └── user_data.xlsx
│
├── log/
│ └── admin_access.log # Logging activity
│
├── login/ # Authentication app
│ ├── asgi.py
│ ├── middleware/
│ ├── settings.py
│ ├── urls.py
│ ├── views.py
│ └── wsgi.py
│
├── myapp/ # Blog and main logic
│ ├── admin.py
│ ├── models.py
│ ├── forms.py
│ ├── urls.py
│ ├── views.py
│ ├── tests.py
│ └── migrations/
│
├── myapp1/ # Extended features or future app
│ ├── admin.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── tests.py
│ └── migrations/


---

## 🚀 Features

- ✅ User Login & Signup
- 📝 Blog Post Creation
- 📄 Upload and manage Excel files
- 🖼️ Media uploads with Django
- 🧾 Logging access to log files
- 🐳 Dockerized for seamless deployment
- 🔁 CI/CD with GitHub Actions

---

## 🐳 Running the App with Docker

1. **Build the Docker Image**
   ```bash
   docker build -t yourdockerhubusername/myapp .
Run the Container

bash
Copy
Edit
docker run -d -p 8000:8000 yourdockerhubusername/myapp
Visit: http://localhost:8000

🛠️ GitHub Actions Deployment
The project includes a GitHub Actions workflow:

Build Docker image

Log in to Docker Hub

Push the image on every commit

Your workflow file: .github/workflows/deploy.yml

📦 Requirements
All dependencies are listed in requirements.txt. Install them with:

bash
Copy
Edit
pip install -r requirements.txt

📁 Media & Data Handling
Uploaded images go to: /media/blog_image/

Logs are stored in: log/admin_access.log

Uploaded Excel files: user_data.xlsx

🔒 Security Tip
Make sure to add these secrets in GitHub → Settings > Secrets and Variables > Actions:

DOCKER_USERNAME

DOCKER_PASSWORD

🙋 Author
Sudhanshu Kumar
Built with ❤️ using Django, Docker, and GitHub Actions.


📜 License
This project is licensed under the MIT License.

---

Let me know if you want to:
- Add badges (Docker Hub, GitHub Actions)
- Include screenshots of the UI
- Add environment variable instructions for production

I'll help you polish it even more!
