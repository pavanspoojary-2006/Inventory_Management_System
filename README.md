Inventory Management System

Overview

The Inventory Management System is a full-stack web application developed using Flask, MySQL, HTML, CSS, and JavaScript. The system provides a centralized platform for managing products, suppliers, warehouses, purchases, sales, and inventory stock levels.

The application is designed to simplify inventory operations by providing an intuitive dashboard and efficient management tools for inventory-related activities.

---

Features

Dashboard

- Display total number of products
- Display total number of suppliers
- Display total number of warehouses
- Display total available stock units
- Quick navigation to all management modules

Product Management

- Add new products
- View product details
- Manage product information
- Delete products

Supplier Management

- Add new suppliers
- View supplier information
- Manage supplier records
- Delete suppliers

Warehouse Management

- Add warehouse locations
- View warehouse information
- Manage warehouse records
- Delete warehouses

Purchase Management

- Record product purchases
- Track purchase history
- Maintain supplier-product relationships

Sales Management

- Record product sales
- Track sales history
- Monitor product movement

Stock Management

- View stock availability
- Monitor inventory across warehouses
- Track product quantities by location

---

Technology Stack

Frontend

- HTML5
- CSS3
- JavaScript

Backend

- Python
- Flask

Database

- MySQL

---

Database Schema

Supplier

Column| Description
supplier_id| Unique supplier identifier
name| Supplier name
phone| Contact number
address| Supplier address

Product

Column| Description
product_id| Unique product identifier
name| Product name
category| Product category
price| Product price

Purchase

Column| Description
purchase_id| Unique purchase identifier
supplier_id| Supplier reference
product_id| Product reference
quantity| Purchased quantity
purchase_date| Purchase date

Sales

Column| Description
sales_id| Unique sales identifier
product_id| Product reference
quantity| Sold quantity
sales_date| Sales date
selling_price| Selling price

Warehouse

Column| Description
warehouse_id| Unique warehouse identifier
location| Warehouse location

Stock

Column| Description
stock_id| Unique stock identifier
product_id| Product reference
warehouse_id| Warehouse reference
quantity| Available quantity

---

Installation

1. Clone the Repository

git clone https://github.com/pavanspoojary-2006/Inventory_Management_System.git
cd Inventory_Management_System

2. Create a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies

pip install flask pymysql

4. Configure MySQL Database

Create the database:

CREATE DATABASE inventory_management;

Import the required tables and sample records into the database.

5. Run the Application

python3 server.py

Open the application in your browser:

http://127.0.0.1:5000

---

Project Structure

Inventory_Management_System/
│
├── server.py
│
├── templates/
│   ├── index.html
│   ├── products.html
│   ├── suppliers.html
│   ├── purchase.html
│   ├── sales.html
│   ├── warehouse.html
│   └── stock.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md

---

Application Modules

- Dashboard
- Product Management
- Supplier Management
- Warehouse Management
- Purchase Management
- Sales Management
- Stock Management

---

Future Enhancements

- User authentication and authorization
- Inventory alerts and notifications
- Data export to Excel and PDF
- Advanced reporting and analytics
- Search and filtering functionality
- Responsive mobile interface
- Cloud deployment support

---

Author

Pawan S

Bachelor of Engineering (B.E.)
Artificial Intelligence and Data Science

---

License

This project is developed for educational and academic purposes.