import unittest
from models.model import train_model, load_model, predict
import os

class TestModel(unittest.TestCase):
    def setUp(self):
        if not os.path.exists("models/model.joblib"):
            train_model()
        self.model = load_model()

    def test_prediction_output(self):
        result = predict(self.model, "USA", "2025-12-01")
        self.assertIn("predicted_revenue", result)
        self.assertGreater(result["predicted_revenue"], 0)

    def test_invalid_date(self):
        result = predict(self.model, "USA", "invalid-date")
        self.assertIn("error", result)

    def test_unknown_country(self):
        result = predict(self.model, "Atlantis", "2025-12-01")
        self.assertIn("predicted_revenue", result)  # OneHotEncoder handle_unknown='ignore'

if __name__ == "__main__":
    unittest.main()
