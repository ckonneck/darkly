**Path Traversal through Download**

Path traversal vulnerabilities are a common way for attackers to access files on a server that were never intended to be publicly available.

The basic idea is that a website allows users to download files, but doesn't properly restrict which files can be requested.

Websites often use a download endpoint that accepts a filename or file path as a parameter. The server then uses that value to locate the requested file and send it back to the user.

The problem arises when the application trusts the supplied path without checking whether it points to a location the user is actually allowed to access.

Imagine a website where you can download a document through an endpoint such as `/download?file=report.pdf`. The server retrieves the requested file from a directory containing downloadable documents.

If the application doesn't properly validate the supplied path, an attacker might be able to use directory traversal sequences such as `../` to navigate outside the intended directory.

For example, instead of requesting `report.pdf`, the attacker could attempt to access a file such as `../../etc/passwd` on a Linux server. This file contains information about local user accounts and can help reveal details about the system.

Depending on the server's operating system, file permissions, and application configuration, the same vulnerability might expose configuration files, database credentials, application source code, or other sensitive information.

The important distinction is that path traversal does not automatically allow an attacker to execute commands on the server. It primarily allows unauthorized file access, although the information obtained could be used to support further attacks.

The most important security measures are restricting downloads to an explicitly allowed directory, validating requested files against an allowlist, resolving paths and verifying that they remain inside the intended directory, and enforcing appropriate file permissions. Simply filtering out `../` is not sufficient because alternative encodings and path representations may bypass naive filters.