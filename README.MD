
# Django Internship 

## Project Overview
A production-ready Django project for a job portal, featuring RESTful APIs, user registration with token authentication, Celery-powered background tasks, and Telegram bot integration. Built with best practices for security, modularity, and maintainability.

## Features
- Django REST Framework APIs (public, protected, user registration)
- Token-based authentication
- User registration triggers a Celery welcome email
- Telegram bot integration with webhook and user info storage
- Production-ready settings with environment variable management
- Docker-ready configuration (see below)
- Admin site for superuser access

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd job_portal
   ```
2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables:**
   - Copy `.env.example` to `.env` and fill in the required values.
   ```bash
   cp .env.example .env
   ```
5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

## Environment Variables
All sensitive and environment-specific settings are managed via `.env` using `python-decouple`.

| Variable                | Example Value                | Description                                 |
|------------------------ |-----------------------------|---------------------------------------------|
| SECRET_KEY              | your-secret-key              | Django secret key                           |
| DEBUG                   | False                        | Debug mode (should be False in production)  |
| ALLOWED_HOSTS           | 127.0.0.1,localhost          | Comma-separated list of allowed hosts       |
| DATABASE_URL            | sqlite:///db.sqlite3         | Database connection URL                     |
| REDIS_URL               | redis://localhost:6379/0     | Redis connection URL for Celery             |
| EMAIL_HOST              | smtp.example.com             | SMTP server host                            |
| EMAIL_PORT              | 587                          | SMTP server port                            |
| EMAIL_USE_TLS           | True                         | Use TLS for email                           |
| EMAIL_USE_SSL           | False                        | Use SSL for email                           |
| EMAIL_HOST_USER         | user@example.com             | SMTP username                               |
| EMAIL_HOST_PASSWORD     | your-email-password          | SMTP password                               |
| TELEGRAM_BOT_TOKEN_WEBHOOK | 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11 | Telegram bot token         |

## Running Locally
1. **Start Redis:**
   ```bash
   redis-server
   ```
2. **Start Django development server:**
   ```bash
   python manage.py runserver
   ```
3. **Start Celery worker:**
   ```bash
   celery -A job_portal worker -l info
   ```

## API Endpoints

### 1. Public Endpoint
- **URL:** `/api/v1/public/`
- **Method:** `GET`
- **Authentication:** None
- **Response:**
  ```json
  { "message": "Hello from Public API!" }
  ```

### 2. Protected Endpoint
- **URL:** `/api/v1/protected/`
- **Method:** `GET`
- **Authentication:** Token (in `Authorization: Token <token>` header)
- **Response:**
  ```json
  { "message": "Hello from Protected API!", "user": "username" }
  ```

### 3. User Registration
- **URL:** `/api/v1/register/`
- **Method:** `POST`
- **Authentication:** None
- **Request Body:**
  ```json
  {
    "username": "newuser",
    "password": "password123",
    "email": "user@example.com"
  }
  ```
- **Response:**
  ```json
  {
    "message": "User registered successfully.",
    "token": "<auth_token>"
  }
  ```
- **Note:** Triggers a background welcome email via Celery.

#### How to Obtain a Token
- Register via `/api/v1/register/` or use the admin to create a user. The token is returned on registration or can be obtained via the admin.

## Telegram Bot Setup
1. **Obtain a bot token:**
   - Talk to [BotFather](https://t.me/botfather) on Telegram and create a new bot.
   - Copy the token and set it as `TELEGRAM_BOT_TOKEN_WEBHOOK` in your `.env`.
2. **Expose your local server:**
   - Use [ngrok](https://ngrok.com/) to expose your local server:
     ```bash
     ngrok http 8000
     ```
   - Note the HTTPS URL provided by ngrok.
3. **Set the webhook URL:**
   - Replace `<ngrok-url>` and `<bot-token>` below:
     ```bash
     curl -X POST "https://api.telegram.org/bot<bot-token>/setWebhook" -d "url=<ngrok-url>/api/v1/telegram/webhook/"
     ```
4. **Test the bot:**
   - Send `/start` to your bot in Telegram. You should receive a confirmation message and see your info stored in the database.

## Celery Setup & Testing
1. **Start Redis:**
   ```bash
   redis-server
   ```
2. **Start Celery worker:**
   ```bash
   celery -A job_portal worker -l info
   ```
3. **Test email task:**
   - Register a new user via the API. Check the console for the welcome email output.

## Docker (Optional)
- You can add a `Dockerfile` and `docker-compose.yml` for containerized deployment.

---

For any issues, please open an issue or contact the maintainer. 

pip --version 

python3 -m django startproject job_portal . 
