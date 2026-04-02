# HTTP vs HTTPS

## HTTP
- Unencrypted communication between client and server.
- Vulnerable to:
  - Packet sniffing
  - Man-in-the-middle (MITM) attacks
  - Injection of ads or malicious code

## HTTPS
- Secure version of HTTP.
- Uses **TLS** and public/private key cryptography.
- Certificates signed by **Certificate Authorities (CA)** verify the website.

## Demo
1. Open `http://example.com` → inspect developer tools → traffic is unencrypted.
2. Open `https://example.com` → traffic is encrypted.
