# Secure File Upload — Best Practices

## 1. Restrict Allowed File Types
Maintain a strict whitelist of permitted extensions and MIME types. Reject anything not on it outright — never rely on a blocklist.


## 2. Validate File Content, Not Just the Extension
A file named `shell.jpg` may contain a PHP script or JavaScript payload. Inspect the actual file signature (magic bytes) to confirm it matches the claimed type.


## 3. Sanitize Filenames
Never trust the client-supplied filename. Strip path traversal sequences, null bytes, and special characters before using it anywhere on the filesystem.


## 4. Randomize Stored Filenames
Never store files under the original client-supplied name. Generate a random UUID or hash-based name server-side — this prevents overwriting existing files and makes stored paths unpredictable.


## 5. Store Outside the Web Root
Uploaded files should never be directly accessible via URL. Serve them through a controlled handler that enforces access checks, rather than as static files from a public directory.


## 6. Rate Limiting
Cap upload frequency per user/IP to prevent abuse. Log all uploads with timestamp, IP, and original filename for audit purposes.
