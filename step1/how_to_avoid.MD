# Brute Force Prevention

## 1. Implement Rate Limiting on Authentication Endpoints

Cap the number of login attempts per IP address and per account within a rolling time window. After a threshold is exceeded, introduce exponential backoff delays before returning a response. A common baseline: 5 failed attempts triggers a 30-second lockout, 10 triggers a 15-minute lockout.

## 2. Use Account Lockout with Owner Notification

Temporarily lock an account after repeated failed login attempts and immediately notify the account owner by email. Lockouts should require either a timeout or an explicit unlock via a verified email link — not just a successful CAPTCHA — to prevent automated bypass.

## 3. Enforce Strong Password Policies at Registration

Reject weak passwords at the point of creation using a strength estimator like zxcvbn. Enforce a minimum length of 12 characters, require mixed character classes, and cross-reference submissions against known breach databases via the HaveIBeenPwned API to block commonly used passwords before they are ever stored.

## 4. Require Multi-Factor Authentication for Privileged Accounts

Even a correctly brute-forced password becomes useless if a second factor is required. Enforce TOTP or hardware key MFA for all admin and privileged accounts. For standard users, offer MFA as an option and incentivize adoption.

## 5. Monitor and Alert on Anomalous Login Patterns

Log every authentication attempt with timestamp, IP address, user agent, and outcome. Alert in real time on patterns indicative of automated attacks — high request volume from a single IP, sequential username enumeration, distributed credential stuffing across many IPs, or logins from geographies inconsistent with the account's history.