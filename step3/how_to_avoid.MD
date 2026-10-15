# XML External Entity Injection (XXE)

## 1. Use a Safe XML Parser
Replace stdlib `xml.etree.ElementTree` with `defusedxml`, which disables external entity resolution, DTD processing, and other dangerous XML features by default.

## 2. Disable DOCTYPE Declarations
If your application does not need DTD support, reject any XML input that contains a `<!DOCTYPE` declaration before parsing begins.

## 3. Disable External Entity Resolution Explicitly
If you must use a standard parser, configure it to reject `SYSTEM` and `PUBLIC` entity references before processing user-supplied XML.

## 4. Validate and Sanitize XML Input
Strip or reject unexpected elements and attributes at the schema validation layer before the document ever reaches the parser.

## 5. Prefer JSON Over XML for User Input
Where possible, accept JSON instead of XML for data import features. JSON parsers do not support entity expansion and are not vulnerable to this class of attack.

