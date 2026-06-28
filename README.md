<!-- <svg xmlns="http://www.w3.org/2000/svg" width="420" height="160" viewBox="0 0 420 160">
  <rect width="100%" height="100%" fill="#0d1117"/>

  <text
    x="20"
    y="35"
    fill="red"
    font-family="monospace"
    font-size="18"
    xml:space="preserve">
<tspan x="20" dy="0"> _      _       _          </tspan>
<tspan x="20" dy="22">| |   | |     | |         </tspan>
<tspan x="20" dy="22">| |_  | |   __| | __  __  </tspan>
<tspan x="20" dy="22">| __| | |  / _` | \ \/ /  </tspan>
<tspan x="20" dy="22">| |_  | | | (_| |  >  <   </tspan>
<tspan x="20" dy="22"> \__| |_|  \__,_| /_/\_\  </tspan>
  </text>
</svg> -->
<div align="center">
<h1>TLDX</h1>
<p>Top Level Domain(TLD) Expansion Tool for Bug Bounty</p>
</div>

---
Expand keywords across all TLDs to discover hidden assets during reconnaissance.

### Features
- Generate domain permutations (keyword + TLD)
- Supports single keywords or keyword files
- Uses official IANA TLD list
- Custom TLD lists support
- Output to console or file

### Installation
```bash
pip install tldx
```
### Usage
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

```yaml
tldx/
├── setup.py
├── requirements.txt
├── README.md
├── tldx/
│   ├── __init__.py
│   ├── cli.py
│   └── core.py
└── tests/
    └── test_tldx.py
```
