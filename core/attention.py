# core/attention.py

class AttentionMechanism:
    def __init__(self):
        self.focus = 1.0

    def adjust_focus(self, mood):
        if mood == "frustration":
            self.focus *= 0.7
        else:
            self.focus = min(1.0, self.focus + 0.2)
