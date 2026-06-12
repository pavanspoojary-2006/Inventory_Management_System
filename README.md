Inventory Management System

Overview

Inventory Management System is a full-stack web application developed using Flask and MySQL for managing products, suppliers, warehouses, purchases, sales, and stock information. The system provides a centralized platform to track inventory operations efficiently through an intuitive dashboard and management modules.

This project was developed as part of a Database Management Systems (DBMS) academic project and demonstrates the integration of frontend, backend, and database technologies.

---

Features

Dashboard

- View total number of products
- View total number of suppliers
- View total number of warehouses
- View total stock units available
- Interactive management dashboard

Product Management

- Add new products
- View product details
- Delete products
- Manage product categories and pricing

Supplier Management

- Add suppliers
- View supplier information
- Delete suppliers
- Manage supplier contact details

Warehouse Management

- Add warehouse locations
- View warehouse records
- Delete warehouses
- Manage inventory storage locations

Purchase Management

- Record product purchases
- Track supplier transactions
- Maintain purchase history

Sales Management

- Record product sales
- Track sales transactions
- Maintain sales history

Stock Management

- View stock availability
- Monitor inventory across warehouses
- Track product quantities

---

Technology Stack

Frontend

- HTML5
- CSS3
- JavaScript

Backend

- Python
- Flask Framework

Database

- MySQL

---

Database Schema

Product

Field| Description
product_id| Unique Product ID
name| Product Name
category| Product Category
price| Product Price

Supplier

Field| Description
supplier_id| Unique Supplier ID
name| Supplier Name
phone| Contact Number
address| Supplier Address

Warehouse

Field| Description
warehouse_id| Unique Warehouse ID
location| Warehouse Location

Purchase

Field| Description
purchase_id| Purchase ID
supplier_id| Supplier Reference
product_id| Product Reference
quantity| Purchased Quantity
purchase_date| Purchase Date

Sales

Field| Description
sales_id| Sales ID
product_id| Product Reference
quantity| Sold Quantity
sales_date| Sales Date
selling_price| Selling Price

Stock

Field| Description
stock_id| Stock ID
product_id| Product Reference
warehouse_id| Warehouse Reference
quantity| Available Quantity

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

Installation and Setup

1. Clone the Repository

git clone https://github.com/pavanspoojary-2006/Inventory_Management_System.git
cd Inventory_Management_System

2. Create a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate

3. Install Required Packages

pip install flask pymysql

4. Configure MySQL Database

Create a database:

CREATE DATABASE inventory_management;

Import the required tables and sample data into the database.

Update database credentials in "server.py" if necessary.

5. Run the Application

python3 server.py

Open your browser and visit:

http://127.0.0.1:5000

---

Learning Outcomes

- Database design and normalization
- SQL query implementation
- Flask web development
- Frontend and backend integration
- CRUD operations
- Inventory tracking systems
- Full-stack application development

---

Future Enhancements

- User authentication and authorization
- Role-based access control
- Inventory analytics dashboard
- PDF report generation
- Barcode and QR code integration
- Search and filtering functionality
- REST API integration
- Cloud deployment support

---

Author

Pavan S Poojary 
4MW24AD026
Artificial Intelligence and Data Science

---

License

This project is intended for educational, academic, and learning purposes.