# core/assistant.py

class MathTutor:
    def __init__(self, memory, emotions, goals, self_model, translator):
        self.memory = memory
        self.emotions = emotions
        self.goals = goals
        self.self_model = self_model
        self.translator = translator

    def explain_formula(self, formula):
        complexity = self.translator.calculate_complexity(formula)
        domain = self.translator.identify_domain(formula)

        self.emotions.update_stress(complexity * 0.5)
        self.self_model.update_engagement(domain)

        similar_formulas = self.memory.recall_similar(formula, domain)
        self.memory.consolidate(formula, {
            "domain": domain,
            "complexity": complexity
        })

        explanation = self.translator.translate(formula, level="intermediate")

        similar_text = ""
        if similar_formulas:
            unique_formulas = list(dict.fromkeys(similar_formulas))
            clean_examples = [
                f.replace('"', '^')
                 .replace('~', '')
                 .strip()
                for f in unique_formulas
            ]
            similar_text = "\nExamples you've seen:\n" + "\n".join(clean_examples)

        return explanation + similar_text


class EmoBot(MathTutor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_formula = None

    def explain_formula(self, formula):
        self.last_formula = formula

        raw_explanation = super().explain_formula(formula)

        if not raw_explanation.strip():
            raw_explanation = "(no translation available)"

        styled_explanation = self._apply_emotional_style(raw_explanation)
        return styled_explanation

    def handle_user_feedback(self, feedback):
        if not self.last_formula:
            return "I don't have a formula to explain yet."

        feedback = feedback.lower()

        if "simpler" in feedback:
            return f"I'll simplify...\n{self.explain_formula(self.last_formula)}"

        if "more" in feedback:
            return f"Here's more detail...\n{self.explain_formula(self.last_formula)}"

        return f"Let me try a different explanation...\n{self.explain_formula(self.last_formula)}"

    def _apply_emotional_style(self, explanation):
        mood = self.emotions.current_mood()

        if mood == "frustration":
            return f"\n*Sigh* Look, it's {explanation}. Got it?"
        elif mood == "confidence":
            return f"\nAbsolutely! {explanation.capitalize()}!"
        elif mood == "playfulness":
            return f"\n✨ Ta-da! {explanation} ✨"
        else:
            return f"\nHmm... {explanation}... interesting, right?"
