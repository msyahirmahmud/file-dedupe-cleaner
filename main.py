import sys
import os
from cleaner import FileDeduper

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f"🔍 Scanning directory for duplicate files: {os.path.abspath(target)}")
    
    deduper = FileDeduper()
    dups = deduper.scan_directory(target)
    reclaimable = deduper.calculate_reclaimable_bytes(dups)

    print(f"Found {len(dups)} sets of duplicate files.")
    print(f"Reclaimable Storage: {reclaimable} bytes\n")

    for h, paths in dups.items():
        print(f"Hash: {h[:12]}...")
        for p in paths:
            print(f"  - {p}")

if __name__ == "__main__":
    main()
