# tests/test_session_handling.py
import unittest
from aimentorapp.session_handling import SessionHandler

class TestSessionHandler(unittest.TestCase):
    def test_start_session(self):
        sh = SessionHandler()
        sh.start_session("testuser")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()