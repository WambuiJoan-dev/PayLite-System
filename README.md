
# PayLite System

A backend system for managing **"Lipa Mdogo Mdogo"** (installment-based mobile phone sales).  
Built with Flask, SQLAlchemy, Marshmallow, and CLI support.

---

## 📌 Project Summary

PayLite is a backend system designed for shops selling mobile phones on credit.

**Key Features:**

- Manage customers and their credit status
- Manage phone stock and sales
- Record payments and track balances
- Automatically update stock and credit status
- RESTful API + CLI interface
- Validation and error handling
- Business reports (coming soon)
- Ready for production deployment

---

## 🏗️ Tech Stack

- **Flask** – REST API framework  
- **Flask-SQLAlchemy** – ORM / Database layer  
- **Marshmallow** – Serialization + Validation  
- **Flask-Migrate** – Database migrations *(planned)*  
- **CLI** – Admin CLI for data management  
- **SQLite** – Development DB *(easily swappable to Postgres/MySQL)*  
- **Docker** – Deployment *(planned)*  

---

## 🚀 Setup & Installation

### Clone the repo

```bash
git clone https://github.com/WambuiJoan-dev/PayLite-System.git
cd PayLite-System
```

### Create virtualenv and install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file:

```env
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///PayLite.db
```

---

## 🏃 Running the API

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

The API will run at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖥️ Running the CLI

```bash
python cli.py
```

You will be able to manage customers, phones, sales, payments via CLI menu.

---

## 📚 API Endpoints (Sample)

| Method | Endpoint      | Description              |
|--------|---------------|--------------------------|
| GET    | /customers/   | List all customers       |
| POST   | /customers/   | Add new customer         |
| GET    | /phones/      | List all phones          |
| POST   | /phones/      | Add new phone            |
| GET    | /sales/       | List all sales           |
| POST   | /sales/       | Create new sale          |
| POST   | /payments/    | Record payment           |

**More endpoints planned → with pagination, filtering, sorting.**

---

## 🧪 Testing

Run tests:

```bash
pytest
```

Test coverage report:

```bash
pytest --cov
```

---

## 📊 Business Reports (Planned)

- Customers with outstanding balances
- Top selling phones
- Revenue report

---

## 🚢 Deployment

- Add Dockerfile → ready to deploy to Heroku, Render, Fly.io
- Production-ready config *(in progress)*

---

## 🗺️ Roadmap / TODO

See [checklist.md](./checklist.md) for full roadmap.

**Next up:**

- [ ] Pagination / Filtering / Sorting
- [ ] JWT Authentication
- [ ] Unit tests
- [ ] Business reports
- [ ] Production deployment

---

## 🤝 Contributing

Feel free to fork and contribute → PRs are welcome!

---

## ⭐ Acknowledgements

Inspired by the real-world "Lipa Mdogo Mdogo" use case in mobile phone shops in Kenya.  
Developed to demonstrate backend architecture, data modeling, API design, testing, and deployment best practices.

---

## 👤 Author

**Joan Wambui**  
Software Engineer  
[GitHub Profile](https://github.com/WambuiJoan-dev)