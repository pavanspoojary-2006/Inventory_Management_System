# Inventory Management System

## Overview

Inventory Management System is a full-stack web application developed using Flask and MySQL to manage products, suppliers, warehouses, purchases, sales, and stock records efficiently.

The system provides a centralized dashboard for monitoring inventory statistics and enables users to manage inventory operations through an intuitive web interface.

---

## Features

### Dashboard
- View total number of products
- View total number of suppliers
- View total number of warehouses
- View total available stock units

### Product Management
- Add new products
- View all products
- Delete products
- Manage product details including category and price

### Supplier Management
- Add new suppliers
- View supplier information
- Delete suppliers
- Store supplier contact details

### Warehouse Management
- Add warehouses
- View warehouse locations
- Delete warehouses
- Manage storage locations

### Purchase Management
- Record product purchases
- Track supplier transactions
- Maintain purchase history

### Sales Management
- Record product sales
- Track sales transactions
- Maintain sales history

### Stock Management
- Monitor inventory levels
- View stock distribution across warehouses
- Track product quantities

---

## Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Database
- MySQL

---

## Database Schema

### Supplier
| Field | Type |
|---------|---------|
| supplier_id | INT |
| name | VARCHAR |
| phone | VARCHAR |
| address | VARCHAR |

### Product
| Field | Type |
|---------|---------|
| product_id | INT |
| name | VARCHAR |
| category | VARCHAR |
| price | DECIMAL |

### Purchase
| Field | Type |
|---------|---------|
| purchase_id | INT |
| supplier_id | INT |
| product_id | INT |
| quantity | INT |
| purchase_date | DATE |

### Sales
| Field | Type |
|---------|---------|
| sales_id | INT |
| product_id | INT |
| quantity | INT |
| sales_date | DATE |
| selling_price | DECIMAL |

### Warehouse
| Field | Type |
|---------|---------|
| warehouse_id | INT |
| location | VARCHAR |

### Stock
| Field | Type |
|---------|---------|
| stock_id | INT |
| product_id | INT |
| warehouse_id | INT |
| quantity | INT |

---

## Project Structure

text Inventory_Management_System/ │ ├── server.py │ ├── templates/ │   ├── index.html │   ├── products.html │   ├── suppliers.html │   ├── purchase.html │   ├── sales.html │   ├── warehouse.html │   └── stock.html │ ├── static/ │   ├── style.css │   └── script.js │ └── README.md 

---

## Installation and Setup

### 1. Clone the Repository

bash git clone https://github.com/pavanspoojary-2006/Inventory_Management_System.git cd Inventory_Management_System 

### 2. Create Virtual Environment

bash python3 -m venv .venv source .venv/bin/activate 

### 3. Install Dependencies

bash pip install flask pymysql 

### 4. Configure MySQL Database

Create a database:

sql CREATE DATABASE inventory_management; 

Import the required tables and sample data into the database.

Update database credentials in server.py if necessary.

### 5. Run the Application

bash python3 server.py 

### 6. Open in Browser

text http://127.0.0.1:5000 

---

## Screenshots

### Dashboard
Add project screenshots here.

### Products Page
Add project screenshots here.

### Suppliers Page
Add project screenshots here.

### Warehouse Page
Add project screenshots here.

### Stock Page
Add project screenshots here.

---

## Learning Outcomes

This project demonstrates:

- Database design and normalization
- CRUD operations using Flask and MySQL
- Frontend development with HTML, CSS, and JavaScript
- Backend development using Flask
- Dynamic data rendering using Jinja Templates
- Full-stack web application development

---

## Future Enhancements

- User authentication and authorization
- Role-based access control
- Search and filtering functionality
- Inventory alerts and notifications
- Export reports to PDF and Excel
- Data visualization and analytics dashboard

---

## Author

Pawan S

Bachelor of Engineering (B.E.)  
Artificial Intelligence and Data Science

---

## License

This project was developed for educational and academic purposes.
