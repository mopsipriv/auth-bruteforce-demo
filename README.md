\# 🔐 Auth Brute-force Demo

Educational Flask project demonstrating authentication vulnerabilities
and basic server-side protection mechanisms.

## 📌 Project Overview

This project intentionally starts with an insecure authentication flow
to demonstrate why brute-force protection is required in real-world systems.

The goal is to understand the attack–defense cycle rather than to build
a production-ready authentication system.

The project follows a clear learning path:

Implement a vulnerable login endpoint

Demonstrate a brute-force attack

Apply server-side protection to mitigate the attack

## Instalation

pip install -r requirements.txt

## ⚠️ Baseline (Vulnerable Version)

- The initial implementation contains multiple intentional weaknesses:

- Simple login form

- No rate limiting

- No account lockout

- Unlimited authentication attempts

- Intentionally vulnerable to brute-force attacks

- This version exists only to demonstrate the problem.

## 🧨 Brute-force Vulnerability

The login endpoint allows unlimited authentication attempts.

A simple brute-force script can:

- Send repeated POST requests

- Enumerate username/password combinations

- Successfully authenticate without restriction

This demonstrates the absence of:

- Rate limiting

- Temporary lockout

- Automated attack detection

## 📝 Logging & Monitoring

Security-related events are logged for analysis:

- Failed login attempts

- Successful logins

- IP blocks triggered by brute-force behavior

- Logs are written to a local log file and can be reviewed
  to understand attack patterns and defense effectiveness.

## 🛡️ Implemented Protection

To mitigate brute-force attacks, the following protections were added:

- Rate limiting based on client IP address

- Failed login attempt tracking

- Temporary IP blocking after multiple failed attempts

- Time-based lockout mechanism

Result

- Automated brute-force attacks no longer succeed

- Repeated login attempts trigger defensive responses

- Attack behavior becomes visible through logs

## ⚠️ Disclaimer

This project is for educational purposes only.

It is not intended for production use and does not implement
all security controls required in real-world systems
(e.g. CSRF protection, secure session handling, HTTPS enforcement).

The vulnerable version is intentionally implemented
to demonstrate common authentication weaknesses
and their exploitation via brute-force attacks.