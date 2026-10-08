import os


class Config:
    # Set these as environment variables in production; the defaults are for local development only.
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-change-me')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://127.0.0.1:27017/test')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'dev-jwt-secret-change-me')
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
