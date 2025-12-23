\# Auth Brute-force Demo



Educational Flask project.



Baseline version:

\- simple login form

\- no protection

\- intentionally vulnerable



Planned:

\- brute-force attack demo

\- protection mechanisms

## Brute-force vulnerability

The login endpoint allows unlimited authentication attempts.

A simple brute-force script can:
- send repeated POST requests
- enumerate username/password combinations
- successfully authenticate without restriction

This demonstrates the absence of rate limiting and account lockout.



