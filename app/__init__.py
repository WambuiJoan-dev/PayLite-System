# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    # Import models here so they are registered
    from app import models

    # Register Blueprints
    from app.routes.customers import customer_bp
    from app.routes.phones import phone_bp
    from app.routes.sales import sale_bp
    from app.routes.payments import payment_bp

    app.register_blueprint(customer_bp, url_prefix='/customers')
    app.register_blueprint(phone_bp, url_prefix='/phones')
    app.register_blueprint(sale_bp, url_prefix='/sales')
    app.register_blueprint(payment_bp, url_prefix='/payments')

    return app
