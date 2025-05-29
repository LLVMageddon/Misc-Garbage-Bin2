## ✅ Project : [Dynamic Envelope API Gateway](<../apigateway>)

**Purpose:**  
Implements a single API endpoint `/api` to receive all envelopes, validate them, and forward based on `eventCode`.

**Use Cases:**  
- Accept envelope input  
- Validate envelope schema  
- Route to appropriate service

**Notes:** Hardened entry point with logging and basic auth.

**Technical Notes:**  
- **Language:** Go  
- **Framework:**  Gin
- **Models:** `Envelope`, `Meta`, `Data`  
- **Pattern:** API Gateway Pattern  
- **Algorithm:** Event code → service map routing

[Back to README](../README.md)
