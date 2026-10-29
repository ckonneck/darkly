**Cross-Site Scripting (XSS)**

Cross-Site Scripting attacks are a common way for attackers to exploit websites that don't properly handle user-supplied input.

The basic idea is that a website accepts information from a user and displays it to other users without correctly treating it as data rather than executable code.

Websites constantly process user input, such as comments, profile descriptions, search queries, and contact form submissions. If this input is inserted into a webpage without proper handling, an attacker might be able to inject JavaScript that runs in another user's browser.

Imagine a website with a comment section where users can post messages. Normally, you would expect the website to display whatever text you submit. If the website doesn't properly handle the input, an attacker might be able to submit a script instead of an ordinary comment.

When another user visits the page containing that comment, the browser might execute the injected JavaScript as if it were part of the legitimate website.

For example, a simple proof of concept might use `alert(1)` to demonstrate that JavaScript execution is possible. While this only displays a popup, the same underlying vulnerability could potentially be abused to perform actions within the victim's authenticated session, access information available to the page, or manipulate the content the victim sees.

The severity depends on where the vulnerable input appears, which users encounter it, and what security protections the website has in place. In some cases, an attacker might be able to target administrators, making XSS particularly dangerous if those administrators have access to sensitive functionality.

There are three common types of XSS. **Reflected XSS** occurs when malicious input is immediately included in a response, such as a search result. **Stored XSS** occurs when the malicious input is saved by the website and later displayed to other users. **DOM-based XSS** occurs when client-side JavaScript processes untrusted data in an unsafe way and causes it to execute in the browser.

The important distinction is that XSS generally executes in the victim's browser, not directly on the web server. It does not automatically provide a server shell or unrestricted access to the victim's computer.

The most important security measures are properly encoding output according to its context, avoiding unsafe JavaScript and HTML insertion methods, sanitizing HTML when user-submitted markup is intentionally allowed, and implementing a suitable Content Security Policy (CSP) as an additional layer of protection.