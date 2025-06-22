# Django Internship Assignment

## Project Overview
A production-ready Django project demonstrating backend development skills, featuring RESTful APIs, token-based authentication, Celery-powered background tasks, and Telegram Bot integration. Built following best practices for security, modularity, and maintainability.

## Features
- Django REST Framework (DRF) APIs (Public, Protected, User Registration)
- Token-based Authentication using DRF TokenAuth
- User Registration triggers a background Welcome Email via Celery
- Telegram Bot integration using Webhook, storing user data in the database
- Environment variable management using `python-decouple`
- Ready for production (`DEBUG=False`, `ALLOWED_HOSTS`, `.env`)
- Admin site for superuser management

---

## Setup Instructions

### 1. **Clone the Repository**
```bash
git clone <your-github-repo-url>
cd Djjango-Internshiip-Assiignment

2. Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure Environment Variables

cp .env.example .env

Edit .env and set:

Variable	Description
SECRET_KEY	Django secret key
DEBUG	False (for production)
ALLOWED_HOSTS	e.g. 127.0.0.1,localhost,
DATABASE_URL	e.g. sqlite:///db.sqlite3
REDIS_URL	e.g. redis://localhost:6379/0
EMAIL_*	SMTP settings (optional for real emails)
TELEGRAM_BOT_TOKEN_WEBHOOK	Your Telegram Bot API token


⸻

5. Apply Migrations

python manage.py migrate

6. Create a Superuser

python manage.py createsuperuser


⸻

Running Locally

1. Start Redis Server (For Celery)

redis-server

2. Run Django Development Server

python manage.py runserver 8080

3. Start Celery Worker

celery -A api_task_project worker -l info


⸻

API Endpoints

Public Endpoint
	•	GET /api/v1/public/
	•	No Authentication Required

{ "message": "Hello from Public API!" }

Protected Endpoint
	•	GET /api/v1/protected/
	•	Token Authentication Required

{ "message": "Hello from Protected API!", "user": "username" }

User Registration
	•	POST /api/v1/register/

{
  "username": "newuser",
  "password": "password123",
  "email": "user@example.com"
}

Returns auth token and sends welcome email via Celery.

⸻

Telegram Bot Setup

1. Get Telegram Bot Token
	•	Create a bot via BotFather.
	•	Set the token as TELEGRAM_BOT_TOKEN_WEBHOOK in .env.

2. Expose Local Server (for webhook)

ngrok http 8080

3. Set Webhook

curl -X POST "https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN_WEBHOOK>/setWebhook" -d "url=https://<ngrok-url>/api/v1/telegram/webhook/"

4. Test the Bot
	•	Send /start to your bot on Telegram.
	•	Confirm data saved and welcome message sent.

⸻

Celery Task (Email Sending)
	1.	Ensure Redis and Celery are running.
	2.	Register a new user via /api/v1/register/.
	3.	Check Celery worker logs for welcome email confirmation.

⸻

Environment Variables Summary

Variable	Example	Description
SECRET_KEY	your-key	Django secret
DEBUG	False	Debugging flag
ALLOWED_HOSTS	127.0.0.1,localhost,	Allowed hosts
DATABASE_URL	sqlite:///db.sqlite3	SQLite URL
REDIS_URL	redis://localhost:6379/0	Redis URL
EMAIL_HOST	smtp.example.com	SMTP Host
TELEGRAM_BOT_TOKEN_WEBHOOK	xxx:yyy	Telegram Bot Token


⸻

Docker (Optional)

You can add Dockerfile and docker-compose.yml for containerized deployment in production.

⸻

Additional Notes
	•	Web Login Enabled at: /accounts/login/ (Django default login)
	•	Admin panel: /admin/
	•	Celery Required: Redis and Celery must run separately.

⸻

Project Structure Reminder:

Djjango-Internshiip-Assiignment/
│
├── core/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── tasks.py
├── api_task_project/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
├── .env.example
└── README.md


⸻

🚀 Ready for Submission

✔️ Production-ready settings
✔️ Telegram Webhook working via ngrok
✔️ Celery integrated & tested
✔️ Good code structure
✔️ GitHub push + this README

⸻

For any issues, open an issue or contact the maintainer.

---

## ✅ **Summary of Fixes Applied:**
| Problem | Fix |
|--------|------|
| Incorrect Celery Command | Fixed: `celery -A api_task_project worker -l info` |
| Project Name space | Fixed to `api_task_project` as per your `manage.py` structure |
| Django Login | Mentioned `/accounts/login/` |
| Ngrok | Example included for setting webhook |
| `.env.example` | Clearly mentioned |
| Docker | Marked as optional (not required by your assignment) |
| General Cleanup | Removed extra/unrelated lines (like `pip --version` etc) |
| Directory Structure | Provided for clarity |

---

If you want — I can also:
- Generate `.env.example` file.
- Provide sample **Dockerfile** and **docker-compose.yml** (optional).
- Make a Git commit plan for your GitHub.

Let me know.