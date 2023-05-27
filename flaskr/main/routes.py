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

    # order_response = requests.post(
    #     f"{os.getenv('PAYPAL_API_URL')}/v2/checkout/orders",
    #     data=data,
    #     headers={
    #         "Content-Type": "application/json",
    #         "Authorization": f"Bearer {access_token}",
    #     },
    # )

    # print(order_response.json())

    return jsonify("create-order")


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
