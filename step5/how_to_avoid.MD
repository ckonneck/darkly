# API Access Control

## 1. Enforce Authorization on Every Endpoint Server-Side
Never rely on the frontend to hide or disable API endpoints for unprivileged users. Every API call must be independently verified server-side against the requesting user's role and permissions — if the check isn't in the handler, it doesn't exist.

## 2. Apply the Principle of Least Privilege
Each user role should have access only to the minimum set of endpoints and data fields required for their function. A student role should never be able to call admin endpoints, patch role fields, or read other users' private data — even if they discover the URL.

## 3. Whitelist Writable Fields Per Role
When accepting PATCH or PUT requests, define explicitly which fields each role is permitted to modify. Reject any request that includes fields outside that whitelist rather than silently ignoring them. A user should never be able to modify their own role, permission level, or verified status.

## 4. Use a Centralized Authorization Layer
Avoid scattering permission checks across individual route handlers where they can be missed or inconsistently applied. Implement a single middleware or decorator that enforces role checks uniformly across all protected endpoints, so no route can accidentally be left unguarded.

## 5. Regularly Audit API Surface and Permissions
Maintain a complete inventory of every endpoint, the roles permitted to call it, and the fields each role can read or write. Review this inventory before every release and after any schema or role change — undocumented endpoints and forgotten admin routes are a consistent source of privilege escalation vulnerabilities.