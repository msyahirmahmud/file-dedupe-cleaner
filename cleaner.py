"""
SHA-256 Duplicate File Scanner & Directory Cleaner Engine
"""

import hashlib
import os

class FileDeduper:
    def __init__(self):
        pass

    def compute_sha256(self, file_path: str, chunk_size: int = 65536) -> str:
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(chunk_size):
                sha256.update(chunk)
        return sha256.hexdigest()

    def scan_directory(self, dir_path: str) -> dict:
        if not os.path.exists(dir_path):
            raise ValueError(f"Directory does not exist: {dir_path}")

        hashes = {} # hash -> list of file paths
        for root, _, files in os.walk(dir_path):
            for file in files:
                full_path = os.path.join(root, file)
                try:
                    h = self.compute_sha256(full_path)
                    if h not in hashes:
                        hashes[h] = []
                    hashes[h].append(full_path)
                except (PermissionError, OSError):
                    continue

        # Filter only entries with duplicate count > 1
        duplicates = {h: paths for h, paths in hashes.items() if len(paths) > 1}
        return duplicates

    def calculate_reclaimable_bytes(self, duplicates: dict) -> int:
        total_bytes = 0
        for h, paths in duplicates.items():
            if paths:
                file_size = os.path.getsize(paths[0])
                total_bytes += file_size * (len(paths) - 1)
        return total_bytes
