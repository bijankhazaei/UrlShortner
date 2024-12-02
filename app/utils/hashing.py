import hashlib

def generate_short_url(original_url: str) -> str:
    return hashlib.md5(original_url.encode()).hexdigest()[:6]