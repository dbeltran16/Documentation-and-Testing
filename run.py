from flask import Flask, jsonify, request


app = Flask(__name__)


CUSTOMERS = [
	{"id": 1, "name": "John Doe", "email": "john@example.com"},
	{"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
	{"id": 3, "name": "Alex Brown", "email": "alex@example.com"},
	{"id": 4, "name": "Maria Davis", "email": "maria@example.com"},
]

MECHANICS = [
	{"id": 1, "name": "Mike Turner", "specialty": "Engine"},
	{"id": 2, "name": "Sara Lee", "specialty": "Brakes"},
	{"id": 3, "name": "David Kim", "specialty": "Electrical"},
]

SERVICES = [
	{"id": 1, "name": "Oil Change", "price": 49.99},
	{"id": 2, "name": "Tire Rotation", "price": 39.99},
	{"id": 3, "name": "Brake Inspection", "price": 59.99},
]


@app.route("/", methods=["GET"])
def home():
	return jsonify({"message": "Documentation and Testing API is running"}), 200


@app.route("/customers", methods=["GET"])
def get_customers():
	return jsonify(CUSTOMERS), 200


@app.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
	customer = next((c for c in CUSTOMERS if c["id"] == customer_id), None)
	if customer is None:
		return jsonify({"message": "not found"}), 404
	return jsonify(customer), 200


@app.route("/customers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
	data = request.get_json(silent=True) or {}
	if not data.get("name"):
		return jsonify({"message": "bad request"}), 400

	customer = next((c for c in CUSTOMERS if c["id"] == customer_id), None)
	if customer is None:
		return jsonify({"message": "not found"}), 404

	customer["name"] = data["name"]
	if data.get("email"):
		customer["email"] = data["email"]

	return jsonify({"message": "customer updated", "customer": customer}), 200


@app.route("/mechanics", methods=["GET"])
def get_mechanics():
	return jsonify(MECHANICS), 200


@app.route("/services", methods=["GET"])
def get_services():
	return jsonify(SERVICES), 200


if __name__ == "__main__":
	app.run(debug=True)
