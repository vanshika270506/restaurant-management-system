import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import time
ADMIN_PASSWORD_FILE = "admin.txt"
GST_RATE = 0.05   # 5% GST

COUPONS = {
    "FESTIVE10": 0.10,
    "STUDENT5": 0.05
}

# ---------------- FILE INITIALIZATION ----------------
def initialize_files():
    # ---------- PREDEFINED MENU ----------
    if not os.path.exists("menu.csv"):
        menu = pd.DataFrame([
            [1, "Pizza", 250],
            [2, "Burger", 120],
            [3, "Pasta", 180],
            [4, "Sandwich", 100],
            [5, "French Fries", 90],
            [6, "Cold Coffee", 80],
            [7, "Sushi", 999]
        ], columns=["ItemID", "ItemName", "Category", "Price", "Available"])

        menu.to_csv("menu.csv", index=False)

    if not os.path.exists("orders.csv"):
        orders = pd.DataFrame(columns=["Customer", "Item", "Quantity", "Total"])
        orders.to_csv("orders.csv", index=False)

    if not os.path.exists("customers.csv"):
        customers = pd.DataFrame(columns=["Customer", "PreferredItem"])
        customers.to_csv("customers.csv", index=False)


    if not os.path.exists("orders.csv"):
        orders = pd.DataFrame(columns=["Customer", "Item", "Quantity", "Total"])
        orders.to_csv("orders.csv", index=False)

    if not os.path.exists("customers.csv"):
        customers = pd.DataFrame(columns=["Customer", "PreferredItem"]
)
        customers.to_csv("customers.csv", index=False)
    if not os.path.exists("feedback.csv"):
        feedback = pd.DataFrame(columns=["Customer", "Rating", "Comment","AdminReply"])
        feedback.to_csv("feedback.csv", index=False)



initialize_files()

# ---------------- ADMIN FUNCTIONS ----------------
def load_admin_password():
    if not os.path.exists(ADMIN_PASSWORD_FILE):
        with open(ADMIN_PASSWORD_FILE, "w") as f:
            f.write("admin123")   # default password
        return "admin123"

    with open(ADMIN_PASSWORD_FILE, "r") as f:
        return f.read().strip()


def save_admin_password(new_password):
    with open(ADMIN_PASSWORD_FILE, "w") as f:
        f.write(new_password)

def add_menu_item():
    menu = pd.read_csv("menu.csv")

    item_id = len(menu) + 1
    name = input("Enter item name: ")
    price = float(input("Enter price: "))

    menu.loc[len(menu)] = [item_id, name, price]
    menu.to_csv("menu.csv", index=False)

    print("Menu item added successfully!")

def update_menu_item():
    menu = pd.read_csv("menu.csv")
    print(menu)

    item_id = int(input("Enter ItemID to update: "))
    new_price = input("New price (press Enter to skip): ")
    new_name = input("New name (press Enter to skip): ")

    if new_price:
        menu.loc[menu["ItemID"] == item_id, "Price"] = float(new_price)
    if new_name:
        menu.loc[menu["ItemID"] == item_id, "ItemName"] = new_name

    menu.to_csv("menu.csv", index=False)
    print("Menu updated.")
def delete_menu_item():
    menu = pd.read_csv("menu.csv")
    item_id = int(input("Enter ItemID to delete: "))
    menu = menu[menu["ItemID"] != item_id]
    menu.to_csv("menu.csv", index=False)
    print("Item deleted.")
def special_of_day():
    menu = pd.read_csv("menu.csv")
    print("🌟 Special of the Day:")
    print(menu.sample(1))

def view_menu():
    menu = pd.read_csv("menu.csv")
    print("\n------------ MENU ------------")
    print(menu.to_string(index=False))
    print("------------------------------")


def view_all_orders():
    orders = pd.read_csv("orders.csv")
    print("\n----------- ALL ORDERS -----------")
    print(orders.to_string(index=False))
    print("---------------------------------")


def menu_performance():
    orders = pd.read_csv("orders.csv")
    if orders.empty:
        print("No orders yet.")
        return

    performance = orders.groupby("Item")["Quantity"].sum()
    performance.plot(kind="bar", title="Menu Performance",color= "pink")
    plt.xlabel("Item")
    plt.ylabel("Quantity Sold")
    plt.tight_layout()
    plt.show()
