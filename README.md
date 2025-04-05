# 📰 Log Analysis Project

## 📌 Project Overview

This project simulates a real-world reporting task for a newspaper website. You’ve been brought onto the team to build an internal reporting tool that provides insights into user activity by analyzing the site’s logs.

The site and its PostgreSQL database are already running. Your task is to write a Python program that connects to the database, executes SQL queries, and prints the answers to key business questions—without requiring any user input.

---

## 🎯 Project Objectives

- Analyze web server logs and article metadata.
- Use SQL to discover user behavior patterns.
- Build a command-line reporting tool using Python and PostgreSQL.

---

## 🔍 Questions to Answer

Your program will answer the following questions:

1. **What are the most popular three articles of all time?**
2. **Who are the most popular article authors of all time?**
3. **On which days did more than 1% of requests lead to errors?**

---

## 💡 Why This Project?

- Practice interacting with a real SQL database (PostgreSQL) from both the command line and Python.
- Work with a large dataset (over a million rows).
- Gain experience writing and refining complex SQL queries.
- Understand how logs are used for reporting in real-world applications.
- See how different parts of a system (like a web server and a reporting tool) can communicate via a shared database.

---

## 🛠️ Setup Instructions

### 📦 Requirements

- VirtualBox
- Vagrant
- PostgreSQL
- Python 3
- `psycopg2` Python library

### 🖥️ Environment Setup

1. **Download and Install Tools**  
   - [Vagrant](https://www.vagrantup.com/)
   - [VirtualBox](https://www.virtualbox.org/)

2. **Initialize and Configure VM**  
   - Use `vagrant up` to bring the VM online.  
   - SSH into the VM using `vagrant ssh`.

   **Modify `Vagrantfile`:**
   ```ruby
   config.vm.box = "bento/ubuntu-16.04"
   config.vm.box_version = "201912.15.0"
   ```

3. **Download and Load the Database**

   - Download data:  
     [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
   - Unzip it inside the Vagrant folder.
   - Load it with:
     ```bash
     psql -d news -f newsdata.sql
     ```

4. **Connect to the Database**
   ```bash
   psql -d news
   ```

5. **Run the Python Script**
   ```bash
   python3 log_analysis.py
   ```

---

## 📁 Project Structure

```
log-analysis/
│
├── log_analysis.py      # Python script to analyze and print report
├── newsdata.sql         # SQL dump of article and log data
├── README.md            # This file
```

---

## 📚 Resources

- [PostgreSQL Official Docs](https://www.postgresql.org/docs/devel/app-psql.html)
- [Connecting to PostgreSQL](https://www.postgresql.org/docs/12/tutorial-accessdb.html)
- [SQL Basics](https://www.sqltutorial.org/sql-cheat-sheet/)
- [Advanced SQL Cheat Sheet](https://hackr.io/blog/sql-cheat-sheet)
- [Tutorial Video](https://www.youtube.com/watch?v=2PDkXviEMD0)

---

## ✅ Notes

- Make sure you're running Python 3.
- Use `psycopg2` to interact with the database.
- The script does **not** accept user input—it just prints a report to the terminal.
