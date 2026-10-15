# Cross-Site Scripting (XSS)

## 1. Escape All User Input Before Rendering
Any value echoed back into HTML must be HTML-escaped. In Jinja2, auto-escaping handles this automatically — never use `| safe` on user-supplied data.

## 2. Content Security Policy (CSP)
Set a strict `Content-Security-Policy` header that blocks inline scripts and restricts script sources to trusted origins. A basic policy: `script-src 'self'`.

## 3. HttpOnly and Secure Cookie Flags
Mark session cookies as `HttpOnly` so JavaScript cannot read them via `document.cookie`, limiting the impact of any XSS that does slip through.

## 4. Validate Input Server-Side
Reject inputs that contain HTML special characters (`<`, `>`, `"`, `'`) where plain text is expected — email addresses should never contain angle brackets.

## 5. Use a Templating Engine Correctly
Never concatenate user input directly into HTML strings. Always let the templating engine handle substitution so escaping is applied automatically and consistently.
