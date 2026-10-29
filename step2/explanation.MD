**Unrestricted File Uploads**

Unrestricted file uploads are a common entryway for breaches, especially on websites that allow users to upload files.

The basic idea is that a website allows users to upload files, but doesn't properly check what kind of files are being uploaded.

For example, a website might allow users to upload profile pictures, documents, or other attachments. If the website only checks the file's name instead of its actual contents, an attacker might be able to upload a file that the website was never supposed to accept.

Imagine a website that only allows you to upload images. You might expect it to reject scripts or executable files, but if its security checks are poorly implemented, you could potentially upload something like a PHP script instead of an image.

If the server is configured to execute that script, rather than simply store it as a file, the attacker might be able to execute commands on the server itself.

Depending on the server's configuration and the permissions of the application, this could lead to a server compromise, unauthorized access to data, or even a foothold for further attacks.

Not every unrestricted file upload leads to remote code execution. Even if the uploaded file cannot be executed, an attacker might still abuse the upload functionality to host malicious files, overwrite existing files, or exploit vulnerabilities in software that processes the uploaded content.

The most important security measures are validating file contents rather than trusting file extensions, restricting allowed file types, generating safe filenames, limiting upload permissions, and storing uploaded files outside directories where the server executes code.