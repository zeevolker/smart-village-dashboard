# Smart Village Dashboard Backend

Backend API for **Smart Village Dashboard**, a web-based platform designed to support village administration through integrated citizen management, territorial master data, and scalable digital services.

---

## 📌 Overview

Smart Village Dashboard aims to provide a solid backend foundation for village digital transformation by offering:

- Territory master data (Province → Regency → District → Village)
- Citizen management
- Secure authentication
- ETL pipeline for Indonesian administrative data
- RESTful API built with FastAPI
- PostgreSQL database
- Clean architecture for scalability

---

## ✨ Features

### Authentication

- JWT Authentication
- Password hashing
- Role-based authorization (foundation)

### Territory Management

- Provinces
- Regencies
- Districts
- Villages

### Citizen Management

- CRUD Citizen
- Pagination
- Response Wrapper
- Exception Handling

### ETL Pipeline

- Downloader
- Normalizer
- Cleaner
- Validator
- Exporter
- Seeder

### Backend Architecture

- Repository Pattern
- Service Layer
- Dependency Injection
- Generic Response
- Generic Pagination

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Framework | FastAPI |
| Language | Python 3.13 |
| ORM | SQLAlchemy 2.0 |
| Validation | Pydantic v2 |
| Database | PostgreSQL |
| Migration | Alembic |
| Authentication | JWT |
| Password Hashing | Passlib |

---

## 🏗 Architecture

```
                Client
                   │
                   ▼
            FastAPI Router
                   │
                   ▼
           Dependency Injection
                   │
                   ▼
              Service Layer
                   │
                   ▼
            Repository Layer
                   │
                   ▼
             SQLAlchemy ORM
                   │
                   ▼
              PostgreSQL
```

---

## 📂 Project Structure

```
backend/
│
├── alembic/
├── app/
│   ├── api/
│   ├── auth/
│   ├── core/
│   ├── database/
│   ├── dependencies/
│   ├── etl/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── seeders/
│   ├── services/
│   └── main.py
│
├── data/
│
├── requirements.txt
├── alembic.ini
└── README.md
```

---

## 🚀 Installation

Clone repository

```bash
git clone <repository-url>
```

Move into project

```bash
cd backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙ Environment Variables

Copy:

```bash
.env.example
```

to

```bash
.env
```

Update your PostgreSQL configuration.

---

## 🗄 Database Migration

Create tables

```bash
alembic upgrade head
```

Create new migration

```bash
alembic revision --autogenerate -m "migration message"
```

---

## 🌏 ETL Workflow

```
BPS API
   │
Downloader
   │
Normalizer
   │
Cleaner
   │
Validator
   │
Exporter
   │
Seeder
   │
Database
```

---

## 🌱 Seed Master Data

```bash
python -m app.scripts.seed_territories
```

---

## ▶ Run API

```bash
uvicorn app.main:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## 🛣 Roadmap

### Phase 1

- [x] Authentication
- [x] Territory Management
- [x] Citizen Module Foundation
- [x] ETL Pipeline
- [x] Database Seeder

### Phase 2

- [ ] Household Management
- [ ] Village Dashboard
- [ ] Statistics
- [ ] Analytics
- [ ] Complaint Module
- [ ] BUMDes Module
- [ ] UMKM Module

### Phase 3

- [ ] Frontend (Next.js)
- [ ] Mobile Responsive Dashboard
- [ ] Public API
- [ ] Deployment

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

---

## 📄 License

This project is released under the MIT License.