
import unittest
import subprocess
import sys
from pathlib import Path

MAIN_FILE = Path(__file__).resolve().parent.parent / "main.py"


class TestStudentTaskManager(unittest.TestCase):

    def run_app(self, user_input):
        result = subprocess.run(
            [sys.executable, str(MAIN_FILE)],
            input=user_input,
            capture_output=True,
            text=True
        )
        return result.stdout

    def test_add_task(self):
        output = self.run_app("1\nMath Assignment\n5\n")
        self.assertIn("Task added successfully!", output)

    def test_complete_task(self):
        output = self.run_app("1\nMath Assignment\n3\n1\n5\n")
        self.assertIn("Task marked as completed!", output)

    def test_delete_task(self):
        output = self.run_app("1\nMath Assignment\n4\n1\ny\n5\n")
        self.assertIn("deleted successfully!", output)


if __name__ == "__main__":
    unittest.main()
