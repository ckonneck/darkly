**Insecure Role Escalation (IDOR on PATCH)**

Insecure role escalation occurs when a website allows users to change their own permissions or privileges without properly checking whether they are authorized to do so.

A PATCH request is commonly used by websites to update specific fields of an existing resource, such as a user's profile information, account settings, or permissions.

The problem arises when the backend accepts changes to sensitive fields without verifying whether the user is allowed to modify them.

Imagine a website where you can edit your profile by sending a PATCH request to an endpoint such as `/api/users/123`. Normally, you might only be allowed to change your display name or email address.

If the backend doesn't properly restrict which fields you can modify, you might be able to include an additional field such as `"role": "admin"` in the request. If the server accepts this change without checking your permissions, your account could be upgraded from a regular user to an administrator.

Another possibility is that the website allows you to change the ID in the request to target another user's account. If the server doesn't verify that you are authorized to modify that particular account, you might be able to change someone else's role or permissions.

The important distinction is that IDOR (Insecure Direct Object Reference) specifically refers to accessing or modifying an object without proper authorization. Changing your own role by submitting an unauthorized field is more accurately described as a mass assignment vulnerability or broken function-level authorization, depending on how the application is implemented. These vulnerabilities can overlap.

If successful, an attacker might gain access to administrative functions, sensitive user data, or functionality that should only be available to privileged accounts.

The most important security measures are enforcing authorization checks on the server, explicitly restricting which fields users can modify, validating role changes against the user's existing permissions, and never trusting role or permission values supplied by the client.