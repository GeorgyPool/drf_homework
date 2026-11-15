import requests
import stripe

from config.settings import SECRET_CURRENCY_API_KEY, SECRET_STRIPE_API_KEY

stripe.api_key = SECRET_STRIPE_API_KEY


def conver_rub_to_usd(amount):
    """Переводит сумму из рублей в доллары"""

    headers = {"apikey": SECRET_CURRENCY_API_KEY}
    params = {"currencies": "RUB"}
    response = requests.get(
        url="https://api.currencyapi.com/v3/latest", headers=headers, params=params
    )
    rate = response.json()["data"]["RUB"]["value"]

    usd_price = int(amount / rate)

    return usd_price


def create_stripe_price(amount):
    """Создает цену в stripe."""
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": "buy"},
    )


def crete_stripe_session(price):
    """Создание сессии для оплаты в stripe."""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price, "quantity": 1}],
        mode="payment",
    )
    return session.id, session.url
