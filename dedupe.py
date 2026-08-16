"""
SHA-256 Duplicate File Finder & Cleaner Module
"""

import hashlib
import os

class FileDedupeCleaner:
    def __init__(self):
        self.hashes = {} # hash -> list of file paths

    def compute_file_hash(self, file_path: str, block_size: int = 65536) -> str:
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for block in iter(lambda: f.read(block_size), b''):
                sha256.update(block)
        return sha256.hexdigest()

    def scan_directory(self, target_dir: str, ext_filter: str = None) -> dict:
        if not os.path.exists(target_dir):
            raise ValueError(f"Target directory does not exist: {target_dir}")

        self.hashes = {}
        for root, _, files in os.walk(target_dir):
            for file in sorted(files):
                if ext_filter and not file.lower().endswith(ext_filter.lower()):
                    continue
                file_path = os.path.join(root, file)
                try:
                    file_hash = self.compute_file_hash(file_path)
                    if file_hash not in self.hashes:
                        self.hashes[file_hash] = []
                    self.hashes[file_hash].append(file_path)
                except (OSError, PermissionError):
                    continue

        # Filter only hashes with duplicates (>1 files)
        duplicates = {h: paths for h, paths in self.hashes.items() if len(paths) > 1}
        return duplicates

    def remove_duplicates(self, duplicates: dict, keep_first: bool = True) -> int:
        removed_count = 0
        for hash_val, paths in duplicates.items():
            if len(paths) <= 1:
                continue
            to_remove = paths[1:] if keep_first else paths[:-1]
            for file_path in to_remove:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    removed_count += 1
        return removed_count
