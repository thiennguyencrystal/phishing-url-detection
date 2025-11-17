# src/features/lexical_features.py

from urllib.parse import urlparse

# --- Feature Extraction Functions ---

def get_url_length(url: str) -> int:
    """1. Trả về độ dài của URL."""
    return len(url)

def get_hostname_length(url: str) -> int:
    """2. Trả về độ dài của hostname."""
    try:
        return len(urlparse(url).netloc)
    except Exception:
        return 0

def count_dots(url: str) -> int:
    """3. Đếm số lượng dấu '.' trong URL."""
    return url.count('.')

def count_hyphens(url: str) -> int:
    """4. Đếm số lượng dấu '-' trong hostname."""
    try:
        hostname = urlparse(url).netloc
        return hostname.count('-')
    except Exception:
        return 0

def count_at_symbol(url: str) -> int:
    """5. Đếm số lượng ký tự '@' trong URL."""
    return url.count('@')

# src/features/lexical_features.py

# ... (Giữ 5 hàm cũ ở trên) ...
import re
from urllib.parse import urlparse

# --- Thêm các hàm mới từ đây ---

def count_slashes(url: str) -> int:
    """6. Đếm số lượng dấu '/' trong URL."""
    return url.count('/')

def count_question_mark(url: str) -> int:
    """7. Đếm số lượng dấu '?' trong URL."""
    return url.count('?')

def count_equals(url: str) -> int:
    """8. Đếm số lượng dấu '=' trong URL."""
    return url.count('=')

def count_and_symbol(url: str) -> int:
    """9. Đếm số lượng dấu '&' trong URL."""
    return url.count('&')

def get_path_length(url: str) -> int:
    """10. Trả về độ dài của đường dẫn (path)."""
    try:
        return len(urlparse(url).path)
    except Exception:
        return 0

def count_digits_in_url(url: str) -> int:
    """11. Đếm số lượng chữ số trong toàn bộ URL."""
    return sum(c.isdigit() for c in url)

def count_letters_in_url(url: str) -> int:
    """12. Đếm số lượng chữ cái trong toàn bộ URL."""
    return sum(c.isalpha() for c in url)

def count_digits_in_hostname(url: str) -> int:
    """13. Đếm số lượng chữ số trong hostname."""
    try:
        hostname = urlparse(url).netloc
        return sum(c.isdigit() for c in hostname)
    except Exception:
        return 0

def has_https(url: str) -> int:
    """14. Kiểm tra xem URL có bắt đầu bằng 'https' không."""
    return 1 if url.startswith('https://') else 0

def has_suspicious_tld(url: str) -> int:
    """15. Kiểm tra TLD có nằm trong danh sách đáng ngờ không."""
    suspicious_tlds = ['.xyz', '.top', '.club', '.site', '.online', '.info', '.pw', '.tk']
    try:
        hostname = urlparse(url).netloc
        tld = '.' + hostname.split('.')[-1]
        return 1 if tld in suspicious_tlds else 0
    except Exception:
        return 0