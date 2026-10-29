# Path Traversal
 
## 1. Validate and Canonicalize File Paths
Before accessing any file, resolve the full canonical path using os.path.realpath() and verify it starts with the intended base directory. A resolved path that escapes the base directory must be rejected outright.

## 2. Strip Path Components from User Input
Never use a client-supplied filename directly in a filesystem operation. Strip directory separators, .. sequences, and null bytes before use. os.path.basename() is a quick first pass but should always be combined with canonical path validation.

## 3. Use an Allowlist for Accessible Files
Rather than trying to block dangerous patterns, maintain an explicit list or database of files that are permitted to be served. If a requested file isn't in the list, reject it — regardless of whether the path looks safe.

## 4. Serve Files Through a Controlled Handler
Never expose a raw filesystem path as a URL parameter. Files should be referenced by an opaque ID (e.g. a UUID) that maps server-side to a real path. The client never sees or influences the filesystem path directly.

## 5. Apply Depth and Character Restrictions
Reject any input containing /, \, .., or null bytes (\x00) at the input validation layer before any path construction occurs. Additionally cap the permitted path depth — a filename that requires more than one level of directory traversal to resolve is almost certainly malicious.