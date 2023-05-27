import os
import requests
import base64
from flask import Blueprint, jsonify, render_template

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET"])
def index():
    return render_template("main/index.html")


@bp.route("/create-order", methods=["GET"])
def create_order():
    api_url = os.getenv("PAYPAL_API_URL")
    client_id = os.getenv("PAYPAL_CLIENT_ID")
    client_secret = os.getenv("PAYPAL_CLIENT_SECRET")

    access_token = get_access_token(api_url, client_id, client_secret)

    json = {
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "items": [
                    {
                        "name": "Testing Payment",
                        "description": "Testing a payment using PayPal",
                        "quantity": "1",
                        "unit_amount": {
                            "currency_code": "USD",
                            "value": "100.00",
                        },
                    },
                ],
                "amount": {
                    "currency_code": "USD",
                    "value": "100.00",
                    "breakdown": {
                        "item_total": {
                            "currency_code": "USD",
                            "value": "100.00",
                        }
                    },
                },
            }
        ],
        "application_context": {
            "brand_name": "My testing app",
            "landing_page": "NO_PREFERENCE",
            "user_action": "PAY_NOW",
            "return_url": "http://localhost:5000/capture-order",
            "cancel_url": "http://localhost:5000/cancel-order",
        },
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.post(
        f"{api_url}/v2/checkout/orders",
        headers=headers,
        json=json,
    )

    return jsonify(response.json())


@bp.route("/capture-order", methods=["GET"])
def capture_order():
    return "Capture Order"


@bp.route("/cancel-order", methods=["GET"])
def cancel_order():
    return "Cancel Order"


def get_access_token(api_url, client_id, client_secret):
    basic_auth = base64.b64encode(
        f"{client_id}:{client_secret}".encode(),
    ).decode()

    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {basic_auth}",
    }

    response = requests.post(
        f"{api_url}/v1/oauth2/token",
        headers=headers,
        data=data,
    ).json()

    return response["access_token"]
