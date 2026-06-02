# OWASP Juice Shop: Web Vulnerability Analysis

> **Author:** Mohamed Amin
> **Date:** June 2026
> **Target:** OWASP Juice Shop (local Docker instance)
> **Tool:** Browser, Developer Tools
> **Platform:** http://localhost:3000

---

## What is OWASP Juice Shop?

OWASP Juice Shop is an intentionally vulnerable web application created by
OWASP for security training and awareness. It contains dozens of real web
vulnerabilities that you can legally practice exploiting in a safe environment.
It is used by security professionals, developers, and students worldwide to
learn about web application security.

Running it locally via Docker means everything stays on your own machine.
No real systems are affected.

```
docker run -p 3000:3000 bkimminich/juice-shop
```

---

## Challenge 1: Finding the Hidden Score Board

### What the challenge is

The score board is a hidden page that shows all available challenges. It is
not linked anywhere on the site. You need to find it by analyzing the
application source code.

### How I found it

Opened browser developer tools with F12, navigated to the Sources tab, and
searched through the main JavaScript bundle for the string "score-board".
Found the route defined in the application code, confirming the path exists
but is intentionally hidden from the navigation menu.

Navigated directly to:
```
http://localhost:3000/#/score-board
```

![Score board found](images/juice-shop/01-scoreboard-found.png)

### What this shows

The application relies on the user not knowing the URL exists. This is called
security through obscurity. Any attacker who spends a few minutes analyzing
the JavaScript source code will find hidden routes, admin panels, and internal
endpoints. Hidden does not mean protected.

OWASP category: Security through Obscurity

---

## Challenge 2: Admin Login via SQL Injection

### What the challenge is

Log in as the administrator without knowing the password by exploiting a SQL
injection vulnerability in the login form.

### How the attack works

The login form takes a username and password and the backend builds a SQL
query using that input. If the application does not sanitize the input an
attacker can inject SQL code directly into the query.

### The payload

In the email field I typed:

```
' OR 1=1 --
```

The query that the application builds becomes:

```sql
SELECT * FROM users WHERE email = '' OR 1=1 --' AND password = ''
```

OR 1=1 is always true so the WHERE condition is always satisfied.
The double dash comments out everything after it including the password check.
The database returns the first user which is the administrator.

![SQLi input in login form](images/juice-shop/02-sqli-input.png)

### Result

Logged in successfully as admin@juice-sh.op without knowing the password.

![Logged in as admin](images/juice-shop/03-sqli-loggedin.png)

### What this shows

The application trusted user input and put it directly into a SQL query
without checking it first. One malformed input bypassed the entire
authentication mechanism and gave full admin access.

OWASP category: Injection (number 3 in OWASP Top 10)

---

## Challenge 3: XSS in the Search Bar

### What the challenge is

Inject a script into the search bar that executes in the browser, demonstrating
a Cross-Site Scripting vulnerability.

### How the attack works

The search bar takes input and displays it on the search results page. If the
application does not sanitize the input before rendering it, anything typed
gets interpreted as HTML and JavaScript by the browser instead of being
displayed as plain text.

### The payload

In the search bar I typed:

```html
<iframe src="javascript:alert('XSS')">
```

### Result

The browser executed the injected script and displayed an alert popup with
the text "XSS". An empty iframe also rendered in the search results area,
confirming the HTML was interpreted by the browser rather than displayed as
text.

![XSS alert popup](images/juice-shop/04-xss-alert.png)

### What this shows

The application rendered user input directly as HTML without escaping special
characters first. The browser had no way to distinguish between legitimate
page content and injected malicious code.

In a real attack the payload would silently steal the session cookie of every
user who visits the affected page and send it to the attacker's server. The
attacker can then log in as that user without needing their password.

OWASP category: XSS (listed under Injection in OWASP Top 10 2021)

---

## Summary

| Challenge | Vulnerability | OWASP Category |
|---|---|---|
| Hidden score board | Security through obscurity | Security Misconfiguration |
| Admin login bypass | SQL Injection | Injection |
| XSS in search bar | Cross-Site Scripting | Injection |

---

## Key Takeaway

All three vulnerabilities share the same root cause: the application trusted
user input without validating or sanitizing it first. SQLi trusted input going
into a database query. XSS trusted input going into a rendered webpage.
Security through obscurity trusted that users would not look at the source code.

These are not theoretical vulnerabilities. SQLi and XSS consistently appear
in real penetration tests against production applications and are in the OWASP
Top 10 for a reason.

---

*Tool: OWASP Juice Shop v17 via Docker | Browser: Chrome | Platform: localhost*
