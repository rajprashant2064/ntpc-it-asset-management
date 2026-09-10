# NTPC IT Asset Management System

A desktop-based IT Asset Management System developed using **Python, Tkinter, and MySQL** to manage organizational IT assets efficiently.

## 📌 Project Overview

The NTPC IT Asset Management System provides a centralized interface for managing IT assets and their assignments. It supports asset registration, searching, updating, assigning, and deleting records through a graphical user interface.

The system includes **administrator authentication** to restrict access to asset management operations.

## 🚀 Features

- 🔐 Administrator Login Authentication
- ➕ Add new IT assets
- 🔍 Search and view asset records
- ✏️ Update existing asset information
- 👤 Assign assets to employees
- 🗑️ Delete assets with administrator authorization
- 📊 Real-time asset statistics
- 🗄️ MySQL database integration
- 🖥️ User-friendly Tkinter GUI
- 🔒 Passwords and database credentials managed through environment variables

## 🛠️ Technologies Used

- **Python**
- **Tkinter**
- **MySQL**
- **MySQL Connector/Python**
- **python-dotenv**
- **bcrypt**

## 🗃️ Database Structure

The application uses a MySQL database named:

`Ntpc_Asset_Management`

Main tables include:

- `assets`
- `employees`
- `users`
- `asset_assignments`

### Asset Information

The system maintains information such as:

- Asset ID
- Asset Code
- Asset Name
- Asset Type
- Manufacturer
- Model
- Serial Number
- Department
- Location
- Assigned Employee
- Purchase Date
- Warranty Expiry
- Status
- Remarks

## 🔐 Security

Sensitive database credentials are **not stored directly in the source code**.

Database credentials are loaded using environment variables through a `.env` file.

The `.env` file is excluded from Git using `.gitignore`.

> **Note:** This repository does not contain the actual database credentials or sensitive authentication information.

## 📂 Project Structure

```text
ntpc-it-asset-management/
│
├── assets.py
├── create_admin.py
├── dashboard.py
├── data.py
├── database.py
├── login.py
├── main.py
├── NTPC.png
├── requirements.txt
├── .gitignore
└── README.md
## 📸 Screenshots

### 🔐 Administrator Login
![Administrator Login](login.png)

### 📊 Dashboard
![Dashboard](dashboard.png)

### ➕ Add New Asset
![Add New Asset](add_asset.png)

### 🔍 Search Assets
![Search Assets](search_asset.png)


### 📋 Asset Records
![Asset Records](screenshots/view_asset.png)
