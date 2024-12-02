#This is the entry point of the program, where the user interacts 
#with the system. It provides a menu for user registration, login, 
#and performing work order management tasks.
#Programmer: Trevone Graves
#Date: 12-1-2024

from database import initialize_db
from users import register_user, login_user
from work_order import create_work_order, list_work_orders, update_work_order_status

def main():
    initialize_db()

    print("Welcome to IT Work Order Management System!")
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            role = input("Enter role (admin/user): ").lower()
            register_user(username, password, role)
            print("Registration successful!")

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = login_user(username, password)

            if user:
                print(f"Welcome, {user[1]}!")
                while True:
                    print("\n1. Create Work Order")
                    print("2. View Work Orders")
                    print("3. Update Work Order Status")
                    print("4. Logout")
                    action = input("Choose an option: ")

                    if action == '1':
                        title = input("Enter the title: ")
                        description = input("Enter the description: ")
                        priority = input("Enter the priority (Low/Medium/High): ")
                        create_work_order(title, description, priority)
                        print("Work order created successfully!")

                    elif action == '2':
                        orders = list_work_orders()
                        for order in orders:
                            print(order)

                    elif action == '3':
                        order_id = int(input("Enter work order ID: "))
                        new_status = input("Enter new status (Open/In Progress/Resolved): ")
                        update_work_order_status(order_id, new_status)
                        print("Work order updated successfully!")

                    elif action == '4':
                        print("Logged Out!")
                        break

                    else:
                        print("Invalid choice! Please try again.")
            else:
                print("Invalid login credentials! Please try again.")

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