def sales_insights():
    orders = pd.read_csv("orders.csv")

    if orders.empty:
        print("No orders yet.")
        return

    top_item = orders.groupby("Item")["Quantity"].sum().idxmax()
    least_item = orders.groupby("Item")["Quantity"].sum().idxmin()

    print(f"\nTop-Selling Item: {top_item}")
    print(f"Least-Selling Item: {least_item}")


def customer_preferences():
    customers = pd.read_csv("customers.csv")

    if customers.empty:
        print("No customer data available.")
        return

    prefs = customers["PreferredItem"].value_counts()

    print("\n------ CUSTOMER PREFERENCES ------")
    for item, count in prefs.items():
        print(f"{item} → Ordered {count} time(s)")
    print("---------------------------------")
def view_feedback():
    feedback = pd.read_csv("feedback.csv")

    if feedback.empty:
        print("No feedback available yet.")
        return

    print("\n---------- CUSTOMER FEEDBACK ----------")
    print(feedback)
    print("-------------------------------------")

    avg_rating = feedback["Rating"].mean()
    print(f"\n⭐ Average Rating: {avg_rating:.2f} / 5")
def reply_feedback():
    feedback = pd.read_csv("feedback.csv")
    print(feedback)

    idx = int(input("Enter feedback index to reply: "))
    reply = input("Enter admin reply: ")

    feedback.at[idx, "AdminReply"] = reply
    feedback.to_csv("feedback.csv", index=False)

    print("Reply saved.")

def change_admin_password():
    current_password = load_admin_password()

    old_pwd = input("Enter current password: ")
    if old_pwd != current_password:
        print("❌ Incorrect current password.")
        return

    new_pwd = input("Enter new password: ")
    confirm_pwd = input("Confirm new password: ")

    if new_pwd != confirm_pwd:
        print("❌ Passwords do not match.")
        return

    if len(new_pwd) < 5:
        print("❌ Password too short (min 5 characters).")
        return

    save_admin_password(new_pwd)
    print("✅ Admin password changed successfully!")
def reply_to_feedback():
    feedback = pd.read_csv("feedback.csv")

    if feedback.empty:
        print("No feedback to reply.")
        return

    print(feedback)

    idx = int(input("Enter feedback index to reply: "))
    reply = input("Enter admin reply: ")

    feedback.at[idx, "AdminReply"] = reply
    feedback.to_csv("feedback.csv", index=False)

    print("Reply saved successfully.")
def update_menu_item():
    menu = pd.read_csv("menu.csv")
    print(menu)

    item_id = int(input("Enter ItemID to update: "))
    if item_id not in menu["ItemID"].values:
        print("Invalid ItemID")
        return

    new_price = float(input("Enter new price: "))
    menu.loc[menu["ItemID"] == item_id, "Price"] = new_price
    menu.to_csv("menu.csv", index=False)

    print("Menu updated successfully.")
def delete_menu_item():
    menu = pd.read_csv("menu.csv")
    print(menu)

    item_id = int(input("Enter ItemID to delete: "))
    menu = menu[menu["ItemID"] != item_id]
    menu.to_csv("menu.csv", index=False)

    print("Item deleted successfully.")




# ---------------- USER FUNCTIONS ----------------
def place_order():
    menu = pd.read_csv("menu.csv")
    if menu.empty:
        print("Menu not available.")
        return

    print(menu.to_string(index=False))

    customer = input("Enter customer name: ")
    item_id = int(input("Enter ItemID: "))
    qty = int(input("Enter quantity: "))

    item = menu.loc[menu["ItemID"] == item_id]
    if item.empty:
        print("Invalid Item ID.")
        return

    item_name = item["ItemName"].values[0]
    price = item["Price"].values[0]
    total = price * qty

    orders = pd.read_csv("orders.csv")
    orders.loc[len(orders)] = [customer, item_name, qty, total]
    orders.to_csv("orders.csv", index=False)

    customers = pd.read_csv("customers.csv")
    customers.loc[len(customers)] = [customer, item_name]
    customers.to_csv("customers.csv", index=False)

    print(f"\nOrder placed: {item_name} x {qty}")
    print(f"Total Amount: ₹{total}")


