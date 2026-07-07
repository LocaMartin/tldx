<p align="right">
  <img src="https://img.shields.io/badge/python-%3E%3D3.6-blue" alt="Python >= 3.6">
</p>

<div align="center">
<h1>TLDX</h1>
<p>1.0.2</p>
<p><b>Top Level Domain(TLD) Expansion Tool For Bug Bounty</b></p>
<p><b>Expand keywords across all TLDs to discover hidden assets during reconnaissance.</b></p>
</div>

---
### Installation
```yml
pip install tldx
```

---

<h3 align="center">Features</h3>

- Generate domain permutations (keyword + TLD)
- Supports single keywords or keyword files
- Uses official IANA TLD list
- Custom TLD lists support
- Output to console or file

---

<h3 align="center">Flags</h3>

```yml
usage: tldx [-h] [-k KEYWORD] [-kf KEYWORD_FILE] [-o OUTPUT] [-t TLD_FILE] [-v]

TLDX - TLD Expansion Tool for Bug Bounty

options:
  -h, --help            show this help message and exit
  -k, --keyword KEYWORD
                        Single keyword to combine with TLDs
  -kf, --keyword-file KEYWORD_FILE
                        File containing keywords (one per line)
  -o, --output OUTPUT   Output file to save results
  -t, --tld-file TLD_FILE
                        Custom TLD file (default: fetch from IANA)
  -v, --verbose         Enable verbose output

```
---

<h3 align="center">Usage</h3>

```yaml
# Single keyword
tldx -k google

# Keyword file
tldx -kf keywords.txt

# Save output
tldx -k admin -o targets.txt

# Custom TLD list
tldx -k test -t custom_tlds.txt

# Verbose mode
tldx -k dev -v
```
### Example

```yaml
# Generate government domains
tldx -k google | head -5
google.aaa
google.aarp
google.abb
google.abbott
google.abbvie

# Pipe to DNS resolver
tldx -k "api.google" | dnsx -silent

# Full recon workflow
tldx -kf keywords.txt | httpx -silent | nuclei -t vulnerabilities/
```
