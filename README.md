# 💾 Relational Database & Web Application (SQL/Django)

## University Project: Phone System Management & Database Analytics

This project is a comprehensive **Full-Stack** solution that demonstrates expertise in **Relational Database Design (SQL)** and the implementation of a functional web front-end using the **Django Web Framework**.

The application, simulating a "Confused Student's Phone System," allows for the management of applications, contacts, and files, while enforcing complex data integrity and storage rules.

---

## 🎯 Core Technical Focus

### 1. Advanced Database Design & SQL

* **Conceptual Modeling:** Full **Entity-Relationship Diagram (ERD)** and robust **Data Definition Language (DDL)** scripts (`Q2.sql`) to enforce complex business rules and data integrity.
* **Analytical Querying:** Implementation of advanced SQL logic using **VIEWS** (`view_queries.sql`) and Python wrappers (`Views.py`) to extract specific data insights, including:
    * Identifying contacts with highly-rated and highly-installed apps (e.g., **"Haifa Leading Apps"**).
    * Pinpointing **"Exceeding Cities"**—where all contacts have surpassed a specific storage threshold.

### 2. Django Web Application Logic

The Django application (using **ORM** via `models.py`) provides an interactive interface with critical business logic:

* **Controlled Data Entry:** Enables **Adding** new applications with size validation (strictly between 100MB and 200MB).
* **Resource Management:** Implements **Installation/Removal** logic that strictly enforces a **1800MB** total storage limit, preventing the user from exceeding phone capacity.
* **Data Presentation:** Displays the complex SQL analytical query results on a dedicated front-end page (`queryResults.html`).
