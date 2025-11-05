# 💾 Relational Database & Web Application (SQL/Django)

## University Project: Confused Student's Phone System

This project is a comprehensive **Full-Stack** solution for a Database Management course, combining **Relational Database Design (SQL)** with a **Django Web Application** for interactive data management and analytics.

---

## 🎯 Core Technical Focus

The repository demonstrates proficiency across two integrated disciplines:

### 1. Database Design & Advanced SQL

* **Conceptual Modeling:** Full **Entity-Relationship Diagram (ERD)** design (`ERD.pdf`).
* **Schema Implementation:** **Data Definition Language (DDL)** scripts (`Q2.sql`) defining tables for Contacts, Applications, Files, Meetings, and Permissions, enforcing complex integrity constraints.
* **Analytical Querying:** Implementation of advanced SQL views and queries (`Views.py`, `Queries.py`, `view_queries.sql`) to perform complex analysis, such as identifying **"Haifa Leading Apps"** and **"Exceeding Cities"**.

### 2. Django Web Application (Management & Analytics)

The application provides a user interface for managing the database, built on a single `phone_app` module.

| Component | Description |
| :--- | :--- |
| **Data Mapping** | **Django ORM** (`models.py`) connects directly to the established SQL schema. |
| **Functionality** | User interfaces for **Adding** new applications with size validation (100MB-200MB), **Installing/Removing** applications while strictly enforcing a **1800MB** total storage limit. |
| **Views & Logic** | **Views** (`views.py`) manage all application logic, user input validation, and database updates, including the use of **Raw SQL** for efficient analytical query execution. |

---

## 📄 Key Project Files

| File Name | Description | Part |
| :--- | :--- | :--- |
| **`ERD.pdf`** | Conceptual design and modeling assumptions. | A |
| **`Q2.sql`** | Full DDL script for table creation and integrity enforcement. | A |
| **`views.py`** | Django application logic, database access, and validation handlers. | B |
| **`models.py`** | Django ORM classes for `Contacts`, `Applications`, and `AppUsers`. | B |
| **`view_queries.sql`** | Dedicated SQL views for complex Django query results (e.g., `view6`, `view7`). | B |
