#!/usr/bin/env python3
"""After Stripe payment, grant user access to courses."""
import os, json, hashlib, hmac
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

R2_SECRET = os.getenv('CLOUDFLARE_R2_SECRET_ACCESS_KEY', '')
ACCOUNT_ID = os.getenv('CLOUDFLARE_ACCOUNT_ID')
BUCKET = os.getenv('CLOUDFLARE_R2_BUCKET', 'prime-agent-courses')

PLANS = {
    'founder':  {'name': 'Founder', 'videos': ['module1','module2'], 'months': 6},
    'standard': {'name': 'Standard', 'videos': ['module1','module2','module3','module4','module5'], 'months': 12},
    'pro':      {'name': 'Pro', 'videos': ['module1','module2','module3','module4','module5','module6','module7','module8'], 'months': 999},
    'team':     {'name': 'Team', 'videos': ['module1','module2','module3','module4','module5','module6','module7','module8'], 'seats': 5},
    'business': {'name': 'Business', 'videos': ['module1','module2','module3','module4','module5','module6','module7','module8'], 'seats': 20},
}

def generate_access(email, plan_type, hours=8760):
    plan = PLANS.get(plan_type, PLANS['standard'])
    payload = json.dumps({'email': email, 'plan': plan_type, 'videos': plan['videos'],
                         'exp': (datetime.utcnow() + timedelta(hours=hours)).isoformat()}, sort_keys=True)
    sig = hmac.new(R2_SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return {'token': f"{payload}.{sig}", 'videos': plan['videos']}

def handle_payment(customer_email, price_id):
    price_map = {
        'price_1U3IDGBrWAEI1HPa0rMd9Eu6': 'founder',
        'price_1U3IDHBrWAEI1HPaB0ifC24F': 'standard',
        'price_1U3IDHBrWAEI1HPaDGMfe0LA': 'pro',
        'price_1U3IDIBrWAEI1HPaFS4f7Vxk': 'team',
        'price_1U3IDKBrWAEI1HPa4u9d1mNq': 'business',
    }
    plan = price_map.get(price_id, 'standard')
    access = generate_access(customer_email, plan)
    print(f"Access granted: {customer_email} -> {PLANS[plan]['name']}")
    print(f"Token: {access['token'][:60]}...")
    print(f"Videos: {', '.join(access['videos'])}")
    return access

if __name__ == '__main__':
    handle_payment('test@example.com', 'price_1U3IDHBrWAEI1HPaB0ifC24F')
