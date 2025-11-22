# src/features/lexical_features.py

from urllib.parse import urlparse
import re

# --- HÀM PHỤ TRỢ QUAN TRỌNG ---
def ensure_scheme(url: str) -> str:
    """Đảm bảo URL luôn có http:// để urlparse hoạt động đúng"""
    if not url.startswith(('http://', 'https://')):
        return 'http://' + url
    return url

# --- CÁC HÀM ĐẶC TRƯNG ---

def get_url_length(url: str) -> int:
    return len(url)

def get_hostname_length(url: str) -> int:
    try:
        url = ensure_scheme(url) # Chuẩn hóa trước
        return len(urlparse(url).netloc)
    except:
        return 0

def count_dots(url: str) -> int:
    return url.count('.')

def count_hyphens(url: str) -> int:
    return url.count('-')

def count_at_symbol(url: str) -> int:
    return url.count('@')

def count_slashes(url: str) -> int:
    return url.count('/')

def count_question_mark(url: str) -> int:
    return url.count('?')

def count_equals(url: str) -> int:
    return url.count('=')

def count_and_symbol(url: str) -> int:
    return url.count('&')

def get_path_length(url: str) -> int:
    try:
        url = ensure_scheme(url)
        return len(urlparse(url).path)
    except:
        return 0

def count_digits_in_url(url: str) -> int:
    return sum(c.isdigit() for c in url)

def count_letters_in_url(url: str) -> int:
    return sum(c.isalpha() for c in url)

def count_digits_in_hostname(url: str) -> int:
    try:
        url = ensure_scheme(url)
        hostname = urlparse(url).netloc
        return sum(c.isdigit() for c in hostname)
    except:
        return 0

def has_https(url: str) -> int:
    # Đặc trưng này kiểm tra xem string gốc có https không
    return 1 if url.startswith('https://') else 0

def has_suspicious_tld(url: str) -> int:
    suspicious_tlds = ['.xyz', '.top', '.club', '.site', '.online', '.info', '.pw', '.tk']
    try:
        url = ensure_scheme(url)
        hostname = urlparse(url).netloc
        # Lấy phần đuôi sau dấu chấm cuối cùng
        if '.' in hostname:
            tld = '.' + hostname.split('.')[-1]
            return 1 if tld in suspicious_tlds else 0
        return 0
    except:
        return 0
# ... các hàm cũ ...

def count_sensitive_words(url: str) -> int:
    """
    20. Đếm số lượng từ nhạy cảm thường dùng trong phishing.
    """
    # Danh sách các từ khóa lừa đảo phổ biến
    sensitive_words = [
        'login', 'signin', 'log-in', 'sign-in', 
        'verify', 'verification', 'account', 'update', 
        'confirm', 'security', 'secure', 'banking', 
        'support', 'service', 'auth', 'paypal', 
        'apple', 'microsoft', 'facebook', 'google', 'netflix'
    ]
    
    url_lower = url.lower()
    count = 0
    for word in sensitive_words:
        if word in url_lower:
            count += 1
    return count