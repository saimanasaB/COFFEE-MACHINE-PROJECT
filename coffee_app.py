#coffee_app
import streamlit as st
import pandas as pd
from coffee_db import create_tables, add_order, get_orders, add_inventory, get_inventory, update_order_status

# Initialize the database tables
create_tables()

# Title of the app
st.title("Coffee Machine Management System")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Order Coffee", "Manage Inventory", "View Orders"])

# Page 1: Order Coffee
if page == "Order Coffee":
    st.header("Order Coffee")

    customer_name = st.text_input("Enter your name")
    coffee_type = st.selectbox("Select Coffee Type", ["Espresso", "Latte", "Cappuccino"])
    sugar_level = st.slider("Select Sugar Level", 0, 5, 2)

    if st.button("Place Order"):
        add_order(customer_name, coffee_type, sugar_level)
        st.success(f"Order placed for {customer_name}!")

# Page 2: Manage Inventory
elif page == "Manage Inventory":
    st.header("Manage Inventory")

    coffee_type = st.selectbox("Select Coffee Type", ["Espresso", "Latte", "Cappuccino"])
    quantity = st.number_input("Quantity", min_value=0, step=1)

    if st.button("Update Inventory"):
        add_inventory(coffee_type, quantity)
        st.success(f"Updated inventory for {coffee_type}")

    # Display inventory
    st.subheader("Current Inventory")
    inventory = get_inventory()
    inventory_df = pd.DataFrame(inventory, columns=["Coffee Type", "Quantity"])
    st.table(inventory_df)

# Page 3: View Orders
elif page == "View Orders":
    st.header("View Orders")
    
    orders = get_orders()
    orders_df = pd.DataFrame(orders, columns=["Order ID", "Customer Name", "Coffee Type", "Sugar Level", "Order Status"])
    st.table(orders_df)

    # Update order status
    order_id = st.number_input("Enter Order ID to update status", min_value=1, step=1)
    new_status = st.selectbox("Select new status", ["Pending", "Completed", "Cancelled"])
    
    if st.button("Update Status"):
        update_order_status(order_id, new_status)
        st.success(f"Updated order {order_id} to {new_status}")
