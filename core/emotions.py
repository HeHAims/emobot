# core/emotions.py

class EmotionEngine:
    def __init__(self):
        self.stress_level = 0.0
        self.emotional_state = {
            "curiosity": 0.7,
            "confidence": 0.5,
            "frustration": 0.0,
            "playfulness": 0.3
        }
        self.decay_rate = 0.95
    
    def update_stress(self, amount):
        self.stress_level = min(1.0, self.stress_level + amount)
        # Update emotional states based on stress
        if self.stress_level > 0.7:
            self.emotional_state["frustration"] = min(1.0, 
                self.emotional_state["frustration"] + 0.2)
            self.emotional_state["confidence"] *= 0.8
    
    def current_mood(self):
        # Apply decay
        for emotion in self.emotional_state:
            self.emotional_state[emotion] *= self.decay_rate
        
        # Return dominant emotion
        return max(self.emotional_state.items(), key=lambda x: x[1])[0]
    
    def record_interaction(self, success):
        if success:
            self.emotional_state["confidence"] = min(1.0,
                self.emotional_state["confidence"] + 0.1)
        else:
            self.emotional_state["frustration"] = min(1.0,
                self.emotional_state["frustration"] + 0.15)