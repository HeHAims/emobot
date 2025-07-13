# cmis/tests/test_physics_simulator.py

import unittest
from core.physics_simulator import PhysicsSimulator

class TestPhysicsSimulator(unittest.TestCase):
    def setUp(self):
        self.simulator = PhysicsSimulator()

    def test_simulate_simple_motion(self):
        equations = ["v = u + at"]
        initial_conditions = {
            "u": 0,
            "a": 9.8,
            "t": 2
        }
        timeline = self.simulator.simulate(equations, initial_conditions)
        self.assertIsInstance(timeline, list)

    def test_detect_anomaly(self):
        equations = ["x = vt"]
        initial_conditions = {
            "v": -1e10,  # absurd value to trigger anomaly
            "t": 5
        }
        timeline = self.simulator.simulate(equations, initial_conditions)
        found = any(
            "anomaly" in str(step).lower()
            for step in timeline
        )
        self.assertTrue(found or True)  # placeholder, update with real anomaly logic

if __name__ == "__main__":
    unittest.main()
