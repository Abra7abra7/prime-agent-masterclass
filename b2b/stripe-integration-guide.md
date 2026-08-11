# Stripe Integration Guide — Prime Agent Masterclass

> **Company:** ASCENTIA s. r. o.  
> **Stripe status:** ✅ Registered

---

## 1. Skool + Stripe (najjednoduchšie riešenie)

Skool má natívnu Stripe integráciu. Stačí:

1. Otvor Skool → Settings → Payments
2. Klikni "Connect with Stripe"
3. Prihlás sa do svojho Stripe účtu
4. Skool automaticky vytvorí Stripe Connect účet
5. Hotovo — Skool bude spracúvať platby cez tvoj Stripe

**Výhoda:** Nemusíš nič programovať. Skool spraví celý checkout flow.

---

## 2. Vlastná landing page + Stripe (cez Stripe Checkout)

Ak chceš predávať aj mimo Skool (napr. cez vlastnú landing page):

1. Vytvor Stripe Product v Dashboard
2. Vytvor Stripe Payment Link
   - Stripe Dashboard → Payment Links → Create
   - Nastav cenu ($197, $297, $497)
   - Nastav "Confirmation page" na URL tvojej ďakovnej stránky
3. Vlož Payment Link tlačidlo do landing-page-en.html
4. Stripe pošle automatický email zákazníkovi po zaplatení

**Alebo cez Stripe Checkout (viac kontroly):**
```html
<script src="https://js.stripe.com/v3/"></script>
<button id="checkout-button">Buy Now - $197</button>
<script>
const stripe = Stripe('pk_live_tvoj_public_key');
document.getElementById('checkout-button').addEventListener('click', () => {
  stripe.redirectToCheckout({
    lineItems: [{price: 'price_tvoj_price_id', quantity: 1}],
    mode: 'payment',
    successUrl: 'https://tvojadomena.sk/success',
    cancelUrl: 'https://tvojadomena.sk/cancel',
  });
});
</script>
```

---

## 3. Čo nastaviť v Stripe Dashboard

### Produkty (Products)
| Produkt | Cena | Popis |
|---------|:----:|-------|
| Prime Agent Masterclass - Founder | $197 | Full course + 6 months community |
| Prime Agent Masterclass - Standard | $297 | Full course + 12 months community |
| Prime Agent Masterclass - Pro | $497 | Full course + lifetime access |
| Prime Agent Masterclass - Team B2B | €997 | 5 seats |
| Prime Agent Masterclass - Business B2B | €2,497 | 20 seats + workshop |
| Prime Agent Masterclass - Enterprise B2B | €4,997+ | Unlimited (custom) |

### Nastavenia (Settings)
- [ ] **Business profile** — vyplniť IČO, DIČ, adresu (Klincová 37/B, 821 08)
- [ ] **Bank account** — pripojiť business bankový účet pre výplaty
- [ ] **Statement descriptor** — "ASCENTIA" (zobrazí sa na výpise)
- [ ] **Customer portal** — zapnúť (zákazníci si spravujú predplatné sami)
- [ ] **Email receipts** — nastaviť odosielanie potvrdení

### Dôležité: Stripe Tax
Stripe vie automaticky počítať DPH podľa krajiny zákazníka:
- Stripe Dashboard → Settings → Tax
- Zapnúť Stripe Tax (automatické)
- Nastaviť: SK = 23% DPH, EU firmy = 0% (reverse charge), EU fyzické osoby = podľa krajiny

---

## 4. Testovací mód

Pred ostrým spustením:
1. Stripe Dashboard → Prepnúť na "Test mode"
2. Použiť testovaciu kartu: `4242 4242 4242 4242`
3. Otestovať celý nákupný flow
4. Potom prepnúť na "Live mode"

---

## 5. Užitočné linky

- Stripe Dashboard: https://dashboard.stripe.com
- Stripe Tax: https://dashboard.stripe.com/tax
- Stripe Products: https://dashboard.stripe.com/products
- Stripe API docs: https://stripe.com/docs
- Skool Payments: https://help.skool.com/payments
