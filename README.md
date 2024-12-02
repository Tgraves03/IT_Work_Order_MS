IT Work Order Management System

Project Overview

The IT Work Order Management System is a Python-based command-line application designed to log, manage, and track IT-related work orders. This system supports user registration, login, work order creation, viewing, and status updates. It also features role-based access control, where admins and users have different levels of access to work orders.

The application provides an efficient way for IT departments to organize, track, and resolve work orders, making it easier to manage day-to-day IT support tasks.

Features

User Registration and Login Users can create an account and log in securely with password hashing for enhanced security. Two roles are available for users: admin and user.

Work Order Management Users can create new work orders, including details such as title, description, and priority. Admins and users can update the status of work orders (e.g., Open, In Progress, Resolved). Users can view all the work orders in the system, giving them transparency on the work being done.

Database Data is stored using SQLite, providing persistence for user information and work orders. Role-Based Access Admins can view, create, and update all work orders. Users can only create work orders and view their own. Tech Stack

Language: Python 3.x
Database: SQLite
Libraries: sqlite3 for database operations. hashlib for password hashing and secure authentication.

Installation Prerequisites Ensure that Python 3.x is installed on your system. If it is not already installed, you can download Python from the official website: python.org.

    Setting Up the Project
        Clone the repository:
        
        Install dependencies: This project uses only Python's built-in libraries, so there are no additional packages to install.
        
        Initialize the database: Run the following command to initialize the database tables:       
            This will set up the necessary database (work_order.db) with the required users and work_orders tables.
Running the Application

Once everything is set up, you can run the system by executing the main.py file: This will launch the command-line interface where you can:
    Register a new user.
    Log in as an existing user.
    Manage work orders by creating, updating, and viewing them.
How to Use the Application

Registration: To use the system, users must first register with a username, password, and role (admin or user).
    
Login: After registration, users can log in using their username and password. Upon successful login, users will be able to manage work orders based on their role.

Work Order Management: 
    After logging in, users can:
        1. Create Work Orders: Provide a title, description, and priority for the work order.
        2. View Work Orders: See a list of all work orders.
        3. Update Work Orders: Change the status of a work order (e.g., In Progress, Resolved).
File Structure

Here’s a breakdown of the key files in the project and their functions:
     main.py: This file contains the main program logic. It handles user registration, login, and the work order management workflow.
    
     database.py: Contains the functions that initialize the database and manage connections to the SQLite database.

    users.py: Manages user registration, login, and password hashing for secure authentication.

    work_order.py: Contains functions to create, list, and update work orders, as well as interact with the work_orders table in the database.
Troubleshooting

Common Issues

    Database connection issues: Ensure the work_order.db file is in the project directory. If it’s missing, run python main.py again to initialize the database.

    Login errors: Ensure that the correct username and password combination is used. Passwords are stored in a hashed format, so ensure the correct hash is entered.
Error Handling

If any issues arise during user input or database operations, the program will provide a descriptive error message and ask the user to try again.
Future Improvements

Web Interface: Consider using Flask or Django to create a web-based interface for the system, making it more user-friendly and accessible.

Email Notifications: Implement email notifications for users when the status of their work orders changes.

Advanced Role Management: Add more user roles (e.g., manager) with different permissions.

Analytics: Track and display work order resolution times and other performance metrics.

License

This project is licensed under the MIT License - see the LICENSE file for details.
