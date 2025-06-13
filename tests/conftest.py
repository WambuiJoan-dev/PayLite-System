import pytest
from app import create_app, db
from app.config import TestConfig
from app.models import User
from werkzeug.security import generate_password_hash

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(config_class=TestConfig)

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()

            # Create test user
            user = User(
                username="Jedidah",
                password_hash=generate_password_hash("Jeddy@1")  # Use hash if your app uses hashed passwords
            )
            db.session.add(user)
            db.session.commit()

            yield testing_client

            db.session.remove()
            db.drop_all()
