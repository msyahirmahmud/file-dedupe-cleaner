# 🧹 File Dedupe Cleaner CLI

[![Build Status](https://github.com/msyahirmahmud/file-dedupe-cleaner/actions/workflows/ci.yml/badge.svg)](https://github.com/msyahirmahmud/file-dedupe-cleaner/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Tests Passing](https://img.shields.io/badge/Tests-100%25-brightgreen.svg)]()

> Fast CLI tool to scan directories, identify duplicate files using SHA-256 cryptographic hashing, and calculate reclaimable disk storage space.

---

## 🌟 Features

- **🔒 SHA-256 Hashing**: Accurate duplicate file matching regardless of filename changes.
- **💾 Storage Reclaim Metrics**: Calculates total wasted bytes across duplicate sets.
- **⚡ Zero External Dependencies**: Runs out of the box using Python's standard library.

---

## 🚀 Quick Start

```bash
git clone https://github.com/msyahirmahmud/file-dedupe-cleaner.git
cd file-dedupe-cleaner
python3 main.py /path/to/scan
```

Run test suite:
```bash
python3 -m unittest discover tests
```

---

## 📄 License

[MIT License](LICENSE)
