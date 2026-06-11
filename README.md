# Inventory Management System

A full-stack Inventory Management System developed using Flask, MySQL, HTML, CSS, and JavaScript.

## Features

### Dashboard
- Total Products
- Total Suppliers
- Total Warehouses
- Total Stock Units

### Product Management
- Add Product
- View Products
- Delete Product

### Supplier Management
- Add Supplier
- View Suppliers
- Delete Supplier

### Warehouse Management
- Add Warehouse
- View Warehouses
- Delete Warehouse

### Purchase Management
- Add Purchase Records
- View Purchase History

### Sales Management
- Add Sales Records
- View Sales History

### Stock Management
- View Product Stock Across Warehouses

## Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python Flask

### Database
- MySQL

## Database Tables

### Supplier
- supplier_id
- name
- phone
- address

### Product
- product_id
- name
- category
- price

### Purchase
- purchase_id
- supplier_id
- product_id
- quantity
- purchase_date

### Sales
- sales_id
- product_id
- quantity
- sales_date
- selling_price

### Warehouse
- warehouse_id
- location

### Stock
- stock_id
- product_id
- warehouse_id
- quantity

## Installation

### Clone Repository

bash git clone https://github.com/yourusername/inventory-management-system.git cd inventory-management-system 

### Create Virtual Environment

bash python3 -m venv .venv source .venv/bin/activate 

### Install Dependencies

bash pip install flask pymysql 

### Configure MySQL

Create database:

sql CREATE DATABASE inventory_management; 

Import tables and sample data.

### Run Application

bash python3 server.py 

Open:

text http://127.0.0.1:5000 

## Project Structure

text Inventory_Management_System/ │ ├── server.py │ ├── templates/ │   ├── index.html │   ├── products.html │   ├── suppliers.html │   ├── purchase.html │   ├── sales.html │   ├── warehouse.html │   └── stock.html │ ├── static/ │   ├── style.css │   └── script.js │ └── README.md 

## Author

Pawan S

BE – Artificial Intelligence and Data Science

## License

This project is developed for educational and academic purposes.