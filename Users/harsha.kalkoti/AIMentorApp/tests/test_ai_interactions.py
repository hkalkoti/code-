# tests/test_ai_interactions.py
import unittest
from unittest.mock import patch
from aimentorapp.ai_interactions import AIInteraction

class TestAIInteraction(unittest.TestCase):
    def test_interact(self):
        ai = AIInteraction()
        ai.interact("testuser")
        self.assertTrue(True)

    @patch('builtins.input', return_value='Yes')
    def test_ask_question(self, mock_input):
        ai = AIInteraction()
        response = ai.ask_question("Do you like AI?")
        self.assertEqual(response, "Yes")

if __name__ == "__main__":
    unittest.main()