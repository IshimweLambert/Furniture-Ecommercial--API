# 🪑 Furniture E-Commerce Backend API

## 📌 Project Overview
This project is a **Furniture E-Commerce Backend API** built using **Django** and **Django REST Framework (DRF)**.  
It provides a robust backend system for managing users, products, carts, orders, and reviews for an online furniture store.

The system follows **RESTful API principles**, uses **MySQL** as the database, and is designed with **scalability, security, and clean architecture** in mind.

---

## 🎯 Project Objectives
- Build a real-world backend for an e-commerce platform
- Apply Django ORM with MySQL for database management
- Implement clean relational data models based on an ERD
- Practice backend architecture used in production systems
- Prepare a capstone-level project suitable for academic defense

---

## 🛠️ Technologies Used

| Technology | Purpose |
|----------|--------|
| Django | Backend framework |
| Django REST Framework | API development |
| MySQL | Relational database |
| MySQL Workbench | Database visualization & management |
| Python | Programming language |
| Virtual Environment (venv) | Dependency isolation |

---

## 🏗️ Project Architecture

The project is divided into multiple Django apps for **separation of concerns**:
furniture_ecommerce/
│
├── accounts/ → Custom user & authentication
├── products/ → Furniture product management
├── cart/ → Shopping cart functionality
├── orders/ → Orders & order items
├── reviews/ → Product reviews & ratings
│
├── config/ → Project settings & URLs
└── manage.py

---

## 👤 User Management (Custom User Model)

A **custom User model** is implemented using `AbstractUser` to support **role-based access control**.

### User Roles
- **Admin**: Manage products and orders
- **Customer**: Browse products, place orders, leave reviews

```python
class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=[('admin', 'Admin'), ('customer', 'Customer')],
        default='customer'
    )
This approach ensures:

Scalability

Secure authorization

Flexibility for future roles

🛒 Product Management

The Product model stores furniture details such as:

Name

Description

Price

Stock quantity

Image

Creation timestamp

Each product can have multiple reviews and can be added to carts and orders.

🛍️ Cart System

The cart system uses two models:

Cart → linked one-to-one with a user

CartItem → junction table between Cart and Product

This design:

Resolves many-to-many relationships

Allows quantity tracking

Supports scalable cart operations

📦 Order Management

Orders are stored using:

Order → overall order details

OrderItem → individual products in an order

Each order includes:

User

Status (pending, paid, shipped, delivered)

Total price

Timestamp

Order items store product price at purchase time to preserve historical accuracy.

⭐ Review System

Customers can leave reviews for products:

Rating

Comment

Timestamp

Each review is linked to:

One user

One product

This ensures data integrity and prevents orphaned reviews.

🗄️ Database Design (MySQL)

Database: MySQL

Managed using MySQL Workbench

Tables are automatically created using Django ORM migrations

Relationships are enforced using foreign keys

Why MySQL?

Strong relational integrity

High performance

Widely used in production systems

🔁 Data Flow (How Data Is Stored)

API request sent from frontend

Django REST Framework validates data

Django ORM translates Python objects to SQL

MySQL stores data in relational tables

Response returned as JSON

🔐 Authentication & Security (Planned)

Django authentication system

Role-based authorization

Secure password hashing

Admin-only endpoints for management tasks

🚀 Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/furniture-ecommerce-backend.git
cd furniture-ecommerce-backend

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install django djangorestframework mysqlclient

4️⃣ Configure MySQL Database

Create database in MySQL Workbench:

CREATE DATABASE furniture_db;


Update settings.py with database credentials.

5️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Create Admin User
python manage.py createsuperuser

7️⃣ Run Server
python manage.py runserver


Access admin panel:

http://127.0.0.1:8000/admin

📚 Future Enhancements

JWT authentication

Product search & filtering

Pagination

Payment integration

API documentation (Swagger)

Deployment on cloud platform

🎓 Academic Value

This project demonstrates:

Backend system design

Relational database modeling

RESTful API development

Clean architecture

Real-world e-commerce logic

It is suitable for capstone defense, portfolio, and job applications.

👨‍💻 Author

Ishimwe Lambert
Backend Developer | Django | MySQL

📄 License

This project is for educational purposes.
