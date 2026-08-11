# Telegram Bot → Prime Agent

## Setup (3 minúty)

### 1. Vytvor bota cez @BotFather
- Otvor Telegram → nájdi @BotFather
- `/newbot` → meno → username
- Dostaneš TOKEN

### 2. Nastav token
```bash
export TELEGRAM_BOT_TOKEN="tvoj_token_od_botfathera"
```

### 3. Spusti
```bash
cd telegram-bot
./start.sh
```

### 4. Používaj z mobilu
Pošli správu svojmu botovi na Telegrame a Prime Agent odpovie!

---

## Príklady správ
```
vygeneruj mi LinkedIn post o AI agentoch
sprav prieskum konkurencie pre SaaS v oblasti HR
vytvor twitter thread o automatizácii
```

## Tipy
- Bot beží kým je PC zapnutý a skript spustený
- Každá správa = nové volanie Prime Agenta (trvá pár sekúnd)
- Dlhé odpovede prídu ako .txt súbor
