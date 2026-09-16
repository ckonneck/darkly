# Insecure Password Reset

## 1. Use Cryptographically Random Tokens
Generate reset tokens using a CSPRNG (`secrets.token_urlsafe(32)` in Python). Never derive them from predictable values like email addresses or timestamps.

## 2. Store Tokens Server-Side with Expiry
Save the token hash in the database with a short expiry (15–30 minutes). Invalidate it immediately after use so it cannot be reused.

## 3. Send Tokens via Email Only
The reset link should only ever arrive in the user's inbox — never appear in a redirect URL, response body, or HTTP header visible to the client.

## 4. Rate Limit Reset Requests
Limit how many reset requests can be made per email per hour to prevent enumeration of valid accounts and token flooding attacks.

## 5. Notify Users of Reset Attempts
Send a notification email even when a reset is requested for an account the attacker doesn't own. This alerts legitimate users to suspicious activity.

https://cheatsheetseries.owasp.org/index.html