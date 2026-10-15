# Insecure Direct Object Reference (IDOR)

## 1. Enforce Ownership Checks on Every Request
Before returning any resource, verify the requesting user owns or has explicit permission to access it. Never rely solely on the ID being hard to guess.

## 2. Use Indirect References
Map internal IDs to user-specific tokens so even if someone enumerates IDs, they cannot access another user's resources without a valid mapping.

## 3. Apply Role-Based Access Control (RBAC)
Define what each role can read, write, and delete. Enforce these rules server-side on every endpoint, not just in the UI.

## 4. Audit Sensitive Field Exposure
Regularly review what fields are returned in API responses. Fields like `private_note`, `recovery_code`, and `pw_hint` should never appear in public-facing responses.

## 5. Log and Monitor Access Patterns
Detect enumeration attempts by logging sequential or high-volume ID lookups and alerting when patterns suggest automated scraping.
