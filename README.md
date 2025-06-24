# Late Show API

A Flask REST API for managing a late night TV show system.

## Setup
```bash
1. Clone the repository

2. Install dependencies:
```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary python-dotenv
pipenv shell

3. Create PostgreSQL database:
```sql
CREATE DATABASE late_show_db;

4. Set up environment variables in .env:
```text
DATABASE_URL=postgresql://username:password@localhost:5432/late_show_db
JWT_SECRET_KEY=your-secret-key

5. Run migrations and seed data:
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py

6. Run the server:
```bash
flask run

- Authentication Flow:
1. Register a user:
```bash
POST /auth/register
Body: {"username": "testuser", "password": "testpass"}

2. Login to get JWT token:
```bash
POST /auth/login
Body: {"username": "testuser", "password": "testpass"}

3. Use the token in protected routes:
```bash
Authorization: Bearer <your-token>

- Routes:
(a.) Public Routes:
1. GET /episodes - List all episodes
2. GET /episodes/<id> - Get episode details with appearances
3. GET /guests - List all guests

(b.)Protected Routes (require JWT)
1. DELETE /episodes/<id> - Delete an episode
2. POST /appearances - Create a new appearance

- Postman Usage:
1. Import the provided Postman collection
2. Start with the register/login requests to get a token
3. Use the token in Authorization header for protected
routes