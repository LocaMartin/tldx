import sys
import requests

def fetch_tlds(tld_file=None):
    """Fetch TLDs from IANA or custom file"""
    if tld_file:
        try:
            with open(tld_file, 'r') as f:
                return [line.strip().lower() for line in f 
                        if line.strip() and not line.startswith('#')]
        except FileNotFoundError:
            sys.exit(f"Error: TLD file {tld_file} not found")
    else:
        url = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return [
                line.strip().lower() 
                for line in response.text.splitlines() 
                if line.strip() and not line.startswith('#')
            ]
        except requests.exceptions.RequestException as e:
            sys.exit(f"Failed to fetch TLD data: {str(e)}")

def load_keywords(keyword=None, keyword_file=None):
    """Load keywords from input sources"""
    keywords = []
    if keyword:
        keywords.append(keyword.strip().lower())
    if keyword_file:
        try:
            with open(keyword_file, 'r') as f:
                keywords.extend([line.strip().lower() for line in f if line.strip()])
        except FileNotFoundError:
            sys.exit(f"Error: Keyword file {keyword_file} not found")
    return keywords

def generate_combinations(keywords, tlds):
    """Generate keyword-tld combinations"""
    for keyword in keywords:
        for tld in tlds:
            yield f"{keyword}.{tld}"

def load_tlds(tld_file=None):
    """Load TLDs without exiting on fetch or file errors."""
    try:
        return fetch_tlds(tld_file)
    except SystemExit:
        return []

def expand_keyword(keyword, tld_list=None):
    """Expand a single keyword across available TLDs."""
    if not keyword:
        return []

    tlds = load_tlds(tld_list)
    return list(generate_combinations([keyword.strip().lower()], tlds))

def expand_keywords_from_file(keyword_file, tld_list=None):
    """Expand keywords from a file across available TLDs."""
    try:
        keywords = load_keywords(keyword_file=keyword_file)
    except SystemExit:
        return []

    tlds = load_tlds(tld_list)
    return list(generate_combinations(keywords, tlds))
