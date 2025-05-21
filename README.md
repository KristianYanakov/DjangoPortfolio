# 🧑‍💻 Django Portfolio Website

A personal portfolio website built with Django where you can showcase your software projects, tech stack, and more.

---

## 📌 Features

- Project listing with title, description, author, tech stack, and date
- Dynamic detail view for each project
- Clean, responsive UI (uses Tailwind CSS or your custom styling)
- Django admin interface for managing content
- Easily extendable with blog, contact form, or tags

---

## 🛠️ Tech Stack

- Python 3.10+
- Django 5.x
- HTML / CSS (with optional Tailwind)
- SQLite (default) or PostgreSQL (optional)
- Bootstrap or Tailwind CSS (if used)

---

## 🚀 Local Installation Guide

Follow these steps to run the project on your own machine.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/your-repo-name.git
cd your-repo-name
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip freeze > requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser(ADMIN) optional
```bash
python manage.py createsuperuser
```

### 6. Run the Server
```bash
python manage.py runserver
```

Now open your browser and go to http://127.0.0.1:8000/projects/

📁 Project Structure
portfolio/               # Root Django project
├── manage.py
├── db.sqlite3
├── portfolio/           # Project settings
│   ├── settings.py
│   └── urls.py
├── projects/            # Your custom app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── project_list.html
│       └── single_project.html
├── static/              # (Optional) Static files like CSS/JS
├── media/               # (Optional) Uploaded images
├── templates/           # (Optional) Global base.html
└── requirements.txt

🔐 Environment Variables (Optional)
If using a .env file for security:
```bash
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=...
```

Use packages like python-decouple or django-environ to load .env variables.

🧩 Coming Soon (Ideas to Add)
Tags or filters for tech stack

Search bar for projects

About and contact pages

Blog functionality

Slug-based URLs for cleaner links

Deployment to Render / Railway / Vercel

📸 Screenshot
Add a screenshot of your homepage or project list view here.

📄 License

🙋‍♂️ Author
Built by Kristian Yanakov
LinkedIn
GitHub
