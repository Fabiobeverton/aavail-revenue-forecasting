import unittest
import logging
import os

LOG_FILE = "logs/test_log.log"

class TestLogging(unittest.TestCase):
    def setUp(self):
        os.makedirs("logs", exist_ok=True)
        logging.basicConfig(
            filename=LOG_FILE,
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s"
        )

    def test_log_file_created(self):
        logging.info("Logging test message")
        self.assertTrue(os.path.exists(LOG_FILE))
        with open(LOG_FILE, "r") as f:
            contents = f.read()
            self.assertIn("Logging test message", contents)

if __name__ == "__main__":
    unittest.main()
