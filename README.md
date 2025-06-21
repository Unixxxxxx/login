# 🛡️ Django Blog & Login App with Docker Deployment

![Header](https://github.com/yourusername/your-repo/assets/your-image-id/header.png)

A modern, full-stack **Django** application with user authentication, blog management, and deployment through **Docker** and **GitHub Actions**.

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
🌐 UI Preview
🏠 Home Page
![image](https://github.com/user-attachments/assets/1de5f078-3e10-42de-8ad7-69548ca23e46)



🔐 Login Page

![image](https://github.com/user-attachments/assets/f4a90be6-588b-46c2-b9e7-043f018c61d1)


👨‍💻 About Me
![image](https://github.com/user-attachments/assets/b9d2a2a1-7bdb-47d6-8b28-a378ae57d889)


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

🔐 GitHub Secrets (Required)
Make sure to add these in GitHub > Repository Settings > Secrets > Actions:

DOCKER_USERNAME

DOCKER_PASSWORD

🙋‍♂️ Author
Sudhanshu Kumar
🛠️ DevSecOps Enthusiast | 💻 Python & Django Developer

📫 LinkedIn | 🌐 Portfolio

📜 License
Licensed under the MIT License.



