<div align="center">

# 🛡️ AuthProfile

**A modern Django starter with authentication, user profiles, and a full REST API.**

Built with clean architecture, premium UI, and production-ready patterns.

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2-092E20?style=flat-square&logo=django&logoColor=white)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/DRF-3.16-ff1709?style=flat-square&logo=django&logoColor=white)](https://django-rest-framework.org)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat-square&logo=bootstrap&logoColor=white)](https://getbootstrap.com)
[![License](https://img.shields.io/github/license/abdulwahed-mans/django-auth-profile?style=flat-square&color=blue)](LICENSE)
[![Stars](https://img.shields.io/github/stars/abdulwahed-mans/django-auth-profile?style=flat-square&color=yellow)](https://github.com/abdulwahed-mans/django-auth-profile/stargazers)

<br>

[Features](#-features) · [Quick Start](#-quick-start) · [API](#-api-endpoints) · [API Docs](#-api-documentation) · [Tech Stack](#-tech-stack) · [Contributing](#-contributing)

</div>

---

## ✨ Features

| | Feature | Description |
|:--|:--|:--|
| 🔐 | **Authentication** | Register, login, logout with Django's built-in auth system |
| 👤 | **User Profiles** | Auto-created via signals — bio, avatar, location, phone |
| 🔑 | **Password Management** | Change password & forgot/reset password with email flow |
| 🌐 | **REST API** | Full CRUD on profiles, read-only users, token auth (DRF) |
| 🎨 | **Premium UI** | Monochromatic design with Google Fonts, icons, smooth transitions |
| 📱 | **Responsive** | Mobile-first layout with collapsible navbar and dropdown menu |
| 🛠️ | **Admin Panel** | Branded admin with inline profiles, search, and filters |
| 🌱 | **Seed Data** | Management command to populate 5 Swedish demo users + admin |
| 📄 | **Static Pages** | Home, About, and Help pages with polished styling |
| 🔒 | **Environment Config** | Secrets in `.env` via python-dotenv — never committed to git |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/abdulwahed-mans/django-auth-profile.git
cd django-auth-profile

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3
LANGUAGE_CODE=en-us
TIME_ZONE=Europe/Stockholm
```

### Run

```bash
# Apply migrations
python manage.py migrate

# Seed demo data
python manage.py seed_users

# Start the server
python manage.py runserver
```

Open **http://127.0.0.1:8000** and you're live.

---

## 🌐 API Endpoints

All endpoints require authentication (session or token).

| Method | Endpoint | Description |
|:--|:--|:--|
| `GET` | `/api/profiles/` | List all profiles |
| `POST` | `/api/profiles/` | Create a profile |
| `GET` | `/api/profiles/{id}/` | Retrieve a profile |
| `PUT` | `/api/profiles/{id}/` | Update a profile |
| `PATCH` | `/api/profiles/{id}/` | Partial update a profile |
| `DELETE` | `/api/profiles/{id}/` | Delete a profile |
| `GET` | `/api/users/` | List all users (read-only) |
| `GET` | `/api/users/{id}/` | Retrieve a user (read-only) |

### Authentication

```bash
# Session auth — login via browser, then access /api/

# Token auth — include header:
curl -H "Authorization: Token YOUR_TOKEN" http://127.0.0.1:8000/api/profiles/
```

Visit **/api/** for the interactive browsable API.

---

## 📖 API Documentation

Interactive API documentation powered by [drf-spectacular](https://drf-spectacular.readthedocs.io/):

| URL | Interface | Description |
|:--|:--|:--|
| `/api/docs/` | **Swagger UI** | Interactive API explorer — try endpoints live |
| `/api/redoc/` | **ReDoc** | Clean, readable API reference with search |
| `/api/schema/` | **OpenAPI Schema** | Raw OpenAPI 3.0 JSON — import into Postman, Insomnia, etc. |
| `/api-docs/` | **API Docs Page** | Styled overview page with all endpoints and auth info |

---

## 🧪 Test Accounts

The `seed_users` command creates these demo accounts:

| Username | Email | Location | Role | Password |
|:--|:--|:--|:--|:--|
| `admin` | admin@django.local | — | Superuser | `Admin123!` |
| `erik.lindberg` | erik@example.se | Stockholm | User | `SwedishTest123!` |
| `anna.johansson` | anna@example.se | Gothenburg | User | `SwedishTest123!` |
| `oscar.nilsson` | oscar@example.se | Malmö | User | `SwedishTest123!` |
| `sara.eriksson` | sara@example.se | Uppsala | User | `SwedishTest123!` |
| `karl.svensson` | karl@example.se | Linköping | User | `SwedishTest123!` |

---

## 🗺️ URL Map

| URL | Page | Auth Required |
|:--|:--|:--:|
| `/` | Home (landing page) | No |
| `/about/` | About page | No |
| `/help/` | Help center | No |
| `/login/` | Sign in | No |
| `/register/` | Create account | No |
| `/dashboard/` | User dashboard | Yes |
| `/profile/` | Edit profile | Yes |
| `/password-change/` | Change password | Yes |
| `/password-reset/` | Forgot password | No |
| `/api/` | Browsable API root | Yes |
| `/api/docs/` | Swagger UI | No |
| `/api/redoc/` | ReDoc | No |
| `/api/schema/` | OpenAPI schema | No |
| `/api-docs/` | API documentation page | No |
| `/admin/` | Admin panel | Staff |

---

## 🏗️ Tech Stack

| Layer | Technology | Version |
|:--|:--|:--|
| **Language** | Python | 3.14 |
| **Framework** | Django | 5.2 |
| **API** | Django REST Framework | 3.16 |
| **API Docs** | drf-spectacular | 0.29 |
| **Frontend** | Bootstrap 5 | 5.3 |
| **Icons** | Bootstrap Icons | 1.11 |
| **Fonts** | Inter + Plus Jakarta Sans | Google Fonts |
| **Database** | SQLite | 3 |
| **Config** | python-dotenv | 1.2 |

---

## 📁 Project Structure

```
django-auth-profile/
├── config/                      # Project configuration
│   ├── settings.py              # Django settings (reads from .env)
│   ├── urls.py                  # Root URL config
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   └── accounts/                # Main application
│       ├── models.py            # Profile model (OneToOne → User)
│       ├── views.py             # Home, dashboard, profile, auth views
│       ├── forms.py             # Register, profile, user update forms
│       ├── signals.py           # Auto-create profile on user creation
│       ├── serializers.py       # DRF serializers
│       ├── api_views.py         # DRF viewsets
│       ├── api_urls.py          # API router
│       ├── urls.py              # App URL patterns
│       ├── admin.py             # Branded admin with inlines
│       └── management/
│           └── commands/
│               └── seed_users.py
├── templates/
│   ├── base.html                # Base template with navbar & footer
│   └── accounts/
│       ├── home.html            # Landing page
│       ├── login.html           # Sign in
│       ├── register.html        # Create account
│       ├── dashboard.html       # User dashboard
│       ├── profile.html         # Edit profile
│       ├── about.html           # About page
│       ├── help.html            # Help center
│       ├── api_docs.html        # API documentation page
│       ├── password_change.html
│       ├── password_change_done.html
│       ├── password_reset.html
│       ├── password_reset_done.html
│       ├── password_reset_confirm.html
│       └── password_reset_complete.html
├── static/
│   └── css/
│       └── main.css             # Custom premium styles
├── .env                         # Environment variables (git-ignored)
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feat/your-feature`
3. **Commit** your changes: `git commit -m "feat: Add your feature"`
4. **Push** to your fork: `git push origin feat/your-feature`
5. **Open** a Pull Request

### Guidelines

- Follow existing code style and patterns
- Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages
- Test your changes before submitting
- Keep PRs focused — one feature or fix per PR

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with Django, DRF & Bootstrap 5**

If you found this useful, consider giving it a ⭐

</div>
