#!/usr/bin/env python3
# main/main.py

import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).parent.parent))

from core.assistant import EmoBot
from core.math_translator import EnhancedMathTranslator
from core.memory import Memory
from core.emotions import EmotionEngine
from core.self_model import SelfModel
from core.goal_system import GoalSystem

def initialize_components():
    """Initialize all CMIS components"""
    print("Initializing CMIS components...")
    
    memory = Memory(capacity=1000)
    emotions = EmotionEngine()
    goals = GoalSystem()
    self_model = SelfModel()
    translator = EnhancedMathTranslator()
    
    # Add initial goals
    goals.add_goal("understand_basic_concepts", priority=0.8)
    goals.add_goal("build_user_confidence", priority=0.7)
    
    emo_bot = EmoBot(memory, emotions, goals, self_model, translator)
    return emo_bot

def main():
    """Main entry point for CMIS"""
    print("\n=== Cognitive Mathematical Intelligence System ===")
    print("Type 'quit' to exit\n")
    
    emo_bot = initialize_components()
    
    while True:
        try:
            user_input = input("\nEnter math formula > ").strip()
            
            if user_input.lower() in ('quit', 'exit'):
                print("\nGoodbye! Come back with more math questions!")
                break
                
            if not user_input:
                print("Please enter a valid math formula")
                continue

            print(f"\nEmoBot: {emo_bot.explain_formula(user_input)}")

            # Feedback loop
            while True:
                feedback = input("\n[Your feedback] > ").strip()

                if feedback.lower() in ('next', ''):
                    break
                elif feedback.lower() == 'quit':
                    print("\nSession ended. Goodbye!")
                    return

                # Check if user typed a new formula
                if any(c.isalpha() for c in feedback) and any(sym in feedback for sym in "+-*/=^∫∂Σ()"):
                    # Looks like a new formula
                    print(f"\nEmoBot: {emo_bot.explain_formula(feedback)}")
                else:
                    print(f"\nEmoBot: {emo_bot.handle_user_feedback(feedback)}")

        except KeyboardInterrupt:
            print("\n\nSession interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try another formula")

if __name__ == "__main__":
    main()
