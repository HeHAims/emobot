import unittest
from core.assistant import EmoBot
from core.math_translator import EnhancedMathTranslator
from core.memory import Memory
from core.emotions import EmotionEngine
from core.self_model import SelfModel
from core.goal_system import GoalSystem

class TestMathTutor(unittest.TestCase):
    def setUp(self):
        memory = Memory()
        emotions = EmotionEngine()
        goals = GoalSystem()
        self_model = SelfModel()
        translator = EnhancedMathTranslator()
        
        self.emo_bot = EmoBot(
            memory,
            emotions,
            goals,
            self_model,
            translator
        )

    def test_explain_simple_formula(self):
        result = self.emo_bot.explain_formula("x + y")
        self.assertIn("plus", result.lower())

    def test_explain_integral(self):
        result = self.emo_bot.explain_formula("∫x dx")
        self.assertIn("integral", result.lower())

    def test_feedback_simpler(self):
        self.emo_bot.last_formula = "∫x dx"
        response = self.emo_bot.handle_user_feedback("simpler")
        self.assertTrue(len(response.strip()) > 0)

if __name__ == "__main__":
    unittest.main()

def _generate_memory_context(self, formula: str) -> str:
    examples = [
        f for f, _ in self.memory.storage
        if f != formula
    ]
    # Remove duplicates
    examples = list(dict.fromkeys(examples))

    if examples:
        clean_examples = [
            f.replace('"', '^')
             .replace('~', '')
             .strip()
            for f in examples
        ]
        return "\nExamples you've seen:\n" + "\n".join(clean_examples)
    return ""
