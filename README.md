# cyber-security-mooc-project-1

A simple, ugly and poorly-wirtten todo app created for as a part of the course Cyber Security Base 2022. The idea is to include at least five different security flaws on the 2021 OWASP Top Ten list and to provide suggested fixes for these flaws. The application contains (at least) the flwas listed further down in this document.

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

### FLAW 1: A01 (Broken Access Control)

### FLAW 2: A02 (Cryptographic Failure)

### FLALw 3: A03 (Injection)

For example with the following input it's possible to remove the admin user from the database.

Remeber to prevent injection'); DELETE from auth_user where username=admin or username in ('

### FLAW 4: A05 (Security Misconfiguration)

### FLAW 5: A09 (Security Logging and Monitoring Failures)
