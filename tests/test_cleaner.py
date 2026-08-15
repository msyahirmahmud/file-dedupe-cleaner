import unittest
import tempfile
import os
from cleaner import FileDeduper

class TestFileDeduper(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.deduper = FileDeduper()

        # Create two identical files and one unique file
        self.file1 = os.path.join(self.temp_dir.name, "file1.txt")
        self.file2 = os.path.join(self.temp_dir.name, "file2.txt")
        self.file3 = os.path.join(self.temp_dir.name, "file3.txt")

        with open(self.file1, "w") as f:
            f.write("Hello Duplicate Content")
        with open(self.file2, "w") as f:
            f.write("Hello Duplicate Content")
        with open(self.file3, "w") as f:
            f.write("Unique Content")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_compute_sha256(self):
        h1 = self.deduper.compute_sha256(self.file1)
        h2 = self.deduper.compute_sha256(self.file2)
        h3 = self.deduper.compute_sha256(self.file3)
        self.assertEqual(h1, h2)
        self.assertNotEqual(h1, h3)

    def test_scan_directory_finds_duplicates(self):
        dups = self.deduper.scan_directory(self.temp_dir.name)
        self.assertEqual(len(dups), 1)
        for h, paths in dups.items():
            self.assertEqual(len(paths), 2)

    def test_calculate_reclaimable_bytes(self):
        dups = self.deduper.scan_directory(self.temp_dir.name)
        reclaimable = self.deduper.calculate_reclaimable_bytes(dups)
        self.assertGreater(reclaimable, 0)

if __name__ == '__main__':
    unittest.main()
