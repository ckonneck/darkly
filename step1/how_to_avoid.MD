Brute Force Attack Prevention
What is a Brute Force Attack?

A brute force attack is an automated attempt to gain unauthorized access by systematically trying large numbers of username/password combinations until the correct one is found. Modern tools can test thousands of combinations per second, making weak or common passwords trivially crackable in minutes.

Mitigation Strategies
1. Rate Limiting

Limit the number of login attempts per IP address or account within a given time window. After a threshold is exceeded, temporarily block further attempts.

Implementation:

Allow 5 failed attempts before introducing a delay or lockout
Implement exponential backoff (1s, 2s, 4s, 8s...) between attempts
Hard lockout after 10+ consecutive failures, requiring manual unlock or CAPTCHA
Apply limits per IP and per account to prevent distributed attacks

Relevant tools: FastAPI's slowapi, nginx limit_req, application-level middleware

2. Password Policy Enforcement

Enforce strong passwords at the point of creation, not just at login.

Minimum requirements:

At least 12 characters
Mix of uppercase, lowercase, numbers, and symbols
Rejection of passwords found in common wordlists (e.g. rockyou.txt)
Prohibition of passwords containing the username or email address
No reuse of the last 5 passwords

Relevant tools: zxcvbn for strength estimation, HaveIBeenPwned API for breach checking

3. Regular Password Rotation

Require users to change passwords periodically, especially for privileged accounts.

Recommended intervals:

Standard users: every 90 days
Admin/privileged accounts: every 30–60 days
Immediate reset required after any suspected compromise

Important caveat: Forced rotation is only effective when combined with strong password policies — users forced to rotate without guidance tend toward predictable patterns (e.g. Password1 → Password2).

4. Multi-Factor Authentication (MFA)

Even a correct password alone is insufficient if MFA is enforced. A brute-forced password becomes useless without the second factor.

Options (strongest to weakest):

Hardware security keys (FIDO2/WebAuthn) — phishing-resistant
TOTP authenticator apps (Google Authenticator, Authy)
SMS OTP — better than nothing, but vulnerable to SIM-swapping
5. Account Lockout and Anomaly Detection

Beyond simple rate limiting, detect and respond to suspicious patterns:

Lock accounts after repeated failures and notify the account owner by email
Flag logins from new geographic locations or unusual hours
Alert on credential stuffing patterns (many accounts attempted from one IP)
Log all failed attempts with timestamps and IP addresses for post-incident analysis
6. CAPTCHA

Introduce CAPTCHA challenges after a small number of failed attempts. This is effective against automated scripts while remaining usable for legitimate users.

Note: CAPTCHAs add friction for all users. Reserve them for the suspicious threshold rather than showing them on every login.

7. Credential Stuffing Defense

Brute force is distinct from credential stuffing (using leaked username/password pairs from other breaches). Additional defenses include:

Cross-reference passwords against known breach databases at registration and login
Detect high-velocity login attempts using varied passwords against a single account
Implement device fingerprinting to identify anomalous clients
Summary

No single measure is sufficient on its own. Defense in depth — combining rate limiting, strong password policies, MFA, and anomaly detection — makes brute force attacks impractical even against a determined attacker.

