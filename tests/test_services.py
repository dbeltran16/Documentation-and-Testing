import unittest

from flask import Flask, jsonify


class TestServices(unittest.TestCase):
	def setUp(self):
		self.app = Flask(__name__)
		self.app.config["TESTING"] = True
		self.services = [
			{"id": 1, "name": "Oil Change", "price": 49.99},
			{"id": 2, "name": "Tire Rotation", "price": 39.99},
			{"id": 3, "name": "Brake Inspection", "price": 59.99},
		]

		@self.app.route("/services")
		def services():
			return jsonify(self.services), 200

		@self.app.route("/services/<int:service_id>")
		def service_detail(service_id):
			service = next((s for s in self.services if s["id"] == service_id), None)
			if service is None:
				return jsonify({"message": "not found"}), 404
			return jsonify(service), 200

		self.client = self.app.test_client()

	def test_get_services_success(self):
		response = self.client.get("/services")
		self.assertEqual(response.status_code, 200)
		self.assertGreaterEqual(len(response.get_json()), 3)

	def test_service_not_found(self):
		response = self.client.get("/services/9999")
		self.assertEqual(response.status_code, 404)

