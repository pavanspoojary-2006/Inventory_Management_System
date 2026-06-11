from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="inventory_management",
    autocommit=True
)


# ==========================
# DASHBOARD
# ==========================

@app.route("/")
def index():

    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM Product")
    products = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Supplier")
    suppliers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Warehouse")
    warehouses = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(quantity) FROM Stock")
    stock = cursor.fetchone()[0] or 0

    return render_template(
        "index.html",
        products=products,
        suppliers=suppliers,
        warehouses=warehouses,
        stock=stock
    )


# ==========================
# PRODUCTS
# ==========================

@app.route("/products")
def products():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM Product")

    products = cursor.fetchall()

    return render_template(
        "products.html",
        products=products
    )


@app.route("/add_product", methods=["POST"])
def add_product():

    name = request.form["name"]
    category = request.form["category"]
    price = request.form["price"]

    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO Product
        (name, category, price)
        VALUES (%s,%s,%s)
    """, (name, category, price))

    return redirect("/products")


@app.route("/delete_product/<int:id>")
def delete_product(id):

    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM Product WHERE product_id=%s",
        (id,)
    )

    return redirect("/products")


# ==========================
# SUPPLIERS
# ==========================

@app.route("/suppliers")
def suppliers():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM Supplier")

    suppliers = cursor.fetchall()

    return render_template(
        "suppliers.html",
        suppliers=suppliers
    )


@app.route("/add_supplier", methods=["POST"])
def add_supplier():

    name = request.form["name"]
    phone = request.form["phone"]
    address = request.form["address"]

    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO Supplier
        (name, phone, address)
        VALUES (%s,%s,%s)
    """, (name, phone, address))

    return redirect("/suppliers")


@app.route("/delete_supplier/<int:id>")
def delete_supplier(id):

    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM Supplier WHERE supplier_id=%s",
        (id,)
    )

    return redirect("/suppliers")


# ==========================
# WAREHOUSE
# ==========================

@app.route("/warehouse")
def warehouse():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM Warehouse")

    warehouses = cursor.fetchall()

    return render_template(
        "warehouse.html",
        warehouses=warehouses
    )


@app.route("/add_warehouse", methods=["POST"])
def add_warehouse():

    location = request.form["location"]

    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO Warehouse(location)
        VALUES(%s)
    """, (location,))

    return redirect("/warehouse")


@app.route("/delete_warehouse/<int:id>")
def delete_warehouse(id):

    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM Warehouse WHERE warehouse_id=%s",
        (id,)
    )

    return redirect("/warehouse")


# ==========================
# PURCHASE
# ==========================

@app.route("/purchase")
def purchase():

    cursor = db.cursor()

    cursor.execute("""
        SELECT
        p.purchase_id,
        s.name,
        pr.name,
        p.quantity,
        p.purchase_date
        FROM Purchase p
        JOIN Supplier s
        ON p.supplier_id=s.supplier_id
        JOIN Product pr
        ON p.product_id=pr.product_id
    """)

    purchases = cursor.fetchall()

    cursor.execute("SELECT * FROM Supplier")
    suppliers = cursor.fetchall()

    cursor.execute("SELECT * FROM Product")
    products = cursor.fetchall()

    return render_template(
        "purchase.html",
        purchases=purchases,
        suppliers=suppliers,
        products=products
    )


@app.route("/add_purchase", methods=["POST"])
def add_purchase():

    supplier_id = request.form["supplier_id"]
    product_id = request.form["product_id"]
    quantity = request.form["quantity"]
    purchase_date = request.form["purchase_date"]

    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO Purchase
        (supplier_id, product_id, quantity, purchase_date)
        VALUES(%s,%s,%s,%s)
    """, (
        supplier_id,
        product_id,
        quantity,
        purchase_date
    ))

    return redirect("/purchase")


# ==========================
# SALES
# ==========================

@app.route("/sales")
def sales():

    cursor = db.cursor()

    cursor.execute("""
        SELECT
        s.sales_id,
        p.name,
        s.quantity,
        s.selling_price,
        s.sales_date
        FROM Sales s
        JOIN Product p
        ON s.product_id=p.product_id
    """)

    sales = cursor.fetchall()

    cursor.execute("SELECT * FROM Product")
    products = cursor.fetchall()

    return render_template(
        "sales.html",
        sales=sales,
        products=products
    )


@app.route("/add_sale", methods=["POST"])
def add_sale():

    product_id = request.form["product_id"]
    quantity = request.form["quantity"]
    sales_date = request.form["sales_date"]
    selling_price = request.form["selling_price"]

    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO Sales
        (product_id, quantity, sales_date, selling_price)
        VALUES(%s,%s,%s,%s)
    """, (
        product_id,
        quantity,
        sales_date,
        selling_price
    ))

    return redirect("/sales")


# ==========================
# STOCK
# ==========================

@app.route("/stock")
def stock():

    cursor = db.cursor()

    cursor.execute("""
        SELECT
        p.name,
        w.location,
        s.quantity
        FROM Stock s
        JOIN Product p
        ON p.product_id=s.product_id
        JOIN Warehouse w
        ON w.warehouse_id=s.warehouse_id
    """)

    stock = cursor.fetchall()

    return render_template(
        "stock.html",
        stock=stock
    )


if __name__ == "__main__":
    app.run(debug=True)