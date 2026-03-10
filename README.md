# THleb

Django web application with community features, neighborhood management, user accounts, and feedback system.

## Tech Stack

- Python 3.14
- Django 5.2+
- django-sass-processor + libsass
- Pillow

## Apps

- **accounts** — user registration and authentication
- **community** — community features
- **neighborhood** — neighborhood management
- **feedback** — user feedback system

## Installation

```bash
git clone https://github.com/xKotom/THleb.git
cd THleb
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Project Structure

```
├── accounts/        # User accounts app
├── community/       # Community app
├── feedback/        # Feedback app
├── neighborhood/    # Neighborhood app
├── kottom/          # Django project settings
├── static/          # Static files
├── templates/       # HTML templates
├── manage.py
└── requirements.txt
```
