Password Security Checker

A beginner-friendly cybersecurity project built with Python that evaluates password strength using several basic security checks.

Project Overview

The Password Security Checker analyzes a test password and provides a basic security assessment.

It checks for:

- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Common passwords
- Repeated characters
- Simple sequences

The program then provides a security score, strength rating, and recommendations for improvement.

Technologies Used

- Python 3
- Visual Studio Code
- Python Standard Library

Features

Password Strength Scoring

The program gives a score from:

0/5 to 5/5

based on basic password characteristics.

### Common Password Detection

The program checks whether the password matches a small list of commonly used passwords.

### Repeated Character Detection

The program detects patterns such as:

```text
aaa
111
!!!

The program checks for simple sequences such as:

1234
abcd
qwer
asdf

Security Recommendations

If weaknesses are detected, the program provides suggestions for improving the password.

How to Run
1. Install Python

Make sure Python 3 is installed on your computer.

2. Open the project

Open the project folder in Visual Studio Code.

3. Open the terminal

In VS Code, select:

Terminal → New Terminal

4. Run the program
python password_checker.py
5. Enter a test password

Use a fake password for testing.

Do not enter real passwords into this program.

Example

Example input:

BlueTiger!8472Moon

The program analyzes the password and displays its security characteristics and recommendations.

Learning Objectives

This project was created to practice:

Python variables
Functions
Conditional statements
Loops
Sets
String methods
The string module
Boolean logic
Basic cybersecurity concepts
Command-line applications

Limitations

This project is an educational password checker.

It does not guarantee that a password is secure or impossible to crack.

The password strength calculation is based on simple rules rather than real-world password cracking data.

The common-password list is also intentionally small because this is a beginner project.

Future Improvements

Possible future improvements include:

Larger common-password database
Detection of more predictable patterns
Improved password-strength estimation
Better command-line interface
Unit tests
Graphical user interface
Web-based version with client-side processing