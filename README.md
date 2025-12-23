\# Auth Brute-force Demo

Educational Flask project demonstrating authentication vulnerabilities
and basic server-side protection mechanisms.

## Project Overview

This project intentionally starts with an **insecure authentication flow**
to demonstrate why brute-force protection is required in real-world systems.

The project follows a clear learning path:
1. Implement a vulnerable login endpoint
2. Demonstrate a brute-force attack
3. Apply server-side protection to mitigate the attack

---

## Baseline (Vulnerable Version)

- Simple login form
- No rate limiting
- No account lockout
- Unlimited authentication attempts
- Intentionally vulnerable to brute-force attacks

---

## Brute-force Vulnerability

The login endpoint allows unlimited authentication attempts.

A simple brute-force script can:
- send repeated POST requests
- enumerate username/password combinations
- successfully authenticate without restriction

This demonstrates the absence of:
- rate limiting
- temporary lockout
- automated attack detection

---

## Implemented Protection

- Rate limiting based on client IP address
- Failed login attempt tracking
- Temporary IP blocking after multiple failed attempts
- Time-based lockout mechanism

Result:
- Automated brute-force attack no longer succeeds

---

## Disclaimer

This project is for **educational purposes only**.
It is not intended for production use and does not implement
all security measures required in real-world systems.
