from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
# from flask_cors import CORS
 
db = SQLAlchemy()
jwt = JWTManager() 
migrate = Migrate() 

def create_app(config_class=None):
    application = Flask(__name__)
    
    if config_class is None:
        from app.config import Config
        config_class = Config
    
    application.config.from_object(config_class)
    
    db.init_app(application)
    jwt.init_app(application)  
    migrate.init_app(application, db)
    # CORS(application, origins=["http://localhost:3000"])  
    
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
