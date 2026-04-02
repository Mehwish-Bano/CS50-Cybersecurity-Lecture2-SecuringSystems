# Ports and Firewalls

## Common Ports
- 80 → HTTP
- 443 → HTTPS
- 22 → SSH

## Port Scanning
- Adversaries may scan open ports for vulnerabilities.
- Example tools: `nmap`

## Firewalls
- Block unauthorized access to ports.
- Can perform deep packet inspection to check traffic.
- Protects against malicious traffic from outside or inside.

## Demo
- Check open ports on your machine:
```bash
netstat -tuln
