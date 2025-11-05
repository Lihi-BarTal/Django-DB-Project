# 💾 Relational Database & Web Application (SQL/Django)

**University Project - Database Systems and Application Development**

---

## 💡 Overview
This project involves the full design, implementation, and querying of a complex relational database system, coupled with a basic web front-end application built using the **Django Web Framework**. The system is designed to manage contacts, applications, meetings, files, and associated permissions/usage logs.

## 🎯 Core Technical Areas

The repository demonstrates expertise in two integrated technical disciplines:

1.  **Database Design & SQL:**
    * **Schema (DDL):** Creation of a detailed **Entity-Relationship Diagram (ERD)** and the necessary Data Definition Language (DDL) to enforce complex business rules and data integrity (Primary Keys, Foreign Keys, etc.).
    * **Advanced Querying:** Implementation of complex analytical queries and **SQL Views** to extract specific data insights (e.g., analyzing contact networks, application usage, and identifying trends).

2.  **Web Application Integration (Django):**
    * **ORM Mapping:** Utilizing the **Django ORM** (`models.py`) to automatically map the relational schema into Python objects, ensuring seamless interaction between the application and the database.
    * **Front-End (Templates):** Basic HTML templates (`index.html`, `queryResults.html`, etc.) are created for user interaction, including adding, installing, and removing applications.
    * **App Logic:** Python files (`Views.py`, `Urls.py`) define the application logic, URL routing, and handle user requests against the database.

## 📄 Key Files & Components

| File Name | Description | Focus |
| :--- | :--- | :--- |
| **`ERD.pdf`** | **Full Database Schema Design.** Contains the Entity-Relationship Diagram and notes on modeling constraints. | **Design** |
| **`models.py`** | **Django ORM Models.** The Python objects generated to map directly to the relational database tables. | **ORM** |
| **`view_queries.sql` / `Q2.sql`** | SQL Scripts for **DDL (Schema Creation)** and defining complex **Views** and queries. | **SQL Logic** |
| **`Views.py` / `urls.py`** | Core application logic, URL routing, and database interaction handlers. | **Django Logic** |
| **`.html` Files** | Front-end templates for user interactions (Add, Install, Remove application screens) and query display. | **Front-End** |
