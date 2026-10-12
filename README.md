# Password Security Checker

A beginner-friendly cybersecurity project that evaluates password strength using basic security checks and checks whether a password has appeared in known data breaches. It comes in two versions: a Python command-line program and a web application.

## Live Demo

Try the web application: https://password-security-checker-web.vercel.app/

> **Use fake or test passwords only.** Do not enter real passwords into this tool or any similar project.

## Project Overview

The Password Security Checker analyzes a test password and provides a basic security assessment. It checks for:

- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Common passwords
- Repeated characters
- Simple sequences
- **Known data breaches** (using the Have I Been Pwned database)

It then gives a security score, a strength rating, and recommendations for improvement.

## Technologies Used

- Python 3 (command-line version)
- HTML, CSS and JavaScript (web version)
- Have I Been Pwned "Pwned Passwords" API (breach check)
- Visual Studio Code
- Git, GitHub and Vercel

## Features

### Password Strength Scoring

The program gives a score from 0/5 to 5/5 based on basic password characteristics.

### Common Password Detection

The program checks whether the password matches a small list of commonly used passwords.

### Repeated Character Detection

Detects patterns such as:

- aaa
- 111
- !!!

### Simple Sequence Detection

Detects simple sequences such as:

- 1234
- abcd
- qwer
- asdf

### Data Breach Check

A password can look strong and still be unsafe if it has already leaked. For example, `P@ssw0rd123!` passes most complexity rules but appears in real breaches.

The tool checks the password against the Have I Been Pwned database of passwords exposed in real data breaches. If the password is found, it is rated **VERY WEAK** and the number of times it appeared is shown.

### Security Recommendations

If weaknesses are detected, the program provides suggestions for improving the password.

## How the Breach Check Works

The breach check uses a technique called **k-anonymity**, so the password itself is never sent anywhere:

1. The password is hashed with SHA-1 on the user's own device.
2. Only the **first 5 characters** of that hash are sent to the Have I Been Pwned API.
3. The API replies with a list of all known hash endings that start with those 5 characters.
4. The program compares the rest of the hash against that list locally to see if there is a match.

The service never receives the password or its full hash.

**If the check cannot run** (for example, no internet connection), the tool shows "could not check" and carries on with its other checks. It never reports a password as safe just because the lookup failed.

**Common passwords** already found in the built-in list skip the breach lookup, since they are already flagged.

## How to Run

### Python version

1. Make sure Python 3 is installed.
2. Open the project folder in Visual Studio Code.
3. Open the terminal: **Terminal → New Terminal**.
4. Install the one required package (first time only):

   ```
   pip install requests
   ```

5. Run the program:

   ```
   python password_checker.py
   ```

6. Enter a test password when prompted.

### Web version

The web version is plain HTML, CSS and JavaScript. It needs to be served from `localhost` or `https` so the browser allows the hashing function used by the breach check.

**Option 1: VS Code Live Server**

Install the Live Server extension, right-click `index.html`, and choose **Open with Live Server**.

**Option 2: Python's built-in server**

From inside the web folder:

```
python -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

## Example

Example input:

```
BlueTiger!8472Moon
```

The program analyzes the password and displays its security characteristics, breach check result, and recommendations.

## Privacy and Security Notes

- Passwords are analyzed in the user's own browser or terminal.
- For the breach check, only the first 5 characters of the SHA-1 hash are sent to the Have I Been Pwned API. The password is never sent.
- Passwords are not stored or logged.
- SHA-1 is used only because the Have I Been Pwned API expects it. It is not used to protect anything.

## Learning Objectives

This project helped me practice:

- Python: variables, functions, conditional statements, loops, sets, string methods, the `string` module, boolean logic and command-line applications
- JavaScript, HTML and CSS
- Regular expressions
- Working with a web API (requests, responses and error handling)
- Hashing and the idea of k-anonymity
- Handling failures safely, such as an offline or unavailable service
- Git, GitHub and version control
- Web deployment with Vercel
- Client-side security considerations

## Limitations

- This project is an educational password checker.
- It does not guarantee that a password is secure or impossible to crack.
- The password strength calculation is based on simple rules rather than real-world password cracking data.
- The common-password list is intentionally small because this is a beginner project.
- The breach check needs an internet connection. A password not found in the database is not guaranteed to be safe, only that it has not appeared in the known breaches.

## Future Improvements

- Detection of more predictable patterns, such as keyboard walks and common substitutions like `p@ssw0rd`
- Improved password-strength estimation
- Showing how long a password might take to crack
- Better command-line interface
- More detailed educational explanations

## Deployment

The web application is deployed using Vercel. The project repository is hosted on GitHub, and the `web` directory is used as the deployment root. Each push to the main branch deploys automatically.

## Author

Izekee

I built this as part of my cybersecurity learning journey. I'm a 2nd year Cybersecurity student at Koladaisi.