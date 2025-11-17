# src/features/host_features.py (Phiên bản Sửa lỗi Cuối cùng)

import re
import whois
from datetime import datetime
from urllib.parse import urlparse
import tldextract 
import time  # Import thư viện time

# Cấu hình lại thư viện whois để kiên nhẫn hơn
whois.NICClient.TIMEOUT = 10  # Tăng thời gian chờ lên 10 giây 
# DÒNG GÂY LỖI "WHOIS_QUIRKS" ĐÃ BỊ XÓA VĨNH VIỄN

def has_ip_address_in_hostname(url: str) -> int:
    """16. Kiểm tra xem hostname có phải là một địa chỉ IP không."""
    try:
        hostname = urlparse(url).hostname
        if hostname is None:
             return 0
        ip_pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        if ip_pattern.match(hostname):
            return 1
        return 0
    except Exception:
        return 0

def get_subdomain_count(url: str) -> int:
    """17. Đếm số lượng subdomain một cách chính xác."""
    try:
        extracted = tldextract.extract(url)
        if extracted.subdomain:
            return len(extracted.subdomain.split('.'))
        return 0
    except Exception:
        return 0

def get_domain_age_days(url: str) -> int:
    """
    18. VÔ HIỆU HÓA - Luôn trả về -1 để tránh lỗi thư viện whois.
    """
    return -1

def get_domain_lifespan_days(url: str) -> int:
    """
    19. VÔ HIỆU HÓA - Luôn trả về -1 để tránh lỗi thư viện whois.
    """
    return -1