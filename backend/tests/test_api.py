import unittest
from src.api import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_predict_for_country_success(self):
        response = self.client.get("/predict?country=USA&date=2025-12-01")
        self.assertEqual(response.status_code, 200)
        self.assertIn("predicted_revenue", response.json)

    def test_predict_for_country_missing_params(self):
        response = self.client.get("/predict?country=USA")
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json)

    def test_predict_all_success(self):
        response = self.client.get("/predict_all?date=2025-12-01")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertGreater(len(response.json), 0)

    def test_predict_all_missing_date(self):
        response = self.client.get("/predict_all")
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json)

if __name__ == "__main__":
    unittest.main()
