# run.py
from app import create_app, db

app = create_app()

# Initialize DB (one time)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
