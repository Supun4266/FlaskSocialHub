# FlaskSocialHub

A social posting platform built with **Flask** and **MongoDB**. Admins publish and manage posts with images; registered users can like and comment. Authentication uses **JWT** tokens and **bcrypt**-hashed passwords, and the main flows are covered by **pytest** and **Selenium** tests.

## Features

- User registration and login with bcrypt password hashing
- JWT-based authentication with 1-hour token expiry
- Role-based access: admin dashboard vs. user dashboard
- Admins can create, edit and delete posts with image uploads (file-type checked)
- Users can like posts, comment, and delete their comments
- "Most liked" page and an admin view of all interactions

## Tech stack

| Area | Technology |
|---|---|
| Backend | Python, Flask |
| Database | MongoDB (Flask-PyMongo) |
| Auth | PyJWT, bcrypt |
| Front end | Jinja2 templates, HTML, CSS |
| Testing | pytest (unit/integration), Selenium (browser automation) |

## Run locally

Requires Python 3.11+ and a running MongoDB instance.

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

Set your secrets as environment variables (local defaults exist, but don't use them in production):

```bash
set SECRET_KEY=your-secret
set JWT_SECRET_KEY=your-jwt-secret
set MONGO_URI=mongodb://127.0.0.1:27017/flasksocialhub
```

Start the app:

```bash
flask --app app run
```

Then open http://localhost:5000.

## Tests

```bash
pytest                                  # registration, login, posts, likes and comments
python create_users_selenium.py         # browser test: creates users through the UI
python admin_delete_post_selenium.py    # browser test: admin deletes a post
```

The Selenium scripts need Google Chrome installed; `webdriver-manager` downloads the matching driver.
