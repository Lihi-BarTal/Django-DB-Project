# 💾 Relational Database & Web Application (SQL/Django)

## University Project: Full-Stack Database System

This repository presents a comprehensive **Full-Stack** project combining **Advanced Relational Database Design (SQL)** with a functional web application built on the **Django Framework**. The system serves as a management and analytics tool for applications and contacts, demonstrating expertise in both back-end data integrity and front-end application logic.

---

## 🎯 Core Technical Focus

### 1. Database Design and Analytical SQL

* **Conceptual Modeling:** Full **Entity-Relationship Diagram (ERD)** and robust **Data Definition Language (DDL)** scripts (`Q2.sql`) defining the schema for Contacts, Applications, Meetings, and Files.
* **Data Integrity:** The DDL enforces complex rules, constraints, and relationships crucial for maintaining system integrity.
* **Advanced Querying:** Complex analytical logic is executed via **SQL Views** and raw queries (`view_queries.sql`, `Views.py`). These queries aggregate data to derive deep insights, such as identifying relationships between usage patterns and contact characteristics.

### 2. Django Web Application Logic

The Django application provides an interactive front-end, with logic implemented in Python (`views.py`) and rendered via HTML templates:

* **Controlled Data Management:** Interfaces are provided for **Adding** and **Installing/Removing** applications.
* **Business Rule Enforcement:** Application logic ensures strict enforcement of critical business rules, including:
    * **Application Size Validation** upon creation.
    * **Total Storage Limit** tracking and enforcement during installation.
* **Data Presentation:** Dedicated pages display the results of the complex analytical SQL queries.
