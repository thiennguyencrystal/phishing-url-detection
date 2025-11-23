# src/features/host_features.py

import re
from urllib.parse import urlparse
import tldextract 

# --- HÀM PHỤ TRỢ ---
def ensure_scheme(url: str) -> str:
    if not url.startswith(('http://', 'https://')):
        return 'http://' + url
    return url

# --- CÁC HÀM ĐẶC TRƯNG ---

def has_ip_address_in_hostname(url: str) -> int:
    try:
        url = ensure_scheme(url)
        hostname = urlparse(url).hostname
        if hostname is None:
            return 0
        ip_pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        if ip_pattern.match(hostname):
            return 1
        return 0
    except:
        return 0

def get_subdomain_count(url: str) -> int:
    try:
        url = ensure_scheme(url)
        extracted = tldextract.extract(url)
        if extracted.subdomain:
            return len(extracted.subdomain.split('.'))
        return 0
    except:
        return 0

# Vô hiệu hóa WHOIS
def get_domain_age_days(url: str) -> int:
    return -1

def get_domain_lifespan_days(url: str) -> int:
    return -1