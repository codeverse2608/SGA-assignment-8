from flask import Flask, jsonify, request

app = Flask(__name__)

menu = {
    "Poha": 30,
    "Tea": 15,
    "Sandwich": 50
}

@app.route("/api/menu", methods=["GET"])
def get_menu():
    return jsonify(menu)


@app.route("/menu", methods=["GET"])
def menu_page():
    # We build a simple HTML page dynamically from the menu dictionary
    html_content = "<h1>Canteen Menu</h1><ul>"
    for item, price in menu.items():
        html_content += f"<li>{item} - {price}</li>"
    html_content += "</ul>"
    
    return html_content

@app.route("/order", methods=["POST"])
def place_order():
    order = request.get_json()

    item = order["item"]
    qty = order["quantity"]

    if item not in menu:
        return jsonify({"error": "Item not found"}), 404

    if not isinstance(qty, int) or isinstance(qty, bool) or qty <= 0:
        return jsonify({"error": "Quantity must be a positive integer"}), 400

    total = menu[item] * qty

    return jsonify({
        "order_id": 101,
        "item": item,
        "quantity": qty,
        "total": total,
        "status": "Order Placed"
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)