# 🥖 Mini Bakery Management System

A comprehensive Python-based bakery management system with role-based access control, inventory management, order processing, and financial reporting capabilities.

## 📋 Table of Contents
- [Features](#features)
- [System Architecture](#system-architecture)
- [User Roles](#user-roles)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [CSV Data Files](#csv-data-files)
- [Contributing](#contributing)

## ✨ Features

### 🔐 Authentication & User Management
- Secure login system with password validation
- Role-based access control (Manager, Customer, Cashier, Baker)
- Account creation for customers
- Employee account management (Manager only)
- Last login tracking

### 👥 User Roles & Capabilities

#### 🏢 Manager
- **System Administration**: Create and manage employee accounts
- **Account Management**: View, modify, and delete user accounts
- **Recipe Management**: Approve/reject baker recipe requests
- **Inventory Control**: Manage ingredients and products
- **Financial Reports**: View sales, expenses, and profit analysis
- **Product Management**: Add, modify, and delete products
- **Equipment Reports**: Track bakery equipment status

#### 🛒 Customer
- **Product Browsing**: View available bakery products with details
- **Shopping Cart**: Add/remove items, manage quantities
- **Order Placement**: Place orders with automatic total calculation
- **Order History**: View past orders and spending
- **Account Management**: Update personal information

#### 💰 Cashier
- **Product Management**: View and modify product information
- **Discount Management**: Apply and manage product discounts
- **Order Processing**: Handle customer transactions
- **Inventory Monitoring**: Check product availability

#### 👨‍🍳 Baker
- **Recipe Management**: Create new recipe requests
- **Recipe Modification**: Request changes to existing recipes
- **Production Planning**: View pending recipes and requirements

### 📊 Data Management
- **CSV-based Storage**: All data stored in structured CSV files
- **Inventory Tracking**: Real-time ingredient and product monitoring
- **Order Management**: Complete order lifecycle tracking
- **Financial Reporting**: Automated expense and revenue calculation
- **Equipment Monitoring**: Track bakery equipment status

## 🏗️ System Architecture

The system follows a modular design with clear separation of concerns:

- **Main Program**: `Assignment Bakery(MainProgram).py` - Core application logic
- **Helper Functions**: `adhocBakerFunctions.py` - Utility functions for CSV operations, validation, and formatting
- **Data Storage**: CSV files for persistent data storage

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only built-in Python libraries)

### Setup
1. Clone or download the repository
2. Ensure all files are in the same directory
3. Run the main program:
```bash
python "Assignment Bakery(MainProgram).py"
```

## 💻 Usage

### Starting the Application
```bash
python "Assignment Bakery(MainProgram).py"
```

### Default Login Credentials
The system comes with pre-configured accounts:

**Manager Account:**
- Username: `test123`
- Password: `Testing123`

**Cashier Account:**
- Username: `XinMin`
- Password: `1WantSleep`

**Baker Account:**
- Username: `Raj123`
- Password: `rajenG@y5`

**Customer Accounts:**
- Various customer accounts available (see `List_Account.csv`)

### Navigation
- Use numbered menu options to navigate
- Type `#exit` or `#cancel` to return to previous menus
- Follow on-screen prompts for data entry

## 📁 File Structure

```
Mini Bakery Program/
├── Assignment Bakery(MainProgram).py    # Main application
├── adhocBakerFunctions.py               # Helper functions
├── List_Account.csv                     # User accounts
├── List_Product.csv                     # Product catalog
├── List_Order.csv                       # Order history
├── List_Expenses.csv                    # Business expenses
├── Inventory_Ingredient.csv             # Ingredient inventory
├── Inventory_Product.csv                # Product inventory
├── Pending_Recipe.csv                   # Recipe requests
├── Report_Equipment.csv                 # Equipment status
├── Report_Finance.csv                   # Financial reports
└── Report_Product.csv                   # Product reports
```

## 📊 CSV Data Files

### Core Data Files
- **`List_Account.csv`**: User credentials, roles, and profile information
- **`List_Product.csv`**: Product catalog with prices and descriptions
- **`List_Order.csv`**: Complete order transaction history
- **`List_Expenses.csv`**: Business expense tracking

### Inventory Management
- **`Inventory_Ingredient.csv`**: Raw ingredient stock levels
- **`Inventory_Product.csv`**: Finished product inventory

### Operations & Reports
- **`Pending_Recipe.csv`**: Baker recipe requests awaiting approval
- **`Report_Equipment.csv`**: Equipment maintenance and status
- **`Report_Finance.csv`**: Financial performance metrics
- **`Report_Product.csv`**: Product performance analytics

## 🔧 Key Features Explained

### Password Security
- Minimum 8 characters, maximum 20 characters
- Must contain at least one uppercase letter
- Must contain at least one number
- Allowed special characters: `!@$_.`

### Username Requirements
- 4-20 characters in length
- Must contain at least 3 alphabetic characters
- Allowed special characters: `@_.`
- Must be unique across all users

### Order Processing
- Real-time inventory checking
- Automatic total calculation
- Order history tracking
- Customer spending analytics

### Financial Reporting
- Automated profit/loss calculations
- Expense categorization
- Revenue tracking by product
- Date-based financial analysis

## 🛠️ Technical Details

### Built With
- **Python 3.x**: Core programming language
- **CSV Module**: Data persistence
- **Datetime Module**: Time tracking and validation
- **OS Module**: Cross-platform file operations

### Data Validation
- Comprehensive input validation for all user entries
- Date format verification (YYYY-MM-DD)
- Numeric range checking for prices and quantities
- String length and character validation

### Error Handling
- Graceful handling of file I/O errors
- User-friendly error messages
- Input validation with retry mechanisms
- Safe exit options throughout the application

## 🤝 Contributing

This is an educational project demonstrating:
- Object-oriented programming concepts
- File I/O operations
- User interface design in console applications
- Data validation and error handling
- Role-based access control implementation

## 📝 Notes

- All data is stored locally in CSV format
- The system is designed for single-user operation
- No network connectivity required
- Cross-platform compatible (Windows, macOS, Linux)

## 🔄 Recent Updates

- Fixed directory path issues for CSV file access
- Improved error handling for file operations
- Enhanced cross-platform compatibility
- Added comprehensive input validation

---

*This bakery management system was developed as a comprehensive Python programming project, showcasing various programming concepts including file handling, data validation, user authentication, and role-based access control.*

##Collaborators 
- Rajendran 
- Tan Zhen Ping
- Sangeerthanaa
