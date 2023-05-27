import os
import requests
from flask import Blueprint, jsonify, render_template, url_for

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET"])
def index():
    return render_template("main/index.html")


@bp.route("/create-order", methods=["GET"])
def create_order():
    client = os.getenv("PAYPAL_API_CLIENT")
    secret = os.getenv("PAYPAL_API_SECRET")

    data = {
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "amount": {
                    "currency_code": "USD",
                    "value": "100.00",
                },
                "items": [
                    {
                        "name": "Test",
                        "description": "Test para una compra usando la RESTApi de PayPal",
                        "quantity": "1",
                        "unit_amount": {
                            "currency_code": "USD",
                            "value": "100.00",
                        },
                    }
                ],
            }
        ],
        "payment_source": {
            "paypal": {
                "experience_context": {
                    "brand_name": "Mi tienda de prueba",
                    "landing_page": "NO_PREFERENCE",
                    "user_action": "PAY_NOW",
                    "return_url": "/capture-order",
                    "cancel_url": "/cancel-order",
                }
            }
        },
    }

    response = requests.post(
        f"{os.getenv('PAYPAL_API_URL')}/v1/oauth2/token",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        },
        auth=(client, secret),
        data={"grant_type": "client_credentials"},
    )

    response_json = response.json()

    access_token = response_json["access_token"]

    order_response = requests.post(
        f"{os.getenv('PAYPAL_API_URL')}/v2/checkout/orders",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        },
    )

    print(order_response.content)

    return jsonify(data)


@bp.route("/capture-order", methods=["GET"])
def capture_order():
    return "Capture Order"


@bp.route("/cancel-order", methods=["GET"])
def cancel_order():
    return "Cancel Order"
