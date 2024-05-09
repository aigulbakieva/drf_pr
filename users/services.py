import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    title_product = f'{instance.paid_course}' if instance.paid_course else instance.paid_lesson
    product = stripe.Product.create(name=f'{title_product}')
    return product['id']


def create_stripe_price(amount, id):
    """Создает цену в stripe."""
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product=id,
    )


def create_stripe_session(price):
    """Создает сессию в stripe."""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')

