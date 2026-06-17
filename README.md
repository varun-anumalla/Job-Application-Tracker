# 🚀 Job Application Tracker

A modern web-based Job Application Tracker built using **Python, Flask, SQLite, HTML, and CSS**.

This project helps job seekers organize, track, and manage their job applications from a single dashboard. Users can add applications, update statuses, search records, filter applications, export data, and store important job links for future reference.

---

# 📸 Project Screenshots

## Dashboard

(soon i will add )

## Add Application Page

(---)

## Edit Application Page

(---)

---

# 🎥 Project Demo

Watch Project Demo Video:

[YouTube Video link]

---

# 📌 Project Overview

Job searching often involves applying to multiple companies across different platforms. Managing these applications manually becomes difficult as the number of applications increases.

This project solves that problem by providing a centralized dashboard where users can:

* Store job applications
* Track application status
* Search applications quickly
* Filter applications by status
* Open saved job links directly
* Export application data to CSV

---

# ✨ Features

### Dashboard Statistics

* Total Applications
* Wishlist Applications
* Applied Applications
* Interview Applications
* Offer Applications
* Rejected Applications

### Application Management

* Add New Application
* Edit Existing Application
* Delete Application

### Status Tracking

Users can track applications using:

* Wishlist
* Applied
* Interview
* Offer
* Rejected

### Search Functionality

Search applications by:

* Company Name
* Job Role
* Location

### Status Filters

Filter applications using status chips.

### Job URL Support

Store job posting links and open them directly from the dashboard.

### CSV Export

Export all application data into a CSV file.

### Modern User Interface

* Dark Theme Dashboard
* Responsive Layout
* Gradient Design
* Interactive Cards
* Clean Forms

---

# 🛠️ Technologies Used

## Backend

* Python
* Flask

## Database

* SQLite

## Frontend

* HTML5
* CSS3

## Version Control

* Git
* GitHub

---

# 📚 Python Concepts Used

### Functions

Used to organize application logic into reusable blocks.

### Lists

Used for status management.

### Dictionaries

Used for dashboard statistics and data handling.

### Loops

Used for displaying records and generating statistics.

### Conditional Statements

Used for filtering and rendering application data.

### Modules

Code organized into multiple Python files.

### Flask Routing

Used to create multiple web pages and actions.

### Form Handling

Used to process user input from HTML forms.

### CSV Handling

Used to export application data.

### Database Connectivity

Used SQLite database connections and SQL queries.

---

# 🗄️ SQL Concepts Used

### CREATE TABLE

Used to create the applications table.

### INSERT

Used to add new job applications.

### SELECT

Used to retrieve application data.

### UPDATE

Used to edit applications and update statuses.

### DELETE

Used to remove applications.

### WHERE Clause

Used for filtering records.

### ORDER BY

Used to display recent applications first.

### COUNT()

Used to generate dashboard statistics.

### LIKE Operator

Used for search functionality.

---

# 📂 Project Structure

```text
Job_Application_Tracker/
│
├── app.py
├── database.py
├── tracker.db
│
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

# 📦 Python Libraries Used

```python
Flask
sqlite3
csv
io
```

---

# 🔧 Flask Imports Used

```python
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    Response
)
```

---

# 🗃️ Database Schema

```sql
CREATE TABLE applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    job_role TEXT NOT NULL,
    location TEXT,
    salary TEXT,
    applied_date TEXT,
    status TEXT,
    job_url TEXT,
    notes TEXT
);
```

---

# 🚀 How To Run The Project

## Clone Repository

```bash
git clone https://github.com/varun-anumalla/Job-Application-Tracker.git
```

## Navigate To Project

```bash
cd Job-Application-Tracker
```

## Install Flask

```bash
pip install flask
```

## Run Application

```bash
python app.py
```

## Open Browser

```text
http://127.0.0.1:5000
```

---

# 🎯 Learning Outcomes

Through this project, I learned:

* Building full-stack web applications using Flask
* Connecting Python applications with SQLite databases
* Performing CRUD operations
* Creating responsive user interfaces using HTML and CSS
* Handling forms and user input
* Managing application data with SQL queries
* Implementing search and filtering functionality
* Exporting data to CSV files
* Using Git and GitHub for version control
* Structuring real-world Python projects

---

# 🔮 Future Improvements

Possible future enhancements:

* User Authentication
* Login and Registration System
* Application Deadline Tracking
* Interview Scheduling
* Email Notifications
* Dashboard Charts and Analytics
* Cloud Database Integration
* Online Deployment

---

# 👨‍💻 Author

**Varun Anumalla**

B.Tech – Computer Science Engineering

Python | SQL | Flask | 

---

⭐ If you found this project useful, consider giving the repository a star.
