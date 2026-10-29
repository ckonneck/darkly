# Sensitive Data Exposure via HTTP Headers

## 1. Audit Response Headers Before Production
Review every header returned by your application. Remove or restrict headers that reveal internal paths, agent versions, schedules, or infrastructure details.

## 2. Return Minimal Error Responses
On authentication failures (403, 401), return an empty body with no diagnostic headers. Operational metadata like backup destinations has no place in HTTP responses.

## 3. Strip Server Version Headers
Disable or spoof `Server` and `X-Powered-By` headers. Advertising your stack (`uvicorn/0.24.0`, `Python/3.11`) helps attackers target known vulnerabilities.

## 4. Use a Reverse Proxy to Sanitize Headers
Place nginx or a similar proxy in front of your application and configure it to strip internal headers before responses reach clients.

## 5. Separate Internal and External APIs
Endpoints intended for internal tooling (backup agents, monitoring) should not be reachable from the public internet at all, regardless of what headers they return.

## 6. Don't leave backend routes open or linked in the frontend
