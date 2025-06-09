from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()  

def create_app():
    application = Flask(__name__)
    application.config.from_object('app.config.Config')
    
    
    db.init_app(application)
    jwt.init_app(application)  
    CORS(application, origins=["http://localhost:3000"])  
    
    import app.models  
    
    
    from app.routes.customers import customer_bp
    from app.routes.phones import phone_bp
    from app.routes.sales import sale_bp
    from app.routes.payments import payment_bp
    from app.routes.auth import auth_bp  
    
    application.register_blueprint(customer_bp, url_prefix='/customers')
    application.register_blueprint(phone_bp, url_prefix='/phones')
    application.register_blueprint(sale_bp, url_prefix='/sales')
    application.register_blueprint(payment_bp, url_prefix='/payments')
    application.register_blueprint(auth_bp, url_prefix='/auth')  
    
    return application
