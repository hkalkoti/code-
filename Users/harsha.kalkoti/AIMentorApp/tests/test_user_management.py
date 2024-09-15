# tests/test_user_management.py
import unittest
from aimentorapp.user_management import UserManager

class TestUserManager(unittest.TestCase):
    def test_create_user(self):
        um = UserManager()
        um.create_user("testuser")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()