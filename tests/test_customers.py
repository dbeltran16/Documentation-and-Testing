import unittest

from flask import Flask, jsonify, request


class TestCustomers(unittest.TestCase):
	def setUp(self):
		self.app = Flask(__name__)
		self.app.config["TESTING"] = True
		self.customers = [
			{"id": 1, "name": "John Doe", "email": "john@example.com"},
			{"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
			{"id": 3, "name": "Alex Brown", "email": "alex@example.com"},
			{"id": 4, "name": "Maria Davis", "email": "maria@example.com"},
		]

		@self.app.route("/customers", methods=["GET", "POST"])
		def customers():
			if request.method == "POST":
				payload = request.get_json(silent=True) or {}
				if not payload.get("name"):
					return jsonify({"message": "bad request"}), 400

				new_customer = {
					"id": len(self.customers) + 1,
					"name": payload["name"],
					"email": payload.get("email", ""),
				}
				self.customers.append(new_customer)
				return jsonify(new_customer), 201

			return jsonify(self.customers), 200

		@self.app.route("/customers/<int:customer_id>", methods=["GET", "PUT", "DELETE"])
		def customer_detail(customer_id):
			customer = next((c for c in self.customers if c["id"] == customer_id), None)
			if customer is None:
				return jsonify({"message": "not found"}), 404

			if request.method == "PUT":
				payload = request.get_json(silent=True) or {}
				if not payload.get("name"):
					return jsonify({"message": "bad request"}), 400
				customer["name"] = payload["name"]
				return jsonify({"message": "customer updated"}), 200

			if request.method == "DELETE":
				self.customers = [c for c in self.customers if c["id"] != customer_id]
				return jsonify({"message": "customer deleted"}), 200

			return jsonify(customer), 200

		self.client = self.app.test_client()

	def test_get_customers(self):
		response = self.client.get("/customers")
		self.assertEqual(response.status_code, 200)
		self.assertGreaterEqual(len(response.get_json()), 4)

	def test_create_customer_success(self):
		response = self.client.post("/customers", json={"name": "John Doe"})
		self.assertEqual(response.status_code, 201)

	def test_update_customer(self):
		response = self.client.put(
			"/customers/1",
			json={
				"name": "Jane Doe"
			},
		)
		self.assertEqual(response.status_code, 200)

	def test_delete_customer(self):
		response = self.client.delete("/customers/1")
		self.assertEqual(response.status_code, 200)

	def test_create_customer_missing_name(self):
		response = self.client.post(
			"/customers",
			json={
				"email": "john@email.com"
			},
		)
		self.assertEqual(response.status_code, 400)

	def test_customer_not_found(self):
		response = self.client.get("/customers/9999")
		self.assertEqual(response.status_code, 404)

