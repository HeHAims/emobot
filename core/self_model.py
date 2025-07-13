# core/self_model.py

class SelfModel:
    def __init__(self):
        self.skills = {
            "algebra": 0.5,
            "calculus": 0.3,
            "geometry": 0.4,
            "statistics": 0.2
        }
        self.confidence = 0.5
        self.learning_style = "balanced"  # visual, verbal, detailed, quick
        self.symbol_competency = {}  # Track understanding of specific symbols
    
    def update_engagement(self, domain):
        if domain in self.skills:
            # Learning curve - faster improvement at lower levels
            improvement = 0.05 * (1 - self.skills[domain])
            self.skills[domain] = min(1.0, self.skills[domain] + improvement)
            self.confidence = min(1.0, self.confidence + improvement * 0.3)
    
    def update_symbol_understanding(self, symbol, success):
        current = self.symbol_competency.get(symbol, 0.5)
        if success:
            new_value = min(1.0, current + 0.1)
        else:
            new_value = max(0.0, current - 0.1)
        self.symbol_competency[symbol] = new_value