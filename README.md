# cyber-security-mooc-project-1

A simple, ugly and poorly-wirtten todo app created as a part of the course Cyber Security Base 2022. The idea is to include at least five different security flaws on the 2021 [OWASP Top Ten](https://owasp.org/www-project-top-ten/) list and to provide suggested fixes for these flaws. The application contains (at least) the flaws that listed further down in this document.

More detailed assignment instructions: https://cybersecuritybase.mooc.fi/module-3.1)

## Requirements

To run this project, python and django should be installed on your computer. The project is built with Python 3.8.4 and Django 4.1.4 on MacOS.

## Installation

Clone the repository and run the following command in the root folder of the project in order to set up the database

`python3 manage.py migrate`

The migration should also create a few test users with the following credentials:

admin:admin      
bobby:tables     
chuck:norris      

You can then start the app by running 

`python3 manage.py runserver`

The app should now be running at http://127.0.0.1:8000/


### FLAW 1: A01 (Broken Access Control)

Code pointer: https://github.com/picada/cyber-security-mooc-project-1/blob/main/todo/views.py#L34

In the current implementation, user passwords are stored in in the database unencrypted in plain text format. This could be a very bad thing for example if the passwords would be leaked after a cyber attack.

The simplest fix in this case would be to just use Django's built-in password management functionality. Basically, the `set_password` and `check_password` could be removed from the file, in whcih case the model would fall back to using the ready-made functionalities for hashing and other password logic.

### FLAW 2: A02 (Cryptographic Failure)

Code pointer: https://github.com/picada/cyber-security-mooc-project-1/blob/main/todo/models.py#L7

### FLAW 3: A03 (Injection)

Code pointer: https://github.com/picada/cyber-security-mooc-project-1/blob/main/todo/views.py#L14


The functionality for adding new todos is vulnerable to SQL injections, which is a major issue as it provides practically anyone a direct access to the database. For example with the following input it's possible to remove the admin user from the database - not nice.

```Remeber to prevent injection'); DELETE FROM auth_user WHERE username=admin OR username IN ('```

The most obvious way to fix this issue is to move away from making direct SQL queries and not handling user input in them. This can be done by using Django's builtin ORM for the databse queries. In addition, the database query is now executed with cursor.executequeries(), which allows multiple queries in the same operation. In case one would like to perform direct SQL queries, it's better to use `cursor.execute()`, which allows performing only one query at a time. This at least prevents adding other query types (such as DELETE or UPDATE) to the same query.

### FLAW 4: A05 (Security Misconfiguration)

Code pointer: https://github.com/picada/cyber-security-mooc-project-1/blob/main/todo/migrations/0002_auto_20221230_2223.py#L6

### FLAW 5: A09 (Security Logging and Monitoring Failures)

Code pointer: https://github.com/picada/cyber-security-mooc-project-1/blob/main/project/settings.py#L26

There is no decent logging or error monitoring whatsoever. There are no try-except-blocks, all errors are thrown to the user as it is. In addition, debugging is left on in the settings, which should never happen in production since having the debug mode enabled in production can expose sensitive information. 

As a fix, the debug flag in settings.py should be changed to DEBUG = False. Also proper logging should be added to all transactions, and possible errors should be caught and handled properly.

