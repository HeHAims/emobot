# core/utils.py

def calculate_complexity(formula):
    return min(1.0, len(formula) / 30.0)

def identify_domain(formula):
    if "∫" in formula:
        return "calculus"
    return "algebra"
