import json
import os
import hashlib

CACHE_FILE = "outputs/cache.json"


def get_file_hash(file_bytes):
    return hashlib.md5(file_bytes).hexdigest()


def load_cache():
    # If cache file does not exist
    if not os.path.exists(CACHE_FILE):
        return {}

    # If cache file is empty
    if os.path.getsize(CACHE_FILE) == 0:
        return {}

    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # If cache file is corrupted
        return {}


def save_cache(cache):
    os.makedirs("outputs", exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
