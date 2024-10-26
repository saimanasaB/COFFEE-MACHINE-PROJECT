#coffee_db
import sqlite3

# Database connection
def connect_db():
    conn = sqlite3.connect("coffee_machine.db")
    return conn

# Initialize tables
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Table for coffee orders
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_name TEXT,
                        coffee_type TEXT,
                        sugar_level TEXT,
                        order_status TEXT
                    )''')

    # Table for inventory
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                        coffee_type TEXT PRIMARY KEY,
                        quantity INTEGER
                    )''')

    conn.commit()
    conn.close()

# Add coffee order
def add_order(customer_name, coffee_type, sugar_level, order_status="Pending"):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (customer_name, coffee_type, sugar_level, order_status) VALUES (?, ?, ?, ?)",
                   (customer_name, coffee_type, sugar_level, order_status))
    conn.commit()
    conn.close()

# Update order status
def update_order_status(order_id, status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE orders SET order_status = ? WHERE order_id = ?", (status, order_id))
    conn.commit()
    conn.close()

# Get all orders
def get_orders():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return orders

# Add inventory
def add_inventory(coffee_type, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO inventory (coffee_type, quantity) VALUES (?, ?)", (coffee_type, quantity))
    conn.commit()
    conn.close()

# Get inventory details
def get_inventory():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    inventory = cursor.fetchall()
    conn.close()
    return inventory
