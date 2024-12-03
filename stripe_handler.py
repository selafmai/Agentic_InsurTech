import stripe
import os
from typing import Dict

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

async def process_payment(amount: float, currency: str = "EUR") -> Dict:
    """Procesira plačilo preko Stripe."""
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),  # Stripe uporablja najmanjše denarne enote
            currency=currency,
            payment_method_types=["card"],
            metadata={"type": "insurance_payment"}
        )
        
        return {
            "client_secret": intent.client_secret,
            "status": "success"
        }
    except stripe.error.StripeError as e:
        return {
            "status": "error",
            "message": str(e)
        }

def create_checkout_session(amount: float, currency: str = "EUR"):
    """Ustvari Stripe Checkout sejo."""
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": currency,
                "product_data": {
                    "name": "Zavarovanje",
                },
                "unit_amount": int(amount * 100),
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url="http://localhost:8501/success",
        cancel_url="http://localhost:8501/cancel",
    )
    
    return session 