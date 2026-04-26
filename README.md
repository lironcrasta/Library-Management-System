# Library-Management-System
This project implements a simple Library Management System using Python's Flask framework for the web application and MySQL as the database. It allows for the management of books, library members, and the borrowing/returning of books (loans).
Core Features:
Book Management:
Add Books: Librarians can add new books to the system, providing details such as title, author, and publication date.
View Books: All available books in the library can be viewed in a tabular format.
Member Management:
Add Members: New library members can be registered by providing their first name, last name, and email address.
View Members: A list of all registered library members is displayed.
Loan Management:
Issue Books: Librarians can issue books to members. When a book is issued, the system automatically records the issue date and calculates a due date (14 days from the issue date). The loan status is initially set to "Issued."
Return Books: Members can return borrowed books. Upon return, the system updates the loan record with the return date and changes the status to "Returned."
View Loans: All loan transactions, including issued, returned, and overdue books, can be viewed. The display includes book title, member name, issue date, due date, return date, and current status.
Delete Loans: Loan records can be removed from the system.
Technologies Used:
Backend:
Python Flask: A micro-framework for building web applications, handling routing, requests, and responses.
MySQL Connector/Python: A Python driver for interacting with MySQL databases.
Database:
MySQL: A relational database management system (RDBMS) used to store and manage library data (books, members, loans).
Frontend:
HTML: Used for structuring the web pages and displaying information.
Jinja2 Templating Engine: Integrated with Flask to dynamically generate HTML pages by injecting data from the backend.
Database Schema:
The system uses three main tables in the LIBRARY_MANAGEMENT database:
Book Table:
book_id (Primary Key, Auto-increment): Unique identifier for each book.
title (VARCHAR): Title of the book.
author (VARCHAR): Author of the book.
published_date (DATE): Date the book was published.
Member Table:
member_id (Primary Key, Auto-increment): Unique identifier for each library member.
first_name (VARCHAR): First name of the member.
last_name (VARCHAR): Last name of the member.
email (VARCHAR, Unique): Email address of the member.
Loan Table:
loan_id (Primary Key, Auto-increment): Unique identifier for each loan transaction.
book_id (Foreign Key): References book_id in the Book table.
member_id (Foreign Key): References member_id in the Member table.
issue_date (DATE): Date the book was issued.
due_date (DATE): Date the book is expected to be returned (automatically calculated as 14 days from issue date).
return_date (DATE, Nullable): Date the book was actually returned.
status (VARCHAR, Default 'Issued'): Current status of the loan (e.g., 'Issued', 'Returned').
Workflow:
Setup: The Db.sql script is executed to create the LIBRARY_MANAGEMENT database and its tables.
Application Start: The Flask application (app.py) connects to the MySQL database.
Navigation: Users can navigate through different sections:
/: Home page with links to other sections.
/books: View all books and add new ones.
/members: View all members and add new ones.
/loans: View all loan transactions, return books, and delete loans.
/issue: Issue a new book to a member.
Data Operations:
Add: Forms are used to submit data for new books and members, which are then inserted into the respective tables.
View: SQL SELECT queries retrieve data from the database, which is then rendered on HTML pages using Jinja2.
Update: The /return/<id> route updates the Loan table when a book is returned.
Delete: The /delete/<id> route removes loan records from the Loan table.
Potential Enhancements:
User Authentication and Authorization: Implement login for librarians and members with different access levels.
Search and Filter: Add search functionality for books, members, and loans.
Validation: Implement input validation for forms to ensure data integrity.
Error Handling: More robust error handling for database operations and user input.
UI/UX Improvements: Enhance the user interface with CSS for a better visual experience.
Overdue Reminders: Implement a system to identify and notify about overdue books.
Book Availability: Track the number of copies for each book and prevent issuing books that are out of stock.
