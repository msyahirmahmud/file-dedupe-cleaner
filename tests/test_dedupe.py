import unittest
import tempfile
import os
from dedupe import FileDedupeCleaner

class TestFileDedupeCleaner(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.cleaner = FileDedupeCleaner()

        # Create duplicate test files
        self.file1 = os.path.join(self.temp_dir.name, "doc1.txt")
        self.file2 = os.path.join(self.temp_dir.name, "doc2.txt")
        self.file3 = os.path.join(self.temp_dir.name, "image.png")

        with open(self.file1, "w") as f:
            f.write("Identical content for duplicate check")
        with open(self.file2, "w") as f:
            f.write("Identical content for duplicate check")
        with open(self.file3, "w") as f:
            f.write("Identical content for duplicate check")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_remove_duplicates_deletes_redundant_files(self):
        duplicates = self.cleaner.scan_directory(self.temp_dir.name)
        removed = self.cleaner.remove_duplicates(duplicates, keep_first=True)
        self.assertEqual(removed, 2)
        self.assertTrue(os.path.exists(self.file1))
        self.assertFalse(os.path.exists(self.file2))
        self.assertFalse(os.path.exists(self.file3))

    def test_non_existent_directory_raises_error(self):
        with self.assertRaises(ValueError):
            self.cleaner.scan_directory("/invalid/non_existent_path")

if __name__ == '__main__':
    unittest.main()
