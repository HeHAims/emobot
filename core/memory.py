# core/memory.py

from collections import defaultdict, deque

class Memory:
    def __init__(self, capacity=100):
        self.storage = deque(maxlen=capacity)
        self.concept_counts = defaultdict(int)
        self.symbol_counts = defaultdict(int)

    def recall_similar(self, formula, domain):
        # Simple similarity: formulas with same domain
        return [f for f, ctx in self.storage if ctx.get("domain") == domain][:3]

    def consolidate(self, formula, context):
        self.storage.append((formula, context))
        domain = context.get("domain", "unknown")
        self.concept_counts[domain] += 1

        for symbol in formula:
            if symbol in "∫∑∂θπ+-*/^":
                self.symbol_counts[symbol] += 1

    def get_concept_count(self, concept):
        return self.concept_counts.get(concept, 0)

    def get_symbol_count(self, symbol):
        return self.symbol_counts.get(symbol, 0)
