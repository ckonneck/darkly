# Weak JWT Secret

## 1. Use a Long, Random Secret
Generate JWT secrets using a CSPRNG with at least 32 bytes of entropy (`secrets.token_hex(32)`). Never use short, guessable strings like `42network`.

## 2. Rotate Secrets Periodically
Treat JWT secrets like passwords — rotate them on a schedule and immediately after any suspected compromise. Implement a grace period to avoid invalidating all active sessions at once.

## 3. Use Asymmetric Signing (RS256)
Switch from HS256 (shared secret) to RS256 (public/private key pair). The private key signs tokens; the public key verifies them. Compromise of the verification key does not allow forgery.

## 4. Validate All Claims
Always verify `exp` (expiry), `iss` (issuer), and `aud` (audience) on every token. Reject tokens missing required claims rather than treating them as optional.

## 5. Never Expose the Secret
Secrets must never appear in source code, HTML comments, config endpoints, or version control. Load them exclusively from environment variables or a secrets manager.
