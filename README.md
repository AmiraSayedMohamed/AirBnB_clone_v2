AirBnB clone - MySQL

Group Project

Python OOP Back-end

 SQL MySQL ORMs SQLAlchemy

Weight: 2

This project is designed to be completed in teams of two people. Your team is comprised of:

    Amira Sayed Mohamed Ali Hemdan
    Olayinka Alawode

The project kicks off on June 21, 2024, at 6:00 AM and concludes on June 27, 2024, at 6:00 AM. The checker was released on June 22, 2024, at 6:00 PM. An automated review will be triggered upon the deadline.

Background Context

Environment variables will be your best friends for this project! Here's a breakdown of the ones you'll be using:

    HBNB_ENV: This variable signifies the running environment. It can be set to either "dev" or "test" for now (with "production" coming soon!).
    HBNB_MYSQL_USER: This stores the username for your MySQL database.
    HBNB_MYSQL_PWD: This stores the password for your MySQL database.
    HBNB_MYSQL_HOST: This specifies the hostname of your MySQL database.
    HBNB_MYSQL_DB: This indicates the database name for your MySQL database.
    HBNB_TYPE_STORAGE: This variable defines the type of storage used. It can be set to either "file" (utilizing FileStorage) or "db" (utilizing DBStorage).

Resources

    Refer to or watch the following resources to enhance your understanding:
        cmd module
        Packages concept page
        unittest module
        Arguments and keyword arguments (args/kwargs)
        SQL Alchemy tutorial
        How to Create a New User and Grant Permissions in MySQL
        Python3 and environment variables
        SQLAlchemy documentation
        MySQL 8.0 SQL Statement Syntax
    Learning Objectives: Upon completing this project, you should be able to confidently explain (without relying on external sources) the following concepts:
        What unit testing is and how to implement it within a large project
        The purpose of *args and how to use it effectively
        The purpose of **kwargs and how to use it effectively
        How to handle named arguments within a function
        How to create a MySQL database
        How to create a MySQL user and grant the necessary privileges
        The concept of ORM (Object-Relational Mapping)
        How to map a Python class to a MySQL table
        How to manage two distinct storage engines using the same codebase
        How to leverage environment variables
    Copyright - Plagiarism

You are tasked with developing solutions for the tasks outlined below to achieve the aforementioned learning objectives. Copying and pasting someone else's work to fulfill these requirements is strictly prohibited. You are not allowed to publish any content related to this project. Any form of plagiarism will be rigorously investigated and may result in removal from the program.

Requirements

    Python Scripts
        Allowed editors: vi, vim, emacs
        All your files should conclude with a new line.
        The first line of all your files should strictly adhere to the following format: #!/usr/bin/python3
        A README.md file is mandatory and must be positioned at the root directory of the project.
        Your code should comply with the pycodestyle (version 2.8.*) guidelines.
        All your files must be executable.
        The length of your files will be subjected to testing using wc.
        All your modules should possess documentation (you can utilize python3 -c 'print(__import__("my_module").__doc__)' to verify).
        All your classes should possess documentation (you can utilize python3 -c 'print(__import__("my_module").MyClass.__doc__)' to verify).
        All your functions (both within and outside of a class) should possess documentation (you can utilize python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' to verify).
        Documentation is not merely a single word; it should be a comprehensive sentence that elucidates the purpose of the module, class, or method (the length will also be assessed).

    Python Unit Tests
        Allowed editors: vi, vim, emacs
        All your files should conclude with a new line.


