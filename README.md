# paypal-payments-flask

Create a simple purchase order using the PayPal REST api with a Flask application.

## Requirements

- A personal or business PayPal account.
- Have an application created in PayPal Developer to have access to client_id and secret_client credentials.
  - [PayPal Developer - Home Page](https://developer.paypal.com/home/)
- Have Python installed.

## Built with

This project was made with Python and the Flask micro framework, and consuming the PayPal REST api.

## How to run the application?

1. Download the repository.

```Shell
$ git clone https://github.com/Remy349/paypal-payments-flask
```

2. Move to the repository and activate a Python virtual environment to install the necessary dependencies.

```Shell
$ cd paypal-payments-flask
# It may be just pip depending on how you installed Python on your computer.
$ python3 -m venv venv

# Linux
$ . venv/bin/activate
# Windows
$ venv\Scripts\activate
```

3. Install the dependencies found in the requirements.txt file.

```Shell
# It may be just "pip" depending on how you installed Python on your computer.
(venv) $ pip3 install -r requirements.txt
```

4. Create an ".env" file in the root of the project to add your environment variables.

```Shell
SECRET_KEY=ab07778a3653971df13e144d26315afb
# When in production use this "https://api-m.paypal.com".
PAYPAL_API_URL=https://api-m.sandbox.paypal.com
PAYPAL_CLIENT_ID=
PAYPAL_CLIENT_SECRET=
```

You get the credentials by creating an application in the PayPal Developer panel, log in with your personal or business PayPal account.

5. Run the application and test purchase.

```Shell
(venv) $ flask run

* Serving Flask app 'application.py'
* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

### Developed by Santiago de Jesús Moraga Caldera - Remy349(GitHub)