def generate_bill():
    name = input("Enter customer name: ")
    orders = pd.read_csv("orders.csv")
    menu = pd.read_csv("menu.csv")

    cust_orders = orders[orders["Customer"] == name]

    if cust_orders.empty:
        print("No orders found.")
        return

    bill = cust_orders.merge(
        menu,
        left_on="Item",
        right_on="ItemName",
        how="left"
    )

    subtotal = np.sum(bill["Price"] * bill["Quantity"])
    gst = subtotal * GST_RATE

    coupon = input("Enter coupon code (or press Enter): ").upper()
    discount = 0

    if coupon in COUPONS:
        discount = subtotal * COUPONS[coupon]
        print(f"Coupon applied: -₹{discount:.2f}")

    total = subtotal + gst - discount
    

    payment = input("Payment Mode (Cash / UPI / Card): ")

    receipt_id = f"R{int(time.time())}"

    print("\n------------ BILL ------------")
    print(bill[["Item", "Price", "Quantity"]])
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"GST (5%): ₹{gst:.2f}")
    print(f"Discount: ₹{discount:.2f}")
    print(f"Total Payable: ₹{total:.2f}")
    print(f"Payment Mode: {payment}")
    print(f"Receipt ID: {receipt_id}")
    print("------------------------------")

def give_feedback():
    customer = input("Enter your name: ")
    
    rating = int(input("Rate us (1 to 5): "))
    if rating < 1 or rating > 5:
        print("Invalid rating. Please give between 1 and 5.")
        return

    comment = input("Write your feedback: ")

    feedback = pd.read_csv("feedback.csv")
    feedback.loc[len(feedback)] = [customer, rating, comment]
    feedback.to_csv("feedback.csv", index=False)

    print("\nThank you for your feedback! 😊")


# ---------------- PORTALS ----------------
def admin_login():
    admin_password = load_admin_password()
    attempts = 3

    while attempts > 0:
        pwd = input("Enter admin password: ")

        if pwd == admin_password:
            print("\nLogin successful! ✅")
            admin_portal()
            return
        else:
            attempts -= 1
            print(f"Wrong password ❌ Attempts left: {attempts}")

    print("Too many failed attempts. Access denied 🚫")

def admin_portal():
    while True:
        print("\n=========== ADMIN PORTAL ===========")
        print("1. Add Menu Item")
        print("2. View Menu")
        print("3. View All Orders")
        print("4. Menu Performance Graph")
        print("5. Customer Preferences")
        print("6. View Feedback")
        print("7. Change Admin Password")
        print("8. Sales Insights")
        print("9. Reply to Feedback")
        print("0. Logout")

        ch = input("Enter choice: ")

        if ch == "1":
            add_menu_item()
        elif ch == "2":
            view_menu()
        elif ch == "3":
            view_all_orders()
        elif ch == "4":
            menu_performance()
        elif ch == "5":
            customer_preferences()
        elif ch == "6":
            view_feedback()
        elif ch == "7":
         change_admin_password()
        elif ch == "8":
         sales_insights()
        elif ch == "9":
          reply_feedback()


        elif ch == "0":
            break
        else:
            print("Invalid choice")


def user_portal():
    while True:
        print("\n=========== USER PORTAL ===========")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Generate Bill")
        print("4. Give Feedback")
        print("0. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            view_menu()
        elif ch == "2":
            place_order()
        elif ch == "3":
            generate_bill()
        elif ch == "4":
          give_feedback()

        elif ch == "0":

            break
        else:
            print("Invalid choice")


# ---------------- MAIN PROGRAM ----------------
while True:
    print("\n====================================")
    print("   THE LILAC RESTAURANT   ")
    print("====================================")
    print("1. Admin Login")
    print("2. User Login")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
       admin_login()
    elif choice == "2":
        user_portal()
    elif choice == "0":
        print("Thank you for visiting!")
        break
    else:
        print("Invalid choice")