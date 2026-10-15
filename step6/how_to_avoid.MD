# Insecure Role Escalation (IDOR on PATCH)

## 1. Never Trust Client-Supplied Role Values
The server must never accept a role field from user input. Role assignment must happen server-side based on verified identity and business logic only.

## 2. Whitelist Updatable Fields
Define explicitly which fields a user may update on their own record. Reject any request that includes fields outside that whitelist, rather than passing them through.

## 3. Require Elevated Auth for Privilege Changes
Any change to roles, permissions, or admin status must require re-authentication or a separate privileged token — not just a valid session.

## 4. Log All Role Changes
Record every privilege escalation with timestamp, requesting user, and old and new values. Alert immediately on any role change to admin or god-level.

## 5. Separate User and Admin APIs
Admin operations should live on a completely separate API surface with its own authentication layer, not on the same endpoint that regular users interact with.
