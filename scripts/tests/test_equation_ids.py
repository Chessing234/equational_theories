import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from find_equation_id import Equation


class EquationIdTests(unittest.TestCase):
    def test_rejects_nonpositive_ids(self):
        for eq_id in (0, -1, -100):
            with self.subTest(eq_id=eq_id):
                with self.assertRaisesRegex(ValueError, "positive"):
                    Equation.from_id(eq_id)

    def test_positive_ids_round_trip(self):
        for eq_id in (1, 2, 3, 10, 100, 4694):
            with self.subTest(eq_id=eq_id):
                self.assertEqual(Equation.from_id(eq_id).id, eq_id)
