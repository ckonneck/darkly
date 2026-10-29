**Insecure Direct Object Reference (IDOR)**

IDOR vulnerabilities are one of the more common ways to gain unauthorized access to data on a website.

The basic idea is that a website uses identifiers to determine which resources a user can access, but doesn't properly check whether that user is actually allowed to access them.

These identifiers can be user IDs, invoice numbers, document IDs, filenames, or any other value the application uses to locate a specific resource.

Imagine a website where you can view your personal information by visiting an endpoint such as `/api/users/123`. The number `123` identifies your account.

If you change that number to `124` and the website returns another user's personal information without checking your permissions, you've found an IDOR vulnerability.

The same principle applies to modifying or deleting data. For example, a website might allow you to download your own invoices through an endpoint such as `/api/invoices/5001`. If you can change the invoice number and retrieve another customer's invoice, the application is failing to enforce proper access controls.

The important distinction is that the identifier itself doesn't need to be secret or difficult to guess. Even randomly generated IDs won't prevent IDOR if the backend fails to verify that the requesting user has permission to access the requested resource.

Depending on the application, an IDOR vulnerability can expose personal information, financial records, private messages, or confidential documents. If the application also allows unauthorized modifications, an attacker might be able to change or delete other users' data.

The most important security measure is to enforce authorization checks on the server for every request involving a specific resource. The application must verify that the logged-in user is actually permitted to access or modify the requested object, rather than simply checking whether the user is logged in.