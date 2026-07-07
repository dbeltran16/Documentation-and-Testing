import unittest

from flask import Flask, jsonify


class TestMechanics(unittest.TestCase):
	def setUp(self):
		self.app = Flask(__name__)
		self.app.config["TESTING"] = True
		self.mechanics = [
			{"id": 1, "name": "Mike Turner", "specialty": "Engine"},
			{"id": 2, "name": "Sara Lee", "specialty": "Brakes"},
			{"id": 3, "name": "David Kim", "specialty": "Electrical"},
		]

		@self.app.route("/mechanics")
		def mechanics():
			return jsonify(self.mechanics), 200

		@self.app.route("/mechanics/<int:mechanic_id>")
		def mechanic_detail(mechanic_id):
			mechanic = next((m for m in self.mechanics if m["id"] == mechanic_id), None)
			if mechanic is None:
				return jsonify({"message": "not found"}), 404
			return jsonify(mechanic), 200

		self.client = self.app.test_client()

	def test_get_mechanics_success(self):
		response = self.client.get("/mechanics")
		self.assertEqual(response.status_code, 200)
		self.assertGreaterEqual(len(response.get_json()), 3)

	def test_mechanic_not_found(self):
		response = self.client.get("/mechanics/9999")
		self.assertEqual(response.status_code, 404)

